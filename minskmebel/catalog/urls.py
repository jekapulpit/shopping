

from django.urls import path, re_path
from django.views.generic import ListView, DeleteView
from . import views
urlpatterns = [
    re_path(r'^$', views.catalog),
    re_path(r'^(?P<number>[0-9]+)/', views.Tovar),

]
