from django.conf.urls import url
from news import views as news_views

urlpatterns = [
    url(r'^$', news_views.articles_list)
]