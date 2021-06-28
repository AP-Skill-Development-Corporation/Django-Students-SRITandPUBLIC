from django.shortcuts import render,redirect
from django.http import HttpResponse
from DTLApp.forms import UserReg,UpdatePro

# Create your views here.

def Demo(request):
	return HttpResponse("Welcome to DTLApp")

def home(request):
	return render(request,'dtlapp/home.html')


def about(request):
	return render(request,'dtlapp/about.html')

def contact(request):
	return render(request,'dtlapp/contact.html')

def dashboard(request):
	return render(request,'dtlapp/dashboard.html')

	

def register(request):
	if request.method == 'POST':
		form = UserReg(request.POST)
		if form.is_valid():
			form.save()
			#return HttpResponse("registration successfull")
			return redirect('login')
	form = UserReg()
	return render(request,'dtlapp/register.html',{'form':form})



def profile(request):
	return render(request,'dtlapp/profile.html')


def Update_user(request):
	if request.method == 'POST':
		data = UpdatePro(request.POST,instance = request.user)
		if data.is_valid():
			data.save()
			return redirect('profile')
	data = UpdatePro(instance=request.user)
	return render(request,'dtlapp/update.html',{'data':data})