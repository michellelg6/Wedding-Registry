from django.contrib import admin
from .models import Picture
from .models import Item

# Register your models here.
admin.site.register(Picture)
admin.site.register(Item)