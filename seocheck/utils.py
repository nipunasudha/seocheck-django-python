from celery.result import AsyncResult

from seotoolset import get_webpage
from .tasks import *
from pyquery import PyQuery as pq


def shout():
    print("OHOHOHOHO!")


def launch_all_get_result_list(url):
    print("URL: " + url)
    result_list = {}
    result1 = task_1_get_css_status.delay(url)
    result_list['task_1_get_css_status'] = result1.task_id
    result2 = task_2_get_keyword_density.delay(url)
    result_list['task_2_get_keyword_density'] = result2.task_id
    result3 = task_3_get_sitemap_list.delay(url)
    result_list['task_3_get_sitemap_list'] = result3.task_id
    result4 = task_4_get_favicon.delay(url)
    result_list['task_4_get_favicon'] = result4.task_id
    print("XXXXXXXXXXXXXX launch_all_get_result_list() output")
    print(result_list)
    return result_list


def generate_status_list(task_list):
    print("XXXXXXXXXXXXXX First back2obj task id")
    print(task_list['task_1_get_css_status'])
    status_list = {}
    print("||||||||||||||||||||| STARTING TRACEBACK ||||||||")
    for task_name, task_id in task_list.items():
        print("XXXXXXXXXXXXXX task ids looping in generate()")
        print("TNAME: " + task_name + "   TID: " + task_id)
        result = AsyncResult(task_id)
        print("TRESULT: ")
        print(result.result)
        print("____________ TRACE ________________")
        print(result.traceback)
        print("____________ END TRACE ________________")
        status_list[task_name] = result.result
    print("||||||||||||||||||||| ENDING TRACEBACK ||||||||")
    return status_list
