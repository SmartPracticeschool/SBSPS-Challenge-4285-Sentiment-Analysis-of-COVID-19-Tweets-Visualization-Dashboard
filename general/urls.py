

from django.contrib import admin
from django.urls import path
from .views import index,analysis

urlpatterns = [
    path('', index,name = 'index'),
    path('analysis',analysis,name ='analysis'),
]