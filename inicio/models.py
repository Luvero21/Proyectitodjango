from django.db import models



class Producto(models.Model):
    nombre = models.CharField(max_length=200)
    descripcion = models.TextField()
    precio = models.DecimalField(max_digits=6, decimal_places=2)
    imagen = models.ImageField(upload_to='static/assets', blank=True, null=True)
    stock = models.IntegerField(default=0)
    

    def __str__(self):
        return self.nombre
    
class Usuario(models.Model):
    nombre_usuario = models.CharField(max_length=30, unique=True)
    nombre = models.CharField(max_length=50)
    email = models.EmailField(unique=True)
    password= models.CharField(max_length=50)
    edad = models.PositiveIntegerField()
    
class Cliente(models.Model):
    nombre = models.CharField(max_length=100)
    direccion = models.CharField(max_length=200)
    telefono = models.CharField(max_length=20)
    email = models.EmailField()

    def __str__(self):
        return self.nombre



    



    
    


