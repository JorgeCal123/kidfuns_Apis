from django.db import models
import uuid
# models

class User(models.Model):

    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    country = models.CharField(max_length=20, blank=False)
    name = models.CharField(max_length=50, null=False, blank=False)
    email = models.EmailField(max_length=255, unique=True, blank=False)
    password = models.CharField(max_length=255)
    
class Kid(models.Model):
 
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = models.CharField(max_length=50, blank=False, null=False, unique=True)
    age = models.IntegerField(blank=False)
    avatar = models.CharField(max_length=50)
    user = models.ForeignKey(User, related_name='user_id', null=True, on_delete=models.PROTECT, blank=False)

class Level(models.Model):

    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    type= models.IntegerField(blank=False)
    stage = models.IntegerField(blank=False)
    id_kid = models.ForeignKey(Kid, related_name='id_kid', on_delete=models.CASCADE, blank=False)

class Progres(models.Model):
    
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    games= models.IntegerField()
    date= models.DateField(auto_now=True)
    score= models.DecimalField(decimal_places=1, max_digits=1)#representacion esta en cadena
    correct= models.IntegerField()
    fail= models.IntegerField()
    id_level= models.ForeignKey(Level, related_name= 'id_level', on_delete=models.CASCADE)