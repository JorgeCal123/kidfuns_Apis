#System

import io

from django.shortcuts import render, get_object_or_404
from django.http import Http404
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

#Django
from rest_framework.renderers import JSONRenderer
from rest_framework.parsers import JSONParser
from django.db.models import Prefetch

#Models 
from registro.models import Kid


#serializer
from registro.serializer import UserSerializer, KidSerializer, LevelSerializer, ProgresSerializer

class Kid_profesorApiView(APIView):
    #class kid register
    
    def get(self, request):
        kid = Kid.objects.values('name','avatar','kid_p_id__score','kid_id__stage').filter(kid_id__stage__lte=1, kid_p_id__type__lte=1)
        serializer = KidSerializer(kid, many=True)
        #json = JSONRenderer().render(serializer.data)
        return Response(serializer.data)

    def get_object(self, id):
        #validate if object exist
        kid = get_object_or_404(Kid, id=id)
        return(kid)
    
    def get(self, request, id):
        #get a object by id
        kid = self.get_object(id)
        serializer = KidSerializer(kid)
        return Response(serializer.data)
    