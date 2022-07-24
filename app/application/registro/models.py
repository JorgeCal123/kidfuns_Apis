import string
import uuid
from .choices import status, lvls, area
from django.db import models
#from django.contrib.auth.models import AbstractBaseUser,PermissionsMixin,BaseUserManager
#from django.utils.translation import gettext_lazy


class User(models.Model):
    id = models.UUIDField(
        primary_key=True, default=uuid.uuid4, editable=False)
    country = models.CharField(max_length=20, blank=False)
    name = models.CharField(max_length=50, null=False, blank=False)
   # username= models.CharField(_('User Name'),max_length=150)
    email = models.EmailField(max_length=255, unique=True, blank=False)
    password = models.CharField(max_length=255)
  #  is_staff=models.BooleanField(default=False)
 #   is_active=models.BooleanField(default=True)

    #objects=CustomUserManager()

    #USERNAME_FIELD='email'
    #REQUIRED_FIELDS=['username','name']
   
    #def __str__(self):
    #   return self.email
    

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
    status = models.CharField(verbose_name="Estado", max_length=1, choices=status, default=2)
    stage = models.CharField(verbose_name="Nivel", max_length=1, choices=lvls, null=True)
    area = models.CharField(verbose_name="Curso", max_length=1, choices=area, null=True)
    kid = models.ForeignKey(Kid, related_name='kid_id',null=True, on_delete=models.CASCADE, blank=False)


class Progress(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    games = models.IntegerField()
    date = models.DateField(auto_now=True)
    area = models.CharField(verbose_name="Curso", max_length=1, choices=area, null=True)
    score = models.DecimalField(max_digits=2, decimal_places=1)#representacion esta en cadena
    correct = models.IntegerField()
    fail = models.IntegerField()
    level = models.ForeignKey(
        Level, related_name='progress', null=True, on_delete=models.CASCADE)
    kid = models.ForeignKey(
        Kid, related_name='progress', null=True, on_delete=models.CASCADE)

    def __str__(self):
        return '%d, %d' % (self.score, self.correct)

#class CustomAccountManager(BaseUserManager):
#    def create_user(self,email,username,name,password,**other_fields):
#        if not email:
#            raise ValueError(_('Please provide an email address'))
#        email=self.normalize_email(email)
#        user=self.model(email=email,username=username,name=name,**other_fields)
#        user.set_password(password)
#        user.save()
#        return user
#    def create_superuser(self,email,username,first_name,password,**other_fields):
#        other_fields.setdefault('is_staff',True)
#        other_fields.setdefault('is_superuser',True)
#        other_fields.setdefault('is_active',True)
#        if other_fields.get('is_staff') is not True:
#                raise ValueError(_('Please assign is_staff=True for superuser'))
#        if other_fields.get('is_superuser') is not True:
 #               raise ValueError(_('Please assign is_superuser=True for superuser'))
#        return self.create_user(email,username,first_name,password,**other_fields)