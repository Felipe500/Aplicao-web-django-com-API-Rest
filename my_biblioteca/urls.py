from django.contrib import admin
from django.urls import path, include

from rest_framework import routers
from django.conf import settings
from django.conf.urls.static import static
from rest_framework.authtoken import views

from livros.api.viewsets import ObraViewSet

router = routers.DefaultRouter()
router.register(r'obras', ObraViewSet, basename='PontoTuristico')

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include(router.urls)),
     path('', include('livros.urls')),
]
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)