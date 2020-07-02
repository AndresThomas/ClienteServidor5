from django.urls import include, re_path,path 
from Landing.views import LandingClass

app_name = 'Landing'
urlpatterns = [
    path('',LandingClass.as_view(), name = 'Landing'),
]