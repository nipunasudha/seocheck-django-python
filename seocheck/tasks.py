# Create your tasks here
from __future__ import absolute_import, unicode_literals
import time
from celery import shared_task
from pyquery import PyQuery as pq

from toolset.keyword_density import *
from toolset.robot import *
from toolset.keyword_density import *
from toolset.css import *


@shared_task
def launch_all(url):
    # nesting_status = get_table_status("http://www.yourhtmlsource.com/tables/nestingtables.html")
    return None


@shared_task
def task_1_get_css_status(url):
    return get_css_status(url)


@shared_task
def task_2_get_keyword_density(url):
    return get_keyword_density(url)


@shared_task
def task_3_get_sitemap_list(url):
    robot = get_robot_instance(url)
    return get_sitemap_list(robot)
