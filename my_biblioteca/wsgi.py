
import os
from django.core.wsgi import get_wsgi_application
from dj_static import Clingort os


os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'my_biblioteca.settings')
application = Cling(get_wsgi_application())
