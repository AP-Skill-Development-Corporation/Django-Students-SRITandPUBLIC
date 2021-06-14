from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
def hi(request):
	return HttpResponse("hai guys welcome to django session")

def hello(request,num):
	return HttpResponse('my roll number is:{}'.format(num))

def task(request,name,id):
	return HttpResponse("my name is {} and My roll number is {}".format(name,id))

def basic(request):
	return render(request,'myApp/basic.html')

def dyn(request,name,id):
	return render(request,'myApp/dyn.html',{'n':name,'i':id})