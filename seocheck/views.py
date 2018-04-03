import time

from celery import group
from django.shortcuts import render
from django.http import HttpResponseRedirect
from .forms import SeocheckForm
from django.core.urlresolvers import reverse as route_url
from celery.result import AsyncResult, GroupResult
import json
from django.http import JsonResponse
from django.http import HttpResponse
from .tasks import sub1, sub2, sub3

global_job_list = []


def get_seocheck(request):
    global global_job_list
    if request.method == 'POST':
        form = SeocheckForm(request.POST)
        if form.is_valid():
            seoUrl = form.cleaned_data['seoUrl']
            # task_results = launch_all.delay(seoUrl)
            job = group([sub1.s(), sub2.s(), sub3.s()])
            task_results = job.apply_async()
            request.session['seocheck_task_index'] = len(global_job_list)
            global_job_list.append(task_results)
            request.session['seocheck_url'] = seoUrl
            # return HttpResponseRedirect('/thanks/')
            return HttpResponseRedirect(route_url('get_seocheck_results', args=[]))
    else:
        form = SeocheckForm()
    return render(request, 'seocheck/home.html', {'form': form})


def get_seocheck_results(request):
    seocheck_task_id = request.session.get('seocheck_task_id')
    if not seocheck_task_id:
        return HttpResponseRedirect(route_url('get_seocheck', args=[]))
    return render(request, 'seocheck/seocheck.html')


def ajax_seocheck_results(request):
    global global_job_list
    print("AJAX")
    # return {'a': 'b'}
    response_data = {}
    # ==========================================
    seocheck_task_index = int(request.session.get('seocheck_task_index'))
    seocheck_url = request.session.get('seocheck_url')
    seocheck_results = global_job_list[seocheck_task_index]
    print(seocheck_results.completed_count())
    # print(seocheck_results.result)
    # print(seocheck_results.ready())
    # print(seocheck_results.get(timeout=1))
    # print(seocheck_results.traceback)

    # ==========================================
    response_data['status'] = 'success'
    response_data['url'] = seocheck_url
    response_data['result'] = seocheck_results.completed_count()
    return JsonResponse(response_data)
