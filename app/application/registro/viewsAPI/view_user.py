from django.shortcuts import get_object_or_404
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from django.contrib.auth.hashers import make_password

from registro.models import User
from registro.serializer import UserSerializer

class Registro_UserApiView(APIView):#ruta register
    """class registro"""
    
    def get(self, request):
        user = User.objects.all()
        serializer = UserSerializer(user, many=True)
        #json = JSONRenderer().render(serializer.data)
        return Response(serializer.data)

    def post(self, request):
        """user register dates from client"""
        #json = request
        #json_bytes = io.BytesIO(json)
        #user_dic = JSONParser().parse(json_bytes)
        #serializer = UserSerializer(data = user_dic)

        #Validando datos
        serializer = UserSerializer(data=request.data)
        if serializer.is_valid(raise_exception = True):
            validated_data = serializer.validated_data
            user = User(**validated_data)
            user.password = make_password('password') 
            user.save() #al guardar yame crea la id
            serializer_response = UserSerializer(user)
            return Response(
                serializer_response.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status.HTTP_400_BAD_REQUEST)

        
class Registro_UserDetailApiView(APIView):
    """class to put or delete register"""
    def get_object(self, id):
        """validate if object exist"""
        user = get_object_or_404(User, id=id)
        return user
    
    def get(self, request, id):
        """get a object by id"""
        user = self.get_object(id)
        serializer = UserSerializer(user)
        return Response(serializer.data)
    
    def put(self, request, id):
        """update a object by id"""
        user = self.get_object(id)
        serializer = UserSerializer(user, data=request.data)
        if(serializer.is_valid()):
            serializer.save()
            return Response(serializer.data)#creo que es serialize_response
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def patch(self, request, id):
        """update a object by id"""
        user = self.get_object(id)
        serializer = UserSerializer(user, data=request.data, partial=True)
        if(serializer.is_valid()):
            serializer.save()
            return Response(serializer.data)#creo que es serialize_response
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self,request,id):
        """delete a object by id"""
        user = self.get_object(id)
        user.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
