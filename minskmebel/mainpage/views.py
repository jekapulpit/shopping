from django.shortcuts import render
from . import models
from catalog.models import ShopItem
from django.shortcuts import render_to_response
from django.core.mail import send_mail
from django.http import HttpResponse
from django.template import RequestContext
from django.http import HttpResponseRedirect
from . import forms

def index(request):
        if request.method == 'POST':
                form = forms.ContactForm(request.POST)
        # Если форма заполнена корректно, сохраняем все введённые пользователем значения
                if form.is_valid():
                    subject = form.cleaned_data['subject']
                    sender = form.cleaned_data['sender']
                    phone = form.cleaned_data['phone']
                    time = form.cleaned_data['time']
                    mess= ("E-mail отправителя: " + sender + ", Телефон: " + phone + ", время, в которое удобно звонить: " + time)    
                    myem = ['q010@bk.ru']
                    # Если пользователь захотел получить копию себе, добавляем его в список получателей
                   
                    try:
                        send_mail(subject, mess, 'q020@bk.ru', myem)
                    except Exception: #Защита от уязвимости
                        return HttpResponse('Invalid header found')
                    # Переходим на другую страницу, если сообщение отправлено
                    return HttpResponseRedirect('/')

        else:
            form =forms.ContactForm()
        slider1 = models.slider1fill.objects.all()
        slider = ShopItem.objects.all()
        slider3 = models.New.objects.all()
        slider2 = []
        for objj in slider:
                if objj.isdiscount:
                        slider2.append(objj)
        shops = models.shops.objects.all()[:8]
        context={"slider1":slider1, "slider2":slider2, "slider3":slider3, "shops":shops, "form":form}
        return render(request,'index.html', context)


