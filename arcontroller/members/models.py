from django.db import models
from django.db.models.fields import CharField, EmailField, URLField
from django.db.models.fields.files import ImageField

# Create your models here.
class person(models.Model):
    nombre = CharField(max_length=70)
    apellido = CharField(max_length=70)
    foto = ImageField(upload_to='person/images')
    correo = EmailField(max_length=70)
    url = URLField( blank=True)