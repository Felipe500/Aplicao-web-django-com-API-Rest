import django_filters
from django_filters import DateFilter, CharFilter

from .models import *
from django import forms

class Date_input(forms.DateInput):
	input_type : 'date'


class ObraFilter(django_filters.FilterSet):
	start_date = DateFilter( field_name="date_created", lookup_expr='gte', label=('Data Inicial'))
	#start_date.render('data1', '01/01/1999')
	end_date = DateFilter(field_name="date_created", lookup_expr='lte',label=('Data Final'))
	descricao = CharFilter(field_name='descricao', lookup_expr='icontains',label=('Descrição'))
	titulo = CharFilter(field_name='titulo', lookup_expr='icontains',label=('Titulo'))
	class Meta:
		model = Obra
		fields = '__all__'
		exclude = ['autores', 'date_created','img']

