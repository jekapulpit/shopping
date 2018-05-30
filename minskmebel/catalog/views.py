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

def Tovar(request, number):
    item = models.ShopItem.objects.get(id = number)
    SimularItems = models.ShopItem.objects.filter(Category=item.Category).exclude(id = item.id)
    context = {"item" : item, "SimularItems" : SimularItems}
    return render(request, 'tovar.html', context)

def collection(request, number):
    item = models.Collection.objects.get(id=number)
    inCollection1 = models.ShopItem.objects.filter(inCollection=item)
    context = {'items': inCollection1, 'item':item}
    return render(request, 'collection.html', context)