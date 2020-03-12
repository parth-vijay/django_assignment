from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import logout, authenticate
from django.contrib.auth.decorators import login_required
from .models import *
import csv, io
from django.contrib import messages
from django.http import HttpResponseRedirect
from django.urls import reverse
from .forms import *
import json

@login_required(login_url='login/')
def logout_request(request):
	logout(request)
	return redirect('home:login')

def home(request):
	return render(request, 'home.html')

def product(request):
	return render(request, 'product.html')

def areakey(request):
	rowd=[]
	if request.method=='POST':
		form=AreaKeyForm(request.POST, request.FILES)
		if form.is_valid():
			profile=form.save(commit=False)
			profile.user=request.user
			if 'file' in request.FILES:
				profile.file=request.FILES['file']
			profile.save()
			return redirect('home:home')
	else:
		form=AreaKeyForm()
	rowda=AreaKey.objects.values('rowdata')
	d=[]
	for k in rowda:
		# print(type(k))
		d+=json.loads(k['rowdata'])
		# d.append(rst)
	print(d)
	return render(request, 'areakey.html', {'form':form, 'rowda':rowda, 'd':d})

def user_profile(request):
	user=get_object_or_404(User, id=request.user.id)
	return render(request, 'user_profile.html', {'user':user})
# Create your views here
