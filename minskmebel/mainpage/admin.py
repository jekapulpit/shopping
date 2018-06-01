from django.contrib import admin
from mainpage.models import slider1fill
from mainpage.models import slider2fill
from mainpage.models import slider3fill
from mainpage.models import shops
from mainpage.models import Collection
from mainpage.models import Sale
from mainpage.models import New


# Register your models here.
admin.site.register(slider1fill)
admin.site.register(slider2fill)
admin.site.register(slider3fill)
admin.site.register(shops)
admin.site.register(Collection)
admin.site.register(Sale)
admin.site.register(New)
