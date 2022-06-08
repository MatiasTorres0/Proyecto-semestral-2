from django.db import models
from django.db.models.deletion import CASCADE
# Create your models here.

class Tipo(models.Model):

    nombre= models.CharField(max_length=80)

class Producto(models.Model):
    nombre= models.CharField(max_length=200)
    peso=models.IntegerField()
    precio= models.IntegerField()
    infomacion=models.CharField(max_length=2000)