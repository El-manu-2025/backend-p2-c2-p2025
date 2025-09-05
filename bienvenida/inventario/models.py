from django.db import models

class Producto(models.Model):
    nombre = models.CharField(max_length=100)
    precio = models.DecimalField(max_digits=10, decimal_places=2, default=0)
    descripcion = models.TextField(max_length=256, default='')
    stock = models.IntegerField(default=0)
    
    def __str__(self):
        return self.nombre