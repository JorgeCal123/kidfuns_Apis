#System

from django.shortcuts import get_object_or_404
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

from registro.models import Kid


#serializer
from registro.serializer import KidSerializer

class Registro_KidApiView(APIView):
    #class kid register

    def get(self, request):
        kid = Kid.objects.all()
        serializer = KidSerializer(kid, many=True)
        #json = JSONRenderer().render(serializer.data)
        return Response(serializer.data)

    def post(self, request):
        #kid register dates from client
        #json = request
        #json_bytes = io.BytesIO(json)
        #user_dic = JSONParser().parse(json_bytes)
        #serializer = UserSerializer(data = user_dic)

        #Validando datos
        
        serializer = KidSerializer(data=request.data)
        if serializer.is_valid(raise_exception = True):
            validated_data = serializer.validated_data
            kid = Kid(**validated_data)
            kid.save() #al guardar yame crea la id
            serializer_response = KidSerializer(kid)
            return Response(
                serializer_response.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status.HTTP_400_BAD_REQUEST)


class Registro_KidDetailApiView(APIView):
    #class to put or delete kid register
    
    def get_object(self, id):
        #validate if object exist
        kid = get_object_or_404(Kid, id=id)
        return(kid)
    
    def get(self, request, id):
        #get a object by id
        kid = self.get_object(id)
        serializer = KidSerializer(kid)
        return Response(serializer.data)
    
    def put(self, request, id):
        #update a object by id
        kid = self.get_object(id)
        serializer = KidSerializer(kid, data=request.data)
        if(serializer.is_valid()):
            kid = Kid(**serializer.validated_data)
            kid.id = id
            kid.save(update_fields=['name','country','email'])
            kid = Kid.objects.get(id=id)
            serializer_response = KidSerializer(kid)
            return Response(serializer.data)#creo que es serialize_response
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def patch(self, request, id):
        """update a object by id"""
        kid = self.get_object(id)
        serializer = KidSerializer(kid, data=request.data, partial=True)
        if(serializer.is_valid()):
            serializer.save()
            return Response(serializer.data)#creo que es serialize_response
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self,request,id):
        """delete a object by id"""
        kid = self.get_object(id)
        kid.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)