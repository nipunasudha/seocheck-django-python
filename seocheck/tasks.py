# Create your tasks here
from __future__ import absolute_import, unicode_literals
import time
from celery import shared_task
from pyquery import PyQuery as pq

from toolset import get_table_status


@shared_task
def launch_all(url):
    nesting_status = get_table_status("http://www.yourhtmlsource.com/tables/nestingtables.html")
    return nesting_status


@shared_task
def sub1():
    time.sleep(2)
    return "ONE"


@shared_task
def sub2():
    time.sleep(4)
    return "TWO"


@shared_task
def sub3():
    time.sleep(6)
    return "THREE"
