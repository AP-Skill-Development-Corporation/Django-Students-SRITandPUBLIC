from django.urls import path
from FormApp import views

urlpatterns = [
	path('demo/',views.demo,name='demo'),
	path('register/',views.register,name='register'),
	path('details/',views.details,name='details'),






]