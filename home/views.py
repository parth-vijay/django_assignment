from django.shortcuts import render


def home(request):
	return render(request, 'home.html')

def product(request):
	return render(request, 'product.html')

def areakey(request):
	return render(request, 'areakey.html')
# Create your views here
