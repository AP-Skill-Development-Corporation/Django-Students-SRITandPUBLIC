from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def Sample(request):
	return HttpResponse("Welcome to Deb Development")


def Sample1(request):
	return HttpResponse("<h1><center> Welcome to django page </center></h1>")

def Sample2(request):
	return HttpResponse("<h1>Welcome Archana....</h1>")


def Mulple(request):
	return HttpResponse("Welcome to web Development<br><h1><center> Welcome to django page </center></h1><br><h1> Welcome Archana.... </h1>")


def StringValue(request,name):
	return HttpResponse("<h1>Welcome %s</h1>"%name)


def IntValue(request,num):
	return HttpResponse("<h1>Age is %d....</h1>"%num)