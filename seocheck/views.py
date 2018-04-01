from django.shortcuts import render
from toolset import *
from django.http import HttpResponseRedirect
from .forms import SeocheckForm


# Create your views here.
def articles_list(request):
    nesting_status = get_table_status("http://www.yourhtmlsource.com/tables/nestingtables.html")
    return render(request, 'seocheck/home.html', {'nesting_status': nesting_status})


def get_seocheck(request):
    if request.method == 'POST':
        form = SeocheckForm(request.POST)
        if form.is_valid():
            # return HttpResponseRedirect('/thanks/')
            print(form.cleaned_data['seoUrl'])
            return render(request, 'seocheck/home.html', {'nesting_status': "Yako wade hari"})
    else:
        form = SeocheckForm()
    return render(request, 'seocheck/home.html', {'form': form})
