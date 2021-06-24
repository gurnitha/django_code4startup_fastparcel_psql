# apps/core/views.py

# Django modules
from django.shortcuts import render

# Create your views here.
def home(request):
	return render(request, 'core/home.html')


def customer_page(request):
	return render(request, 'core/home.html')


def courier_page(request):
	return render(request, 'core/home.html')