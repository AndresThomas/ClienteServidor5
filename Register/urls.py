from django.urls import include, re_path,path 
from Register.views import RegisterClass

app_name = 'Register'

urlpatterns = [
    path('',RegisterClass.as_view(), name = 'Register'),
]