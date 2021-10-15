from django.db import models
from django.contrib.auth.models import User
from ckeditor.fields import RichTextField


class Leitor(models.Model):
	user = models.OneToOneField(User, null=True, blank=True, on_delete=models.CASCADE)
	name = models.CharField(max_length=200, null=True)
	phone = models.CharField(max_length=200, null=True, blank=True)
	email = models.CharField(max_length=200, null=True, blank=True)
	biografia =  RichTextField(null=True,blank=True )
	img_perfil = models.ImageField( default="profile.png", null=True, blank=True)
	date_created = models.DateTimeField(auto_now_add=True, null=True)

	def __str__(self):
		return self.name


class Autor(models.Model):
	nome = models.CharField(max_length=200, null=True)

	def __str__(self):
		return self.nome


class Editora(models.Model):
	nome = models.CharField(max_length=200, null=True)

	def __str__(self):
		return self.nome


class Obra(models.Model):
	titulo = models.CharField(max_length=200, null=True)	
	descricao = models.TextField(max_length=200, null=True, blank=True)
	editora = models.ForeignKey(Editora, null=True, on_delete= models.SET_NULL)
	img = models.ImageField( default="image_not_found.png", null=True, blank=True)
	date_created = models.DateTimeField(auto_now_add=True, null=True)
	autores = models.ManyToManyField(Autor)

	def __str__(self):
		return self.titulo