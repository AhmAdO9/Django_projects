"""
URL configuration for TO_DO_LIST project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
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
from django.urls import path
from App.views import *





urlpatterns = [
    path('admin/', admin.site.urls),
    
    path('create/', create, name='create'),
    path('read/one/<id>/', read_id, name='read'),
    path('read/all/', read_all, name='all'),
    path('update/<id>/', update, name='update'),
    path('delete/<id>/', delete_id, name='delete'),
    path('authenticate/', authentication, name='authenticate'),
]                                           


