"""CS5HOME URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.contrib.auth.models import User
from django.conf.urls import url, include
from django.urls import path, re_path

from rest_framework import routers, serializers, viewsets
from rest_framework_swagger.views import get_swagger_view

from Login2.views import l


class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ['url', 'username', 'email', 'is_staff']

class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer

router = routers.DefaultRouter()
router.register(r'users', UserViewSet)

schema_view = get_swagger_view(title='Pastebin API')

urlpatterns = [
    path('admin/', admin.site.urls),
    re_path(r'^', include(router.urls)),
    re_path(r'^api/v1/example/', include('Example1.urls')),
    re_path(r'^api/v1/example2/', include('Example2.urls')),
    re_path(r'^api/v1/login/', include('Login.urls')),
    path('api/v1/entrar', include('Login2.urls'),name = 'Login2'),
    path('logout/',l.as_view() ,name ='logout'),
    path('api/v1/inicio', include('Dashboard.urls'),name = 'Dashboard'),
    re_path(r'^api/v1/', include('Landing.urls')),
    re_path(r'^api/v1/registrate/', include('Register.urls')),
    
    
    url(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework')),
    url('swagger/', schema_view),
]
