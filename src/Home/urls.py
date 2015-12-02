from django.conf.urls import patterns, include, url
from Home import views

urlpatterns = patterns('',


    url(r'^$', views.home, name='home'),


)
