import time

# from celery import group
from django.shortcuts import render
from django.http import HttpResponseRedirect

from seocheck.utils import shout, launch_all_get_result_list, generate_status_list
from toolset import get_clean_text
from .forms import SeocheckForm
from django.core.urlresolvers import reverse as route_url
from celery.result import AsyncResult, GroupResult
import json
from django.http import JsonResponse
from django.http import HttpResponse
from .tasks import task_1_get_css_status, task_2_get_keyword_density, task_3_get_sitemap_list


def get_seocheck(request):
    global global_job_list
    if request.method == 'POST':
        form = SeocheckForm(request.POST)
        if form.is_valid():
            seoUrl = form.cleaned_data['seoUrl']
            # task_results = launch_all.delay(seoUrl)
            # job = group([sub1.s(), sub2.s(), sub3.s()])
            # task_results = job.apply_async()
            # print(json.dumps(launch_all_get_result_list(seoUrl)))
            # print(json.dumps({'xx':'yy'})) 
            request.session['seocheck_task_list'] = json.dumps(launch_all_get_result_list(seoUrl))
            # request.session['seocheck_task_list'] = json.dumps({'xx':'yy'})
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
    # return {'a': 'b'}
    response_data = {}
    # ==========================================
    seocheck_task_list = json.loads(request.session.get('seocheck_task_list'))
    print("TASK LIST CAME DOWN!")
    print(seocheck_task_list)
    seocheck_url = request.session.get('seocheck_url')
    status_list = generate_status_list(seocheck_task_list)
    print("^^^^^^^^^^^^^^^^^^status list")
    print(status_list)
    # print(seocheck_results.result)
    # print(seocheck_results.ready())
    # print(seocheck_results.get(timeout=1))
    # print(seocheck_results.traceback)
    shout()
    # ==========================================
    response_data['status'] = 'success'
    response_data['url'] = seocheck_url
    response_data['result'] = json.dumps(status_list)
    return JsonResponse(response_data)
