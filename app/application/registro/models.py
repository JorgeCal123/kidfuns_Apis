import string
import uuid

from django.db import models


class User(models.Model):
    id = models.UUIDField(
        primary_key=True, default=uuid.uuid4, editable=False)
    country = models.CharField(max_length=20, blank=False)
    name = models.CharField(max_length=50, null=False, blank=False)
    email = models.EmailField(max_length=255, unique=True, blank=False)
    password = models.CharField(max_length=255)
    

class Kid(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = models.CharField(max_length=50, blank=False, null=False, unique=True)
    age = models.IntegerField(blank=False)
    avatar = models.CharField(max_length=50)
    user = models.ForeignKey(
        User, related_name='kid', null=True, on_delete=models.PROTECT,
        blank=False)


class Level(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    stage = models.IntegerField(blank=False)
    kid = models.ForeignKey(
        Kid, related_name='level',null=True, on_delete=models.CASCADE,
        blank=False)


class Progress(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    games = models.IntegerField()
    date = models.DateField(auto_now=True)
    type = models.IntegerField(blank=False, null=True)
    score = models.DecimalField(max_digits=2, decimal_places=1)#representacion esta en cadena
    correct = models.IntegerField()
    fail = models.IntegerField()
    level = models.ForeignKey(
        Level, related_name='progress', null=True, on_delete=models.CASCADE)
    kid = models.ForeignKey(
        Kid, related_name='progress', null=True, on_delete=models.CASCADE)
