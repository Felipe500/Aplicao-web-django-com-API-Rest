from django.forms import ModelForm, Textarea
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django import forms
from .models import *


class ObraForm(ModelForm):
	class Meta:
		model = Obra
		fields = '__all__'
		

class CreateUserForm(UserCreationForm):
	class Meta:
		model = User
		fields = ['username', 'email', 'password1', 'password2']


class LeitorForm(ModelForm):
	

	class Meta:
		model = Leitor
		fields = '__all__'
		exclude = ['user']

