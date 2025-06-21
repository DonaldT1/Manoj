from django.shortcuts import render

def home(request):
    return render(request, 'index.html')

def flat(request):
    return render(request, 'flat.html')

def car(request):
    return render(request, 'car.html')

def bike(request):
    return render(request, 'bike.html')

def laptop(request):
    return render(request, 'leptop.html')

def mobile(request):
    return render(request, 'mobile.html')

def more(request):
    return render(request, 'more.html')