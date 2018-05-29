

from django.urls import path, re_path
from django.views.generic import ListView, DeleteView
from mainpage.models import slider1fill
from . import views
urlpatterns = [
    re_path(r'^$', views.index),
    re_path(r'index/', views.index),

]
