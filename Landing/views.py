from django.shortcuts import render
from django.views.generic import View
# Create your views here.
class LandingClass(View):
    template = 'Landing/landing.html'
    def get(self, request, *arg, **kargs):
        return render(request, self.template, {})