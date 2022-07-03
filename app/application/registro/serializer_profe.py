from rest_framework import serializers

from django.contrib.auth.hashers import make_password

#Models
from registro.models import User
from registro.models import Kid
from registro.models import Level
from registro.models import Progres

from registro.serializer import KidSerializer,ProgresSerializer
    
"""serializer class"""
class ProfeSerializer(serializers.ModelSerializer):
    Progres = ProgresSerializer()
    class Meta:
        model = User
        fields = ['id','country','name','email','password']
        #exclude = [password] excluye password
        #validate_password = make_password
        