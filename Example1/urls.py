from django.contrib import admin
from django.contrib.auth.models import User
from django.conf.urls import url, include
from django.urls import path, re_path

from Example1 import views


urlpatterns = [
    
    re_path(r'example1/$', views.ExampleList.as_view()),
    re_path(r'example1_detail/(?P<id>\d+)/$', views.ExampleList.as_view()),

]
