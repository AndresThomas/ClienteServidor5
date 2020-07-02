from django.contrib import admin
from django.contrib.auth.models import User
from django.conf.urls import url, include
from django.urls import path, re_path

from Example2 import views


urlpatterns = [
    
    re_path(r'example2/$', views.ExampleList.as_view()),

]
