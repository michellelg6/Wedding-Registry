from django.shortcuts import render

# Create your views here.
def photos():
    return render(request, 'photos/photos.html')