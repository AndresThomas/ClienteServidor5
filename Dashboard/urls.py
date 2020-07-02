from django.urls import include, re_path,path 


from Dashboard.views import DashboardClass

app_name = 'Dashboard'
urlpatterns = [
    path('Dashboard',DashboardClass.as_view(), name = 'Dashboard')
]