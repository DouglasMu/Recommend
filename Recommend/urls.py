"""Recommend URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.0/topics/http/urls/
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

from app import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('login/',views.login),
    path('register/',views.register),
    path('main/',views.main),
    path('feature/', views.feature),
    path('index/' ,views.index),
    path('charts/',views.charts),
    path('log/',views.log),
    path('test/',views.test),
    path('phone/',views.phone),
    path('netbook/',views.netbook_m),
    path('pad/',views.pad_m),
    path('phone_search/',views.phonesearch),
    path('netbook_search/',views.netbooksearch),
    path('pad_search/',views.padsearch)
]
