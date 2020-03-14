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
	data.reverse()
	for i in data:
		b=[]
		file_id=int(i.split('|')[0])
		row_index=int(i.split('|')[1])
		rdata=AreaKey.objects.get(pk=file_id)
		rodata=json.loads(rdata.rowdata)
		del rodata[row_index]
		for index, u in enumerate(rodata):
			row_ind={'row':index}
			u.update(row_ind)
			b+=[u]
		strdata=json.dumps(b)
		AreaKey.objects.filter(pk=file_id).update(rowdata=strdata)
	return HttpResponse("Success!")

@csrf_exempt
def csv_export(request):
	selet_row=[]
	csv_data=request.POST.getlist('csv_file[]')
	print(csv_data)
	for data in csv_data:
		# print(data)
		ids=int(data.split('|')[0])
		csv_data=AreaKey.objects.filter(pk=ids).values('rowdata')
		for x in csv_data:
			fid=json.loads(x['rowdata'])

	return HttpResponse('csv_file')
# Create your views here
