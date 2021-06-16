from django.shortcuts import render, HttpResponse
from django.core.files.storage import FileSystemStorage
from .models import *
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
    allimages = ArtModel.objects.all()
    return render(request, 'portrait.html', {'images' : allimages})

def payment(request):
    return render(request, 'payment.html')

def about(request):
    return render(request, 'about.html')

def upload(request):
    if request.method == 'POST':
        form = ArtForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            img_obj = form.instance
            return render(request, 'upload.html', {'form': form, 'img_obj': img_obj})
    else:
        form = ArtForm()
    return render(request, 'upload.html', {'form': form})