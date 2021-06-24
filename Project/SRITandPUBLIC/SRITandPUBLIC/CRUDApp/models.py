from django.db import models

# Create your models here.
class Student(models.Model):
	Sname = models.CharField(max_length=30)
	Sroll = models.CharField(max_length=30)
	Sbranch = models.CharField(max_length=30)
	Semail = models.EmailField(max_length=50)
	Smobile = models.IntegerField()


	