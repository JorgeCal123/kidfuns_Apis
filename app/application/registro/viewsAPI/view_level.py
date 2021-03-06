from django.shortcuts import get_object_or_404
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

from registro.models import Level


from registro.serializer import LevelSerializer

class Registro_LevelApiView(APIView):
    """class level register has the get and post method"""

    def get(self, request):
        """function get obtein all the object of level"""
        level = Level.objects.all()
        serializer = LevelSerializer(level, many=True)
        #json = JSONRenderer().render(serializer.data)
        return Response(serializer.data)

    def post(self, request):
        """function post all the dates into the database"""
        #kid register dates from client
        #json = request
        #json_bytes = io.BytesIO(json)
        #user_dic = JSONParser().parse(json_bytes)
        #serializer = UserSerializer(data = user_dic)

        #Validando datos
        serializer = LevelSerializer(data=request.data)
        if serializer.is_valid(raise_exception = True):
            validated_data = serializer.validated_data
            level = Level(**validated_data)
            level.save() #al guardar yame crea la id
            serializer_response = LevelSerializer(level)
            return Response(serializer_response.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status.HTTP_400_BAD_REQUEST)


class Registro_LevelDetailApiView(APIView):
    """class contains to put or delete level register"""
    
    def get_object(self, id):
        """validate if object exist"""
        level = get_object_or_404(Level, id=id)
        return(level)
    
    def get(self, request, id):
        """get a object by id"""
        level = self.get_object(id)
        serializer = LevelSerializer(level)
        return Response(serializer.data)
    
    def put(self, request, id):
        """update a object by id"""
        level = self.get_object(id)
        serializer = LevelSerializer(Level, data=request.data)
        if(serializer.is_valid()):
            level = Level(**serializer.validated_data)
            level.id = id
            level.save(update_fields=['type','stage'])
            level = Level.objects.get(id=id)
            serializer_response = LevelSerializer(level)
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def patch(self, request, id):
        """update a object by id"""
        level = self.get_object(id)
        serializer = LevelSerializer(level, data=request.data, partial=True)
        if(serializer.is_valid()):
            serializer.save()
            return Response(serializer.data)#creo que es serialize_response
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self,request,id):
        """delete a object by id"""
        level = self.get_object(id)
        level.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)