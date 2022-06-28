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
from registro.models import Progres

#serializer
from registro.serializer import ProgresSerializer

class Registro_ProgresApiView(APIView):
    #class Progres register

    def get(self, request):
        progres = Progres.objects.all()
        serializer = ProgresSerializer(Progres, many=True)
        #json = JSONRenderer().render(serializer.data)
        return Response(serializer.data)

    def post(self, request):
        #kid register dates from client
        #json = request
        #json_bytes = io.BytesIO(json)
        #user_dic = JSONParser().parse(json_bytes)
        #serializer = UserSerializer(data = user_dic)

        #Validando datos
        serializer = ProgresSerializer(data=request.data)
        if serializer.is_valid(raise_exception = True):
            validated_data = serializer.validated_data
            progres = Progres(**validated_data)
            progres.save() #al guardar yame crea la id
            serializer_response = ProgresSerializer(progres)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status.HTTP_400_BAD_REQUEST)


class Registro_ProgresDetailApiView(APIView):
    """class to put or delete level register"""
    
    def get_object(self, id):
        """validate if object exist"""
        progres = get_object_or_404(Progres, id=id)
        return(progres)
    
    def get(self, request, id):
        """get a object by id"""
        progres = self.get_object(id)
        serializer = ProgresSerializer(progres)
        return Response(serializer.data)
    
    def put(self, request, id):
        """update a object by id"""
        progres = self.get_object(id)
        serializer = ProgresSerializer(Progres, data=request.data)
        if(serializer.is_valid()):
            progres = Progres(**serializer.validated_data)
            progres.id = id
            progres.save(update_fields=['type','stage'])
            progres = Progres.objects.get(id=id)
            serializer_response = ProgresSerializer(progres)
            return Response(serializer_response.data)#creo que es serialize_response
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def patch(self, request, id):
        """update a object by id"""
        progres = self.get_object(id)
        serializer = ProgresSerializer(progres, data=request.data, partial=True)
        if(serializer.is_valid()):
            serializer.save()
            return Response(serializer.data)#creo que es serialize_response
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    def delete(self,request,id):
        """delete a object by id"""
        progres = self.get_object(id)
        progres.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)