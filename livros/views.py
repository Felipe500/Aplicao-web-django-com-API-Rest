from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.forms import inlineformset_factory
from django.contrib.auth.forms import UserCreationForm
from .models import *

from .filters import ObraFilter

from django.contrib.auth import authenticate, login, logout

from django.contrib import messages

from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import Group
from .forms import ObraForm, CreateUserForm, LeitorForm
from .decorators import unauthenticated_user
import csv
from datetime import datetime


#verificar se usuário está logado	
@unauthenticated_user
def register_page(request):

	form = CreateUserForm()
	if request.method == 'POST':
		form = CreateUserForm(request.POST)
		if form.is_valid():
			user = form.save()
			username = form.cleaned_data.get('username')


			messages.success(request, 'Registrado a conta ' + username)

			return redirect('logar')
		

	context = {'form':form}
	return render(request, 'register.html', context)


#verificar se usuário está logado	
@unauthenticated_user
def login_page(request):
	
	if request.method == 'POST':
		username = request.POST.get('username')
		password =request.POST.get('password')

		user = authenticate(request, username=username, password=password)

		if user is not None:
			login(request, user)
			return redirect('home')
		else:
			messages.info(request, 'Usuário ou senha estão errados')

	context = {}		
	return render(request,'login.html')

def sair_conta(request):
	logout(request)
	return redirect('logar')



@login_required(login_url='logar')
def inicio(request):
	
	obras_set = Obra.objects.all()
	total_obras = obras_set.count()

	

	context = { 'obras' :obras_set,
	'total_obras':total_obras}
	
	return render(request, 'pagina_usuario.html',context)


@login_required(login_url='logar')
def export_obras(request):
	#a =export_csv(request)
	obras_set = Obra.objects.all()
	total_obras = obras_set.count()
	

	if 'filtrar' in request.POST:
		username = request.GET.get('end_data')
		password =request.POST.get('password')
		print(username)

		
		myFilter = ObraFilter(request.GET, queryset=obras_set)
		obras = myFilter.qs


		x = exportar_csv(request,obras)
		return x
	else:
		myFilter = ObraFilter(request.GET, queryset=obras_set)
		obras = myFilter.qs
		obra = myFilter.qs.count()


	context = { 'obras' :obras,
	'total_obras':total_obras,'myFilter':myFilter,'pesquisa_resul':obra}
	
	return render(request, 'export_obras.html',context)


@login_required(login_url='logar')
def exportar_csv(request,obras):

    d = datetime.now().strftime('%d-%m-%Y--%H-%M')
    obras_set = Obra.objects.all()
	


    response = HttpResponse(
        content_type='text/csv',
        headers={'Content-Disposition': 'attachment; filename="obras--'+d+'.csv'},
    )

    writer = csv.writer(response)
    writer.writerow(['ID','Titulo', 'Descricao', 'Editora', 'date_created','autores'])
    
    #list_obras = Obra.objects.all()
    for obra in obras:
    	dd = obra.date_created.strftime('%d-%m-%Y--%H:%M')
    	writer.writerow([obra.id,obra.titulo,obra.descricao,obra.editora,dd,obra.autores])

    return response


@login_required(login_url='login')
def perfil_usuario(request):
	

	leitor = request.user.leitor
	form = LeitorForm(instance=leitor)

	if request.method == 'POST':
		form = LeitorForm(request.POST, request.FILES,instance=leitor)
		print("form config")
		if form.is_valid():
			print("salvo")
			form.save()


	context = {'form':form}

	
	return render(request, 'perfil_user.html', context)


@login_required(login_url='logar')
def list_obras(request):
	list_obras = Obra.objects.all()
	return render(request, 'list_obras.html', {'list_obras':list_obras})



@login_required(login_url='logar')
def criar_obra(request):

	#id_obra = Obra.objects.get(id=id)
	form = ObraForm()

	if request.method == 'POST':
		form = ObraForm(request.POST,request.FILES)
		if form.is_valid():
			form.save()
			return redirect('/')

	context = {'form':form}
	return render(request, 'criar_obra.html', context)







@login_required(login_url='logar')
def atualizar_obra(request, id):

	id_obra = Obra.objects.get(id=id)
	form = ObraForm(instance=id_obra)

	if request.method == 'POST':
		form = ObraForm(request.POST,request.FILES, instance=id_obra)
		if form.is_valid():
			form.save()
			return redirect('/')

	context = {'form':form,'dados':id_obra}
	return render(request, 'form_atualizar.html', context)


@login_required(login_url='logar')
def remover_obra(request, id):
	id_obra = Obra.objects.get(id=id)
	if request.method == "POST":
		id_obra.delete()
		return redirect('/')

	context = {'item':id_obra}
	return render(request, 'delete.html', context)

