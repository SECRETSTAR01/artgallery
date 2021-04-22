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
    return render(request, 'portrait.html')

def payment(request):
    return render(request, 'payment.html')

def about(request):
    return render(request, 'about.html')

def upload(request):
    if request.method == "POST":
        form=ArtForm(data=request.POST,files=request.FILES)
        if form.is_valid():
            form.save()
            obj=form.instance
            return render(request,"upload.html",{"obj":obj})  
    else:
        form=ArtForm()    
        img=ArtModel.objects.all()
    return render(request,"upload.html",{"img":img,"form":form})