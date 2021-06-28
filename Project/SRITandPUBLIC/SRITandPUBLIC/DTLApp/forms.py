from django import forms

from django.forms import ModelForm

from django.contrib.auth.models import User

from django.contrib.auth.forms import UserCreationForm 



class UserReg(UserCreationForm):
	password1 = forms.CharField(widget=forms.PasswordInput(
		attrs={'class':'form-control','placeholder':'Enter Password'}))
	password2 = forms.CharField(widget=forms.PasswordInput(
		attrs={'class':'form-control','placeholder':'Enter Confirm Password'}))

	class Meta:
		model = User
		#fields = '__all__'
		fields = ['username','email']

		widgets = {
			'username' : forms.TextInput(
				attrs={'class':'form-control','placeholder':'Enter Username'}),
			'email' : forms.TextInput(
				attrs={'class':'form-control','placeholder':'Enter EmailId'})
		}



class UpdatePro(ModelForm):

	class Meta:
		model = User
		fields = ['username','email','first_name','last_name']

		widgets = {
			'username' : forms.TextInput(
				attrs={'class':'form-control','placeholder':'Update Username'}),
			'email' : forms.TextInput(
				attrs={'class':'form-control','placeholder':'Update EmailId'}),
			'first_name' : forms.TextInput(
				attrs={'class':'form-control','placeholder':'Update FirstName'}),
			'last_name' : forms.TextInput(
				attrs={'class':'form-control','placeholder':'Update lastName'})
			

		}

