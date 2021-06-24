from django.contrib import admin
from django.urls import path
from CRUDApp import views

urlpatterns = [
	path('demo/',views.Demo,name='Demo'),
	path('register/',views.Register,name='Register'),
	path('dtails/',views.Details,name='Details'),
	path('update/<int:id>/',views.Update,name='Update'),
	path('delete/<int:id>/',views.Delete,name='Delete')
]