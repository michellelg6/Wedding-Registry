from django.shortcuts import render
from django.http import HttpResponse
from .models import Picture
from .models import Item
from .models import Guest

# Create your views here.
def home(request):
    return render(request, 'mainPage/index.html')
    
def registry(request):
    items = Item.objects.all()
    return render(request, 'mainPage/registry.html', {'items':items})
    
def rsvp(request):
    return render(request, 'mainPage/rsvp.html')
    
def thanks(request):
    thename = request.POST.get('name')
    theemail = request.POST.get('email')
    
    g = Guest(name=thename, email=theemail)
    g.save()
   
    return render(request, 'mainPage/thankYou.html', {'name': thename})
   
    
    return HttpResponse('<h1>Success!</h1>')
def photos(request):
    pictures = Picture.objects.all()
    return render(request, 'mainPage/photos.html', {'pictures':pictures})



  
    

 