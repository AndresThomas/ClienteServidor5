from django.urls import include, re_path,path 

from Login2.views import LoginClass


app_name = "Login2"

urlpatterns = [
    path('',LoginClass.as_view(), name = 'Login2'),
]