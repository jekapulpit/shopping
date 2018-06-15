from django.conf.urls.static import static
from . import settings
from django.contrib import admin
from django.urls import path, re_path, include
from catalog import views

urlpatterns = [
    path('admin/', admin.site.urls),
    re_path(r'^', include('mainpage.urls')),
    re_path(r'^catalog/', include('catalog.urls')),
    re_path(r'^shops/(?P<shopid>[0-9]+)/', views.shoppage),
    re_path(r'^shops/$', views.shops),
    re_path(r'^sales/(?P<num>[0-9]+)/', views.sales),
    re_path(r'^sales/$', views.allsales),
    re_path(r'^news/(?P<num>[0-9]+)/', views.news),
    re_path(r'^news/$', views.allnews),
    re_path(r'^contacts/$', views.contacts),
    re_path(r'^arend/$', views.arend),

]
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)