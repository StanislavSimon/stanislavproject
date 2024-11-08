from django.shortcuts import render


def home(request):
    return render(request, 'home.html')


def shop(request):
    return render(request, 'shop.html')


def about(request):
    return render(request, 'about.html')

# Create your views here.
