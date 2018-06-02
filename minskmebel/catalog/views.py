from django.shortcuts import render
from . import models
from mainpage.models import shops, Sale, New

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
    sortparam = request.GET.get('priority');
    if (sortparam is None or sortparam is ""):
        sortparam = 'Category'
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
    allshops = models.shops.objects.all()
    allitems = models.Collection.objects.all()
    for objj in allitems:
        values.append(objj.price)
    minvalue = min(values)
    maxvalue = max(values)
    if min1 is None or '':
        min1 = minvalue
    if max1 is None or '':
        max1 = maxvalue
    if Categoty is None:
        items2 = models.Collection.objects.all().order_by(sortparam)
    else:
        items2 = models.Collection.objects.filter(Category=categories[Categoty]).order_by(sortparam)
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
    paginator = Paginator(items, 8)
    page = request.GET.get('page')
    if (page is None or page == ''):
        page = 1
    try:
        items = paginator.page(page)
    except PageNotAnInteger:
        # If page is not an integer, deliver first page.
        items = paginator.page(1)
    except EmptyPage:
        # If page is out of range (e.g. 9999), deliver last page of results.
        items = paginator.page(paginator.num_pages)
    return render(request, 'allcollections.html', {'items': items,
                                            'shops': allshops,
                                            'min': minvalue,
                                            'max': maxvalue,
                                            'max1': max1,
                                            'min1': min1,
                                            'category': Categoty,
                                            'sort': sortparams1,
                                            'priority' : sortparam,
                                            'minpage' : int(page) - 2,
                                            'maxpage': int(page) + 2,
                                            'maxpage1': int(paginator.num_pages) - 1,})



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
    sortparam = request.GET.get('priority');
    if(sortparam is None or sortparam is ""):
        sortparam  = '-isdiscount'
    if(request.GET.get('opt') == 'add'):
        sortparams1.append(SORT)
    else:
        if(request.GET.get('opt') == 'del'):
            sortparams1.remove(SORT)

    values = [];
    allshops = models.shops.objects.all()
    allitems = models.ShopItem.objects.all()
    for objj in allitems:
        values.append(objj.newprice)
    minvalue = min(values)
    maxvalue = max(values)
    if min1 is None or min1 is '':
        min1 = minvalue
    if max1 is None or max1 is '':
        max1 = maxvalue
    if Categoty is None:
        items2 = models.ShopItem.objects.all().order_by(sortparam)
    else:
        items2 = models.ShopItem.objects.filter(Category = categories[Categoty]).order_by(sortparam)
    items1 = []
    for objj in items2:
        if float(objj.newprice) >= float(min1) and float(objj.newprice) <= float(max1):
            items1.append(objj)
    items = []
    if(sortparams1 != []):
        for objj in items1:
            if objj.seller.title in sortparams1:
                items.append(objj)
    else:
        items = items1
    paginator = Paginator(items, 8)
    page = request.GET.get('page')
    if(page is None or page == ''):
        page = 1
    try:
        items = paginator.page(page)
    except PageNotAnInteger:
        # If page is not an integer, deliver first page.
        items = paginator.page(1)
    except EmptyPage:
        # If page is out of range (e.g. 9999), deliver last page of results.
        items = paginator.page(paginator.num_pages)
    return render(request, 'catalog.html', {'items': items,
                                            'shops':allshops,
                                            'min':minvalue,
                                            'max' : maxvalue,
                                            'max1' : max1,
                                            'min1' : min1,
                                            'category': Categoty,
                                            'sort': sortparams1,
                                            'priority' : sortparam,
                                            'minpage' : int(page) - 2,
                                            'maxpage': int(page) + 2,
                                            'maxpage1': int(paginator.num_pages) - 1,})



def shoppage(request, shopid):
    item = models.shops.objects.get(id = shopid)
    Staff = models.ShopItem.objects.filter(seller = item)
    context = {"item" : item, "staff" : Staff}
    return render(request, 'shoppage.html', context)



def shops(request):
        allshops = models.shops.objects.all()
        news = New.objects.all()
        return render(request, 'shop.html', {'shops' : allshops, 'news': news} )

def sales(request, num):
    sale = Sale.objects.get(id=num);
    allsales = Sale.objects.all()
    alldiscounts1 = models.ShopItem.objects.all();
    alldiscounts = []
    for objj in alldiscounts1:
        if objj.isdiscount:
            alldiscounts.append(objj)
    return render(request, 'sales.html', {'sale': sale, 'slider2': alldiscounts})

def allsales(request):
    allsales = Sale.objects.all()
    alldiscounts1 = models.ShopItem.objects.all();
    alldiscounts = []
    for objj in alldiscounts1:
        if objj.isdiscount:
            alldiscounts.append(objj)
    return render(request, 'allsales.html', {'sales': allsales, 'slider2': alldiscounts})


def allnews(request):
    allnews = New.objects.all()
    alldiscounts1 = models.ShopItem.objects.all();
    alldiscounts = []
    for objj in alldiscounts1:
        if objj.isdiscount:
            alldiscounts.append(objj)
    return render(request, 'allnews.html', {'news': allnews, 'slider2': alldiscounts})

def news(request, num):
    new = New.objects.get(id=num);
    alldiscounts1 = models.ShopItem.objects.all();
    alldiscounts = []
    for objj in alldiscounts1:
        if objj.isdiscount:
            alldiscounts.append(objj)
    return render(request, 'news.html', {'new': new, 'slider2': alldiscounts})

def contacts(request):
    return render(request, 'contacts.html')
