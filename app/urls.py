from django.urls import path, re_path, include
from django.contrib import admin
from .views import homepage

urlpatterns = [
    path('', homepage, name='home_page'),
    re_path(r'^', include('app.modules.main.main_url')),
]
