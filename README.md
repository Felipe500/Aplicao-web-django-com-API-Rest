# Aplicao-web-django-com-API-Rest 


Desenvolvendo uma aplicação web com um back end que possa se comunicar com outras aplicações, atravéis de uma API desenvolvida com django rest framework


#--------------------------------
# Arquivos estáticos 


Configure your static assets in settings.py:

STATIC_ROOT = 'staticfiles'
STATIC_URL = '/static/'

Then, update your wsgi.py file to use dj-static:

from django.core.wsgi import get_wsgi_application
from dj_static import Cling

application = Cling(get_wsgi_application())

