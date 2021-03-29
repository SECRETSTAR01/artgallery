from django.shortcuts import render, HttpResponse

def menu(request):
    return render(request, 'index.html')

def contact(request):
    return render(request, 'contact.html')

def pricing(request):
    return render(request, 'pricing.html')

def homepage(request):
    return render(request, 'home.html')