from django.contrib.auth.models import User, Group
from rest_framework import viewsets
from rest_framework import permissions
from .serializers import ObraSerializer
from livros.models import Obra

class ObraViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = Obra.objects.all()
    serializer_class = ObraSerializer
    #permission_classes = [permissions.IsAuthenticated]