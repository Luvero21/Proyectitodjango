from django.db import models
from ckeditor.fields import RichTextField

class Producto(models.Model):
    nombre = models.CharField(max_length=200)
    descripcion = RichTextField()
    precio = models.DecimalField(max_digits=6, decimal_places=2)
    imagen = models.ImageField(upload_to= 'static/assets', blank=True, null=True)
    stock = models.IntegerField(default=0)
    
    def __str__(self):
        return self.nombre
  
class Cliente(models.Model):
    nombre = models.CharField(max_length=100)
    direccion = models.CharField(max_length=200)
    telefono = models.CharField(max_length=20)
    email = models.EmailField()


    def __str__(self):
        return self.nombre



    



    
    


