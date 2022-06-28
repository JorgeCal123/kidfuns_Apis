#Django import
from rest_framework import serializers

#make password
from django.contrib.auth.hashers import make_password

#Models
from registro.models import User
from registro.models import Kid
from registro.models import Level
from registro.models import Progres

"""serializer class"""
class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id','country','name','email','password']
        #exclude = [password] excluye password
        #validate_password = make_password
        
class KidSerializer(serializers.ModelSerializer):
    class Meta:
        model = Kid
        #fields = ['name','age','avatar']
        fields ='__all__' #todos los campos

class LevelSerializer(serializers.ModelSerializer):
    class Meta:
        model= Level
        fields = ['id','type','stage','id_kid']

class ProgresSerializer(serializers.ModelSerializer):
    class Meta:
        model:Progres
        fiels = ['id','games','date','score','correct','fail','id_level']

#class UserListSerializer(serializers.ModelSerializer):
 #   class Meta:
  #      model = User
   #     fields = '__all__'
