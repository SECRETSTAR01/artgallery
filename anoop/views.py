from django.shortcuts import render, HttpResponse
from django.core.files.storage import FileSystemStorage
from .forms import *

def menu(request):
    return render(request, 'index.html')

def contact(request):
    return render(request, 'contact.html')

def pricing(request):
    return render(request, 'pricing.html')

def homepage(request):
    return render(request, 'home.html')

def artwork(request):
    return render(request, 'artwork.html')

def portrait(request):
    return render(request, 'portrait.html')

def payment(request):
    return render(request, 'payment.html')

def about(request):
    return render(request, 'about.html')

def upload(request):
    form = ArtForm()
    return render(request, 'upload.html', {'form': form})