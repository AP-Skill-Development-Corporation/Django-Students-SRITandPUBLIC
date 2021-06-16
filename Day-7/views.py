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

def table(request):
	return render(request,'myApp/table.html')

def inline(request):
	return render(request,'myApp/inline.html')

def internal(request):
	return render(request,'myApp/internal.html')

def task2(request,num):
	data=[]
	for i in range(1,11):
		td=str(num)+"*"+str(i)+'='+str(num*i)
		data.append(td)
	return render(request,'myApp/task2.html',{'info':data})

def external(request):
	return render(request,'myApp/external.html')

def boot(request):
	return render(request,'myApp/boot.html')
