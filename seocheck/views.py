import time

from django.shortcuts import render
from toolset import *
from django.http import HttpResponseRedirect
from .forms import SeocheckForm
from django.core.urlresolvers import reverse as route_url
from celery.result import AsyncResult
import json
from django.http import JsonResponse
from django.http import HttpResponse
from .tasks import launch_all

# Create your views here.
def articles_list(request):
    nesting_status = get_table_status("http://www.yourhtmlsource.com/tables/nestingtables.html")
    return render(request, 'seocheck/home.html', {'nesting_status': nesting_status})


def get_seocheck(request):
    if request.method == 'POST':
        form = SeocheckForm(request.POST)
        if form.is_valid():
            print("%%%%%%%%%%%%%%%%%%% HOME %%%%%%%%%%%%%%%%%%%")
            seoUrl = form.cleaned_data['seoUrl']
            task_results = launch_all.delay(seoUrl)
            print("--------------- traceback ---------------")
            print(task_results.traceback)
            time.sleep(1)
            request.session['seocheck_task_id'] = task_results.task_id
            print(seoUrl)
            print("Heyyyyyyyyyyyyyyyyyyy down hereeee!")
            print(task_results.ready())
            # return HttpResponseRedirect('/thanks/')
            return HttpResponseRedirect(route_url('get_seocheck_results', args=[]))
    else:
        form = SeocheckForm()
    print("%%%%%%%%%%%%%%%%%%% END HOME %%%%%%%%%%%%%%%%%%%")
    return render(request, 'seocheck/home.html', {'form': form})


def get_seocheck_results(request):
    seocheck_task_id = request.session.get('seocheck_task_id')
    if not seocheck_task_id:
        return HttpResponseRedirect(route_url('get_seocheck', args=[]))
    seocheck_results = AsyncResult(seocheck_task_id)
    print(seocheck_results)
    if request.method == 'GET':
        print("THIS IS GET")
    return render(request, 'seocheck/seocheck.html')


def ajax_seocheck_results(request):
    print("AJAX")
    # return {'a': 'b'}
    response_data = {}
    # ==========================================
    seocheck_task_id = request.session.get('seocheck_task_id')
    seocheck_results = AsyncResult(seocheck_task_id)
    print("%%%%%%%%%%%%%%%%%%% RESULT PAGE %%%%%%%%%%%%%%%%%%%")
    print(seocheck_results.result)
    print(seocheck_results.ready())
    # print(seocheck_results.get(timeout=1))
    print(seocheck_results.traceback)

    # ==========================================
    response_data['result'] = 'success'
    response_data['data'] = seocheck_results.result
    print("%%%%%%%%%%%%%%%%%%% END RESULT PAGE %%%%%%%%%%%%%%%%%%%")
    return JsonResponse(response_data)
