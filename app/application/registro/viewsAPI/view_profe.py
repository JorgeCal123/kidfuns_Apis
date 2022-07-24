#from urllib import response
from rest_framework.views import APIView
#from rest_framework import serializers
#from registro import models

#from registro.models import Kid, Progress
#from registro.serializer import KidSerializer, ProfeSerializer


#class KidProgress(APIView):
#    """
#    A simple ViewSet for viewing and editing kid.
#    """
    #def get_context_data(self, request, **kwargs):
    #    context = super().get_context_data(**kwargs)
    #    context['kid_data'] = models.Kid.objects.all()
    #    
    #    context[''] = models.Kid.objects.all()
    #    #context['progress_data'] = models.Progress.objects.all()
    #    context['progress_data'] = models.Progress.objects.filter(score__gte = 2).all()
    #    if context['progress_data']:
    #        context['score']
    #    return 0