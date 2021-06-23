from django.shortcuts import render,redirect
from django.http import HttpResponse
from FormApp.models import Register
from FormApp.forms import Reg

# Create your views here.

def demo(request):
	return HttpResponse("im from FormApp")

def register(request):
	if request.method=="POST":
		formdata=Reg(request.POST)
		if formdata.is_valid():
			formdata.save()
			return redirect('/form/register')
	formdata= Reg()
	return render(request,'FormApp/register.html',{'data':formdata})

def details(request):
	data=Register.objects.all()
	return render(request,'FormApp/details.html',{'data':data})