from django.shortcuts import render
from . import models
from django.views.generic import ListView, DeleteView
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger

# Create your views here.
def catalog(request):
    items = models.ShopItem.objects.all()
    paginator = Paginator(items, 8) # Show 25 contacts per page
    page = request.GET.get('page')
    items = paginator.get_page(page)
    return render(request, 'catalog.html', {'items': items})