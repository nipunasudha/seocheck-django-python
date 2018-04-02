# Create your tasks here
from __future__ import absolute_import, unicode_literals
from celery import shared_task
from toolset import *

@shared_task
def launch_all(url):
    nesting_status = get_table_status("http://www.yourhtmlsource.com/tables/nestingtables.html")
    return nesting_status
