from celery.result import AsyncResult

from toolset import get_webpage
from .tasks import task_1_get_css_status, task_2_get_keyword_density, task_3_check_h2_tags
from pyquery import PyQuery as pq


def shout():
    print("OHOHOHOHO!")


def launch_all_get_result_list(url):
    print("URL: " + url)
    page = get_webpage(url, False)
    result_list = {}
    result1 = task_1_get_css_status.delay(url)
    result_list['result1'] = result1.task_id
    result2 = task_2_get_keyword_density.delay(url)
    result_list['result2'] = result2.task_id
    result3 = task_3_check_h2_tags.delay(url)
    result_list['result3'] = result3.task_id
    return result_list


def generate_status_list(task_list):
    status_list = {}
    print("||||||||||||||||||||| STARTING TRACEBACK ||||||||")
    for task_name, task_id in task_list.items():
        result = AsyncResult(task_id)
        status_list[task_name] = str(result.result)
        # print(result.traceback)
    print("||||||||||||||||||||| ENDING TRACEBACK ||||||||")
    return status_list
