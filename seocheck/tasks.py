# Create your tasks here
from __future__ import absolute_import, unicode_literals
import time
from celery import shared_task
from pyquery import PyQuery as pq

from toolset import get_table_status, get_keyword_density, check_h2_tags, get_robot_instance, \
    get_css_status


@shared_task
def launch_all(url):
    nesting_status = get_table_status("http://www.yourhtmlsource.com/tables/nestingtables.html")
    return nesting_status


@shared_task
def task_1_get_css_status(url):
    # return get_css_status(url)
    return {'bad': 888}


@shared_task
def task_2_get_keyword_density(url):
    return get_keyword_density(url)


@shared_task
def task_3_check_h2_tags(url):
    robot = get_robot_instance(url)
    return check_h2_tags(robot)
