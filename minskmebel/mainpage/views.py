from django.shortcuts import render
from . import models
# Create your views here.
def index(request):
        slider1 = models.slider1fill.objects.all()
        slider2 = models.slider2fill.objects.all()
        context={"slider1":slider1, "slider2":slider2}
        return render(request,'index.html', context)