from django.db import models
from django.db.models.fields import CharField, IntegerField

# Create your models here.
class product(models.Model):
    nombre=CharField(max_length=20)
    tipo=CharField(max_length=20)
    stock=IntegerField