from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import logout, authenticate
from django.contrib.auth.decorators import login_required
from django.views.decorators.csrf import csrf_exempt
from .models import *
import csv, io
from django.contrib import messages
from django.http import HttpResponseRedirect, HttpResponse
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

@login_required
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
			return redirect('home:areakey')
	else:
		form=AreaKeyForm()
	rowda=AreaKey.objects.filter(user=request.user.id).values('rowdata')
	d=[]
	for k in rowda:
		d+=json.loads(k['rowdata'])
	return render(request, 'areakey.html', {'form':form, 'd':d})

def user_profile(request):
	user=get_object_or_404(User, id=request.user.id)
	return render(request, 'user_profile.html', {'user':user})

@csrf_exempt
def table_data(request):
	data=request.POST.getlist('id[]')
	for i in data:
		d=int(i.split('|')[0])
		j=int(i.split('|')[1])
		# print(d)
	print(type(d))
	rdata=AreaKey.objects.filter(pk=d).values('rowdata')
	# print(rdata)
	i=[]
	rodata=json.loads(str(rdata))
	print(rodata)
	return HttpResponse("Success!")
# Create your views here
