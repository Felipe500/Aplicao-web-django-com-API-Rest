
from django.urls import path, include

from .views import *

urlpatterns = [
    path('', inicio, name = 'home'),

    path('registrar/', register_page, name = 'registrar'),
    path('login/', login_page , name='logar'),
    path('sair/', sair_conta , name='logout'),

    path('obras/', list_obras, name = 'list_obras'),
    path('criar_obra/', criar_obra, name="criar_obra"),
    path('obras/<str:id>/', atualizar_obra, name="atualizar_obra"),
    path('obras-del/<str:id>/', remover_obra, name="remover_obra"),
    path('file-obras/', export_obras, name = 'export_obras'),
    path('exportar_csv/', exportar_csv, name = 'export_csv'),
    path('perfil_user/', perfil_usuario, name="perfil_usuario")

]