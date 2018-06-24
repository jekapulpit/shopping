from django.shortcuts import render
from . import models
from mainpage.models import shops, Sale, New

from django.views.generic import ListView, DeleteView
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from mainpage import forms

from django.shortcuts import render_to_response
from django.core.mail import send_mail
from django.http import HttpResponse
from django.template import RequestContext
from django.http import HttpResponseRedirect

sortparams1 = []
# Create your views here.
def Tovar(request, number):
    item = models.ShopItem.objects.get(id = number)
    form =forms.ContactForm()
    SimularItems = models.ShopItem.objects.filter(Category=item.Category).exclude(id = item.id)
    context = {"item" : item, "SimularItems" : SimularItems, "form" : form}
    return render(request, 'tovar.html', context)

def collection(request, number):
    item = models.Collection.objects.get(id=number)
    form =forms.ContactForm()

    inCollection1 = models.ShopItem.objects.filter(inCollection=item)
    SimularItems = models.ShopItem.objects.filter(Category=item.Category)
    context = {'items': inCollection1, 'item':item, 'SimularItems' : SimularItems, "form" : form}
    return render(request, 'collection.html', context)

def collections(request):
    form =forms.ContactForm()

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
        if (request.GET.get('opt') == 'del' and SORT in sortparams1):
            try:
                sortparams1.remove(SORT)
            except ValueError:
                pass


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
    if Categoty == None or Categoty == "" or Categoty == 'None':
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
                                            'maxpage1': int(paginator.num_pages) - 1,
                                            "form" : form})




def catalog1(request):
    form =forms.ContactForm()

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
    if(request.GET.get('opt') == 'add' and request.GET.get('opt') not in sortparams1):
        sortparams1.append(SORT)
    else:
        if(request.GET.get('opt') == 'del'):
            try:
                sortparams1.remove(SORT)
            except ValueError:
                pass

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
    if Categoty == None or Categoty == "" or Categoty == 'None':
        items2 = models.ShopItem.objects.all().order_by(sortparam)
    else:
        items2 = models.ShopItem.objects.filter(Category = categories[Categoty]).order_by(sortparam)
    items1 = []
    for objj in items2:
        if (float(objj.newprice) >= float(min1) and float(objj.newprice) <= float(max1)) or (objj.newprice == 0.0) :
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
                                            'maxpage1': int(paginator.num_pages) - 1, "form" : form})



def shoppage(request, shopid):
    form =forms.ContactForm()

    item = models.shops.objects.get(id = shopid)
    Staff = models.ShopItem.objects.filter(seller = item)
    categories = []
    check = []
    links = []
    linktemplate = {
     'Мягкая мебель' : "softmebel", 
     'Гостиная' :  "leavingroom",
     'Спальня' : "bedroom",
     'Кухня' : "kitchen",
     'Столовая' : "stolovaya",
     'Прихожая' : "inner",
     'Ванная' :"bathroom",
     'Детская' : "childroom",
     'Рабочий кабинет' :  "office",
    }
    categoryTemplate = {
        1: 'Мягкая мебель',
        2: 'Гостиная',
        3: 'Спальня',
        4: 'Кухня',
        5: 'Столовая',
        6: 'Прихожая',
        7: 'Ванная',
        8: 'Детская',
        9: 'Рабочий кабинет',
    }
    lastitem='heh'
    for item1 in Staff:
        if item1.Category not in check:
            categories.append(categoryTemplate[int(item1.Category)])
            check.append(item1.Category)
    if categories != []:        
        lastitem = categories[-1]
    context = {"item" : item, "staff" : Staff, "categories" : categories, "lastitem"  : lastitem, "form" : form}
    return render(request, 'shoppage.html', context)



def shops(request):
        form =forms.ContactForm()

        allshops = models.shops.objects.all()
        news = New.objects.all()
        return render(request, 'shop.html', {'shops' : allshops, 'news': news, "form" : form } )

def sales(request, num):
    form =forms.ContactForm()

    sale = Sale.objects.get(id=num);
    allsales = Sale.objects.all()
    alldiscounts1 = models.ShopItem.objects.all();
    alldiscounts = []
    for objj in alldiscounts1:
        if objj.isdiscount:
            alldiscounts.append(objj)
    return render(request, 'sales.html', {'sale': sale, 'slider2': alldiscounts, "form" : form})

def allsales(request):
    form =forms.ContactForm()

    allsales = Sale.objects.all()
    alldiscounts1 = models.ShopItem.objects.all();
    alldiscounts = []
    for objj in alldiscounts1:
        if objj.isdiscount:
            alldiscounts.append(objj)
    return render(request, 'allsales.html', {'sales': allsales, 'slider2': alldiscounts, "form" : form})


def allnews(request):
    form =forms.ContactForm()

    allnews = New.objects.all()
    alldiscounts1 = models.ShopItem.objects.all();
    alldiscounts = []
    for objj in alldiscounts1:
        if objj.isdiscount:
            alldiscounts.append(objj)
    return render(request, 'allnews.html', {'news': allnews, 'slider2': alldiscounts, "form" : form})

def news(request, num):
    form =forms.ContactForm()
    new = New.objects.get(id=num)
    alldiscounts1 = models.ShopItem.objects.all()
    alldiscounts = []
    for objj in alldiscounts1:
        if objj.isdiscount:
            alldiscounts.append(objj)
    return render(request, 'news.html', {'new': new, 'slider2': alldiscounts, "form" : form})

def contacts(request):
    form =forms.ContactForm()
    form1 = forms.SendMessage()

    if request.method == 'POST':
                form1 = forms.SendMessage(request.POST)
        # Если форма заполнена корректно, сохраняем все введённые пользователем значения
                if form1.is_valid():
                    subject = form1.cleaned_data['subject']
                    sender = form1.cleaned_data['sender']
                    message = form1.cleaned_data['message']
                    mess= ("E-mail отправителя: " + sender + ", Сообщение: " + message)    
                    myem = ['tcminskmebel@gmail.com']
                    # Если пользователь захотел получить копию себе, добавляем его в список получателей
                   
                    try:
                        send_mail(subject, mess, 'q020@bk.ru', myem)
                    except Exception: #Защита от уязвимости
                        return HttpResponse('Invalid header found')
                    # Переходим на другую страницу, если сообщение отправлено
                    return HttpResponseRedirect('/')
    return render(request, 'contacts.html', {"form" : form, "form1" : form1})

def arend(request):
    form =forms.ContactForm()
    alldiscounts = []
    
    alldiscounts1 = models.ShopItem.objects.all()
    for objj in alldiscounts1:
        if objj.isdiscount:
            alldiscounts.append(objj)
    return render(request, 'arend.html', {'slider2': alldiscounts, "form" : form})