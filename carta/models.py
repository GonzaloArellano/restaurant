from django.db import models

# Create your models here.

class Menu(models.Model):
    nombre = models.CharField(max_length=100)
    descripcion = models.TextField()
    imagen = models.ImageField(upload_to= 'menus')