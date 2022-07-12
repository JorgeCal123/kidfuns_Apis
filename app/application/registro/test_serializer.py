#System
import io

#Django
from rest_framework.renderers import JSONRenderer
from rest_framework.parsers import JSONParser
from django.db.models import Prefetch

#Others
from tabulate import tabulate 

#Models 
from registro.models import User
from registro.models import Kid
from registro.models import Level
from registro.models import Progress

#serializer
from registro.serializer import KidSerializer

#serializacion
def test_serializer():
    user = Kid.objects.get(id = 'f6b98a943f1143ef95ac47482f1271ff')
    serializer = KidSerializer(user)
    json = JSONRenderer().render(serializer.data)

    #imprimir datos
    data = [[user,serializer,serializer.data,json]]
    print(tabulate(data, headers=["modelo","serializer","serializer.Data","Json"]))

#Deserealizacion
def test_desereali():
    json = '{"name":"luifer","age":"3"}'
    json_bytes = io.BytesIO(json)
    user_dic = JSONParser().parse(json_bytes)
    serializer = KidSerializer(data = user_dic)

    #Validando datos
    is_valid = serializer.is_valid()
    errors = serializer.errors
    validated_data = serializer.validated_data

    kid = Kid(**validated_data)
    kid.save() #al guardar yame crea la id
    
    #imprimir datos
    data1 = [[json,user_dic,serializer]]
    data2 = [[is_valid,errors,validated_data,kid]]
    print(tabulate(data1, headers=["Json","Dict","Serializer"]))
    print("\n")
    print(tabulate(data2, headers=["is_valid","errors","validated"]))
    