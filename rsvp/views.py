from django.shortcuts import render

# Create your views here.
def rsvp():
    return render(request, 'rsvp/rsvp.html')
 