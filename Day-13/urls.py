"""myProject URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path,include
from myApp import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('hi/',views.hi,name='hi'),
    path('hello/<int:num>',views.hello,name='hello'),
    path('task/<str:name>/<int:id>/',views.task),
    path('basic/',views.basic,name='basic'),
    path('dyn/<str:name>/<int:id>/',views.dyn,name='dyn'),
    path('table/',views.table,name='table'),
    path('inline/',views.inline,name='inline'),
    path('internal/',views.internal,name="internal"),
    path('task2/<int:num>/',views.task2,name='task2'),
    path('external/',views.external,name='external'),
    path('boot/',views.boot,name='boot'),
    path('task3/',views.task3,name='task3'),
    path('offline/',views.offline,name="offline"),
    path('get/',views.get,name='get'),
    path('crud/',include('CrudApp.urls')),
    path('form/',include('FormApp.urls')),

]
