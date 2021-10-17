# Aplicao-web-django-com-API-Rest 


Desenvolvendo uma aplicação web com um back end que possa se comunicar com outras aplicações, atravéis de uma API desenvolvida com django rest framework


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

https://github.com/Felipe500/Aplicao-web-django-com-API-Rest/blob/bf5620458c22917a0de7ed4206dc0bd353e4011c/Captura%20de%20tela_2021-10-17_17-37-08.png
