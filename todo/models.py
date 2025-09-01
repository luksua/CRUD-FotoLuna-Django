from django.db import models
from django.contrib.auth.hashers import make_password

# Create your models here.

class Cliente(models.Model):
    nombreCliente = models.CharField(max_length=100)
    apellidoCliente = models.CharField(max_length=100)
    fotoCliente = models.ImageField(upload_to="uploads/fotos_cliente/", null=True, blank=True)
    correoCliente = models.CharField(max_length=200)
    contrasena = models.CharField(max_length=200)
    
    def save(self, *args, **kwargs):
        if not self.contrasena.startswith('pbkdf2_'):
            self.contrasena = make_password(self.contrasena)
        super().save(*args, **kwargs)
        
    telefonoCliente = models.CharField(max_length=20)
    TIPO_DOC_CHOICES = [
        ("CC", "Cedula"),
        ("PAS", "Pasaporte"),
        ("CE", "Cedula Extranjeria")
    ]
    tipoDocCliente = models.CharField(max_length=20, choices=TIPO_DOC_CHOICES)
    numeroDocCliente = models.CharField(max_length=20)
    
    def __str__(self):
        return f"{self.nombreCliente} {self.apellidoCliente}"