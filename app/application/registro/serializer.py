from rest_framework import serializers

#from projectkind.utils import DynamicFieldsModelSerializer
from registro.models import User, Kid, Level, Progress


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id','country','name','email']
                
#class KidSerializer(serializers.ModelSerializer):
#    campos = ProgressSerializer(many=True, source='progress')
#    #fail = serializers.IntegerField(source='progress.fail', read_only=True)
#    #correct = serializers.IntegerField(
#    #    source='progress.correct', read_only=True)
#    class Meta:
#        model = Kid
#        fields = ['name', 'age','campos']
class KidSerializer(serializers.ModelSerializer):
        #fail = serializers.IntegerField(source='progress.fail', read_only=True)
        #correct = serializers.IntegerField(
        #    source='progress.correct', read_only=True)
        class Meta:
            model = Kid
            fields = '_all_'
           
class LevelSerializer(serializers.ModelSerializer):
    class Meta:
        model = Level
        fields = '__all__'


class ProgressSerializer(serializers.ModelSerializer):
    #name = serializers.CharField(
    #    source='Kid', read_only=True)
    class Meta:
        model = Progress
        fields = '_all_'

class InfoProgressSerializer(serializers.ModelSerializer):
    #name = serializers.CharField(
    #    source='Kid', read_only=True)
    class Meta:
        model = Progress
        fields = ['score','fail','correct']
        

class ProfeSerializer(serializers.ModelSerializer):
    campos = InfoProgressSerializer(many=True, source='progress')

    class Meta:
        model = Kid
        fields = ['name','age','campos']
