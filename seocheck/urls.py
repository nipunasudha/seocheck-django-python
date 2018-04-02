from django.conf.urls import url
from seocheck import views as seocheck_views

urlpatterns = [
    url(r'^$', seocheck_views.get_seocheck, name='get_seocheck'),
    url(r'^results/$', seocheck_views.get_seocheck_results, name='get_seocheck_results'),
    url(r'^ajax/$', seocheck_views.ajax_seocheck_results, name='ajax_seocheck_results'),
]
