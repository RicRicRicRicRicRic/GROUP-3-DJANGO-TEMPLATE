from django.shortcuts import render

def home(request):
    return render(request, 'Home.html')

def level(request):
    return render(request, 'Level.html')

def easyQ(request):
    return render(request, 'EasyQ.html')

def medQ(request):
    return render(request, 'MedQ.html')

def hardQ(request):
    return render(request, 'HardQ.html')