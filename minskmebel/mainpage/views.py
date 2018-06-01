from django.shortcuts import render
from . import models
from catalog.models import ShopItem
# Create your views here.
def index(request):
        slider1 = models.slider1fill.objects.all()
        slider = ShopItem.objects.all()

        slider3 = models.slider3fill.objects.all()
        slider2 = []
        for objj in slider:
                if objj.isdiscount:
                        slider2.append(objj)
        shops = models.shops.objects.all()[:8]
        context={"slider1":slider1, "slider2":slider2, "slider3":slider3, "shops":shops}
        return render(request,'index.html', context)