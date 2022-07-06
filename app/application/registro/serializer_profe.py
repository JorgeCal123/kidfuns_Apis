#Django import
from rest_framework import serializers

#make password
from django.contrib.auth.hashers import make_password

#Models

from registro.models import Progres
from registro.models import Kid
from registro.models import Level

from registro.serializer import KidSerializer
from registro.serializer import LevelSerializer

