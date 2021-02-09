from django.shortcuts import render
from .models import Picture
from .models import Item

# Create your views here.
def home(request):
    return render(request, 'mainPage/index.html')
    
def registry(request):
    items = Item.objects.all()
    return render(request, 'mainPage/registry.html', {'items':items})
    
def rsvp(request):
    return render(request, 'mainPage/rsvp.html')
    
def photos(request):
    pictures = Picture.objects.all()
    return render(request, 'mainPage/photos.html', {'pictures':pictures})



  
    

 