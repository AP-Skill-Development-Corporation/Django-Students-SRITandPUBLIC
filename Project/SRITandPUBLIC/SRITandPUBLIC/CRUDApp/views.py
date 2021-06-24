from django.shortcuts import render,redirect
from django.http import HttpResponse
from CRUDApp.models import Student

# Create your views here.


def Demo(request):
	return HttpResponse("Welcome CRUDApp")


def Register(request):
	if request.method == "POST":
		sname = request.POST.get('sname')
		sroll = request.POST.get('sroll')
		sbranch = request.POST.get('sbranch')
		semail = request.POST.get('semail')
		smobile = request.POST.get('smobile')
		#print(Sname,Sroll)
		Student.objects.create(Sname=sname,Sroll=sroll,Sbranch=sbranch,Semail=semail,Smobile=smobile)
		return HttpResponse("Record inserted into table")
	return render(request,'crudapp/register.html')


def Details(request):
	data = Student.objects.all()
	return render(request,'crudapp/show.html',{'data':data})



def Update(request,id):
	rec = Student.objects.get(id=id)
	if request.method == 'POST':
		rec.Sname = request.POST.get('sname')
		rec.Sroll = request.POST.get('sroll')
		rec.Sbranch = request.POST.get('sbranch')
		rec.Semail = request.POST.get('semail')
		rec.Smobile = request.POST.get('smobile')
		rec.save()
		#return HttpResponse("updated successfully")
		return redirect('Details')
	return render(request,'crudapp/update.html',{'rec':rec})


def Delete(request,id):
	del_rec = Student.objects.get(id=id)
	if request.method == 'POST':
		del_rec.delete()
		#return HttpResponse("Deleted successfully")
		return redirect('Details')
	return render(request,'crudapp/delete.html',{'del_rec':del_rec})