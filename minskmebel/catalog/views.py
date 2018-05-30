from django.shortcuts import render
from . import models
from mainpage.models import shops

from django.views.generic import ListView, DeleteView
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
sortparams1 = []
# Create your views here.
def Tovar(request, number):
    item = models.ShopItem.objects.get(id = number)
    SimularItems = models.ShopItem.objects.filter(Category=item.Category).exclude(id = item.id)
    context = {"item" : item, "SimularItems" : SimularItems}
    return render(request, 'tovar.html', context)

def collection(request, number):
    item = models.Collection.objects.get(id=number)
    inCollection1 = models.ShopItem.objects.filter(inCollection=item)
    SimularItems = models.ShopItem.objects.filter(Category=item.Category)
    context = {'items': inCollection1, 'item':item, 'SimularItems' : SimularItems}
    return render(request, 'collection.html', context)

def collections(request):
    categories = {
        "softmebel": '1',
        "leavingroom": '2',
        "bedroom": '3',
        "kitchen": '4',
        "stolovaya": '5',
        "inner": '6',
        "bathroom": '7',
        "childroom": '8',
        "office": '9',
    }

    min1 = request.GET.get('min1')
    max1 = request.GET.get('max1')
    Categoty = request.GET.get('category')
    SORT = request.GET.get('shopsort')
    if (request.GET.get('opt') == 'add'):
        sortparams1.append(SORT)
    else:
        if (request.GET.get('opt') == 'del'):
            sortparams1.remove(SORT)

    values = [];
    allshops = shops.objects.all()
    allitems = models.Collection.objects.all()
    for objj in allitems:
        values.append(objj.price)
    minvalue = min(values)
    maxvalue = max(values)
    if min1 is None:
        min1 = minvalue
    if max1 is None:
        max1 = maxvalue
    if Categoty is None:
        items2 = models.Collection.objects.all()
    else:
        items2 = models.Collection.objects.filter(Category=categories[Categoty])
    items1 = []
    for objj in items2:
        if float(objj.price) >= float(min1) and float(objj.price) <= float(max1):
            items1.append(objj)
    items = []
    if (sortparams1 != []):
        for objj in items1:
            if objj.seller.title in sortparams1:
                items.append(objj)
    else:
        items = items1
    return render(request, 'allcollections.html', {'items': items,
                                            'shops': allshops,
                                            'min': minvalue,
                                            'max': maxvalue,
                                            'max1': max1,
                                            'min1': min1,
                                            'category': Categoty,
                                            'sort': sortparams1}, )



def catalog1(request):
    categories = {
        "softmebel" : '1',
        "leavingroom": '2',
        "bedroom": '3',
        "kitchen": '4',
        "stolovaya": '5',
        "inner": '6',
        "bathroom": '7',
        "childroom": '8',
        "office": '9',
    }

    min1 = request.GET.get('min1')
    max1 = request.GET.get('max1')
    Categoty = request.GET.get('category')
    SORT = request.GET.get('shopsort')
    if(request.GET.get('opt') == 'add'):
        sortparams1.append(SORT)
    else:
        if(request.GET.get('opt') == 'del'):
            sortparams1.remove(SORT)

    values = [];
    allshops = shops.objects.all()
    allitems = models.ShopItem.objects.all()
    for objj in allitems:
        values.append(objj.price)
    minvalue = min(values)
    maxvalue = max(values)
    if min1 is None:
        min1 = minvalue
    if max1 is None:
        max1 = maxvalue
    if Categoty is None:
        items2 = models.ShopItem.objects.all()
    else:
        items2 = models.ShopItem.objects.filter(Category = categories[Categoty])
    items1 = []
    for objj in items2:
        if float(objj.price) >= float(min1) and float(objj.price) <= float(max1):
            items1.append(objj)
    items = []
    if(sortparams1 != []):
        for objj in items1:
            if objj.seller.title in sortparams1:
                items.append(objj)
    else:
        items = items1
    return render(request, 'catalog.html', {'items': items,
                                            'shops':allshops,
                                            'min':minvalue,
                                            'max' : maxvalue,
                                            'max1' : max1,
                                            'min1' : min1,
                                            'category': Categoty,
                                            'sort': sortparams1},)
