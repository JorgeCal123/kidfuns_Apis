from django.shortcuts import get_object_or_404
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

from registro.models import Progress
from registro.serializer import ProgressSerializer


class Registro_ProgressApiView(APIView):
    def get(self, request):
        progress = Progress.objects.all()
        serializer = ProgressSerializer(progress, many=True)
        #json = JSONRenderer().render(serializer.data)
        return Response(serializer.data)

    def post(self, request):
        #kid register dates from client
        #json = request
        #json_bytes = io.BytesIO(json)
        #user_dic = JSONParser().parse(json_bytes)
        #serializer = UserSerializer(data = user_dic)

        #Validando datos
        serializer = ProgressSerializer(data=request.data)
        if serializer.is_valid(raise_exception = True):
            validated_data = serializer.validated_data
            progress = Progress(**validated_data)
            progress.save() #al guardar yame crea la id
            serializer_response = ProgressSerializer(progress)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status.HTTP_400_BAD_REQUEST)


class Registro_ProgressDetailApiView(APIView):
    """class to put or delete level register"""
    def get_object(self, id):
        """validate if object exist"""
        progress = get_object_or_404(Progress, id=id)
        return(progress)
    
    def get(self, request, id):
        """get a object by id"""
        progress = self.get_object(id)
        serializer = ProgressSerializer(progress)
        return Response(serializer.data)
    
    def put(self, request, id):
        """update a object by id"""
        progress = self.get_object(id)
        serializer = ProgressSerializer(Progress, data=request.data)
        if(serializer.is_valid()):
            progress = Progress(**serializer.validated_data)
            progress.id = id
            progress.save(update_fields=['type','stage'])
            progress = Progress.objects.get(id=id)
            serializer_response = ProgressSerializer(progress)
            return Response(serializer_response.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def patch(self, request, id):
        """update a object by id"""
        progress = self.get_object(id)
        serializer = ProgressSerializer(
            progress, data=request.data, partial=True)
        if(serializer.is_valid()):
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    def delete(self,request,id):
        """delete a object by id"""
        progress = self.get_object(id)
        progress.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)