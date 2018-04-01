from django.conf.urls import url
from seocheck import views as seocheck_views

urlpatterns = [
    url(r'^$', seocheck_views.get_seocheck)
]