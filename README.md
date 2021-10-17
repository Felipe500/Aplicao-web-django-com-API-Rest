# Aplicao-web-django-com-API-Rest 


Desenvolvendo uma aplicação web com um back end que possa se comunicar com outras aplicações, atravéis de uma API desenvolvida com django rest framework. 


#--------------------------------
# Arquivos estáticos 

- pip install dj_static
Configure your static assets in settings.py:

STATIC_ROOT = 'staticfiles'
STATIC_URL = '/static/'

Then, update your wsgi.py file to use dj-static:

from django.core.wsgi import get_wsgi_application
from dj_static import Cling

application = Cling(get_wsgi_application())

# TELA DE LOGIN DO SISTEMA

![alt text](https://github.com/Felipe500/Aplicao-web-django-com-API-Rest/blob/main/Captura%20de%20tela_2021-10-17_17-37-08.png?raw=true)

-----------------------------------------------------------------------------------------------------------------------------------------
# TELA DE ROTA INICIAL PÓS LOGIN

![alt text](https://github.com/Felipe500/Aplicao-web-django-com-API-Rest/blob/main/Captura%20de%20tela_2021-10-17_18-00-54.png?raw=true)

-----------------------------------------------------------------------------------------------------------------------------------------
# CONFIGURAÇÃO DO PERFIL DO USUÁRIO

![alt text](https://github.com/Felipe500/Aplicao-web-django-com-API-Rest/blob/main/Captura%20de%20tela_2021-10-17_18-03-01.png?raw=true)

----------------------------------------------------------------------------------------------------------------------------------------
# TELA DE ATUALIZAÇÃO E INSERÇÃO DE OBRAS NO SISTEMA

![alt text](https://github.com/Felipe500/Aplicao-web-django-com-API-Rest/blob/main/Captura%20de%20tela_2021-10-17_18-03-59.png?raw=true)

-----------------------------------------------------------------------------------------------------------------------------------------
# REALIZAR UMA FILTRAGEM E EXPORTAR DADOS DAS OBRAS EM ARQUIVO .CSV  

![alt text](https://github.com/Felipe500/Aplicao-web-django-com-API-Rest/blob/main/Captura%20de%20tela_2021-10-17_18-01-26.png?raw=true)

----------------------------------------------------------------------------------------------------------------------------------------
# LISTAGEM DE TODAS OBRAS

![alt text](https://github.com/Felipe500/Aplicao-web-django-com-API-Rest/blob/main/Captura%20de%20tela_2021-10-17_18-01-10.png?raw=true)

----------------------------------------------------------------------------------------------------------------------------------------
# API PARA CONSUMO DE DADOS

![alt text](https://github.com/Felipe500/Aplicao-web-django-com-API-Rest/blob/main/Captura%20de%20tela_2021-10-17_17-47-03.png?raw=true)
