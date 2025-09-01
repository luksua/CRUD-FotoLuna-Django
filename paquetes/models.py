from django.db import models

# Create your models here.
class Paquete(models.Model):
    nombrePaquete = models.CharField(max_length=50)
    descripcionPaquete = models.CharField(max_length=200)
    precio = models.DecimalField(max_digits=10, decimal_places=2)
    
    def __str__(self):
        return f"{self.nombrePaquete} {self.precio}"