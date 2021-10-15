from django.contrib import admin

# Register your models here.
from .models import Leitor, Autor, Obra, Editora

admin.site.register(Leitor)
admin.site.register(Autor)
admin.site.register(Editora)
admin.site.register(Obra)