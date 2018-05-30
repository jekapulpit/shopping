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

]
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)