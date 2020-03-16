from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import logout, authenticate
from django.contrib.auth.decorators import login_required
from django.views.decorators.csrf import csrf_exempt
from .models import *
import csv
from django.contrib import messages
from django.http import HttpResponseRedirect, HttpResponse
from django.urls import reverse
from .forms import *
import json
import datetime

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
	plc_odr=Order.objects.filter(user=request.user.id)
	return render(request, 'areakey.html', {'form':form, 'd':d, 'plc_odr':plc_odr})

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
	if request.method=='POST':
		csv_data=request.POST.getlist('csv_file[]')
		response = HttpResponse(content_type='text/csv')
		response['Content-Disposition'] = 'attachment; filename="areakey-template.csv"'
		fieldnames = ['cust_name', 'order_num', 'date', 'post']
		writer = csv.DictWriter(response, fieldnames=fieldnames)
		writer.writeheader()
		d= csv_data[0].split(',')
		for data in d:
			ids=int(data.split('|')[0])
			rid=int(data.split('|')[1])
			csv_data=AreaKey.objects.get(pk=ids)
			fid=json.loads(csv_data.rowdata)
			seled_row=fid[rid]
			print(seled_row)
			writer.writerow({'cust_name':seled_row['cust_name'], 'order_num':seled_row['order_num'], 'date':seled_row['date'], 'post':seled_row['post']})
		return response

		return HttpResponse('csv_file')

@csrf_exempt
def place_order(request):
	data=request.POST.getlist('order[]')
	print(type(data))
	data.reverse()
	for i in data:
		b=[]
		file_id=int(i.split('|')[0])
		row_index=int(i.split('|')[1])
		rdata=AreaKey.objects.get(pk=file_id)
		rodata=json.loads(rdata.rowdata)
		sel_r=rodata[row_index]
		date=rodata[row_index]['date']
		sd=datetime.datetime.strptime(date,"%d/%m/%Y").strftime("%Y-%m-%d")
		Order.objects.create(user=request.user, order_no=sel_r['order_num'], customer_order=sel_r['cust_name'], date=sd, postcode=sel_r['post'])
		del rodata[row_index]
		for index, u in enumerate(rodata):
			row_ind={'row':index}
			u.update(row_ind)
			b+=[u]
		strdata=json.dumps(b)
		AreaKey.objects.filter(pk=file_id).update(rowdata=strdata)
	return HttpResponse("Success!")

# Create your views here
