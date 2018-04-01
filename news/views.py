from django.shortcuts import render
from toolset import *


# Create your views here.
def articles_list(request):
    nesting_status = get_table_status("http://www.yourhtmlsource.com/tables/nestingtables.html")
    return render(request, 'news/articles_list.html', {'nesting_status': nesting_status})
