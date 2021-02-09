from django.shortcuts import render


# Create your views here.
def regPage():
    return render(request, 'regPage/regPage.html')