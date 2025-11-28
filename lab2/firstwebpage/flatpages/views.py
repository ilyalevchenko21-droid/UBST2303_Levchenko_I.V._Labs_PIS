from django.shortcuts import render
from django import template

# Главная страница — возвращает HTML
def home(request):
    return render(request, 'index.html')

def hello(request):
    return render(request, 'static_handler.html')
