from django.shortcuts import render
from django.views.generic import View
from django.shortcuts import redirect
from django.contrib.auth import authenticate
from django.contrib.auth.mixins import LoginRequiredMixin

from Login2.views import LoginClass
# Create your views here.
class DashboardClass(LoginRequiredMixin,View):
    template = 'Dashboard/dashboard.html'
    def get(self, request, *arg, **kargs):
        print("return dash views")
        return render(request, self.template, {})
