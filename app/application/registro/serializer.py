from rest_framework import serializers

from projectkind.utils import DynamicFieldsModelSerializer
from registro.models import User, Kid, Level, Progress


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id','country','name','email']
                
class KidSerializer(DynamicFieldsModelSerializer):
    score = serializers.DecimalField(
        source='progress.score', max_digits=2, decimal_places=1,
        read_only=True)
    fail = serializers.IntegerField(source='progress.fail', read_only=True)
    correct = serializers.IntegerField(
        source='progress.correct', read_only=True)
    class Meta:
        model = Kid
        fields = ['name','age','avatar','score','fail','correct']


class LevelSerializer(serializers.ModelSerializer):
    class Meta:
        model = Level
        fields = '__all__'


class ProgressSerializer(DynamicFieldsModelSerializer):
    class Meta:
        model = Progress
        fields = '__all__'
