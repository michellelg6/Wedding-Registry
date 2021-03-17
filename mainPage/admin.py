from django.contrib import admin
from .models import Picture
from .models import Item
from .models import Guest

# Register your models here.
admin.site.register(Picture)
admin.site.register(Item)
admin.site.register(Guest)