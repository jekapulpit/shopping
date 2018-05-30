

from django.urls import path, re_path
from django.views.generic import ListView, DeleteView
from . import views
urlpatterns = [
    re_path(r'^$', views.catalog1),
    re_path(r'^collections/(?P<number>[0-9]+)/', views.collection),
    re_path(r'^collections/$', views.collections),
    re_path(r'^(?P<number>[0-9]+)/', views.Tovar),
    re_path(r'^(?P<category>[a-z]+)/', views.catalog1),

]
