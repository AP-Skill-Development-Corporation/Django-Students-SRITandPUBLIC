from django.contrib import admin
from django.urls import path,include
from DTLApp import views

from django.contrib.auth import views as v

urlpatterns = [
	path('demo/',views.Demo,name='Demo'),
	path('home/',views.home,name='home'),
	path('about/',views.about,name='about'),
	path('contact/',views.contact,name='contact'),
	path('dashboard/',views.dashboard,name='dashboard'),

	path('register/',views.register,name='register'),




	path('login/',v.LoginView.as_view(template_name='dtlapp/login.html'),name='login'),
	path('logout/',v.LogoutView.as_view(template_name='dtlapp/logout.html'),name='logout'),


	path('profile/',views.profile,name='profile'),
	path('update/',views.Update_user,name='Update_user')


]