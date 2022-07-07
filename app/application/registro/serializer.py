#Django import
from rest_framework import serializers

from registro.models import User
from registro.models import Kid
from registro.models import Level
from registro.models import Progres

"""serializer class"""
class UserSerializer(serializers.ModelSerializer):
    """This class permit to serialize fields of the User model"""
    class Meta:
        model = User
        fields = ['id','country','name','email']
        
        
class KidSerializer(serializers.ModelSerializer):
    """This class permit to serialize fields of the Kid model"""
    class Meta:
        model = Kid
        #fields = ['name','age','avatar']
        fields ='__all__'

class LevelSerializer(serializers.ModelSerializer):
    """This class permit to serialize fields of the Level model"""
    class Meta:
        model = Level
        #fields = ['id','type','stage','id_kid']
        fields ='__all__'

class ProgresSerializer(serializers.ModelSerializer):
    """This class permit to serialize fields of the Progres model"""
    class Meta:
        model = Progres
        #fiels = ['id','games','date','score','correct','fail','id_level']
        fields ='__all__'
