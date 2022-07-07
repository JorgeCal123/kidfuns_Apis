from rest_framework import viewsets

from registro.models import Kid
from registro.serializer import KidSerializer


class KidProgress(viewsets.ModelViewSet):
    """
    A simple ViewSet for viewing and editing kid.
    """
    queryset = Kid.objects.all()
    serializer_class = KidSerializer
