import string
from django.db import models
import uuid


class User(models.Model):
    """contains the fields of the User model"""
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    country = models.CharField(max_length=20, blank=False)
    name = models.CharField(max_length=50, null=False, blank=False)
    email = models.EmailField(max_length=255, unique=True, blank=False)
    password = models.CharField(max_length=255)
    
class Kid(models.Model):
    """contains the fields of the Kid model"""
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = models.CharField(max_length=50, blank=False, null=False, unique=True)
    age = models.IntegerField(blank=False)
    avatar = models.CharField(max_length=50)
    user = models.ForeignKey(User, related_name='user', null=True, on_delete=models.PROTECT, blank=False)

class Level(models.Model):
    """contains the fields of the Level model"""
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    stage = models.IntegerField(blank=False)
    lvl = models.CharField(max_length=20, blank=False, null=True)
    type= models.CharField(max_length=20, blank=False, null=True)
    kid = models.ForeignKey(Kid, related_name='Lkid',null=True, on_delete=models.CASCADE, blank=False)

class Progress(models.Model):
    """contains the fields of the Progress model"""
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    games= models.IntegerField()
    date= models.DateField(auto_now=True)
    type= models.IntegerField(blank=False, null=True)
    score= models.DecimalField(decimal_places=1, max_digits=2)#representacion esta en cadena
    correct= models.IntegerField()
    fail= models.IntegerField()
    level= models.ForeignKey(Level, related_name= 'level', null=True, on_delete=models.CASCADE)
    kid = models.ForeignKey(Kid, related_name= 'kid', null=True, on_delete=models.CASCADE)
