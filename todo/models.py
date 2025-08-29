from django.db import models
from django.contrib.auth.hashers import make_password, check_password

# Create your models here.
class Evento(models.Model):
    tipoEvento = models.CharField(max_length=50)
    
    def __str__(self):
        return self.tipoEvento

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

class Cita(models.Model):
    clienteFK = models.ForeignKey(Cliente, on_delete=models.CASCADE)
    eventoFK = models.ForeignKey(Evento, on_delete=models.CASCADE)
    fechaCita = models.DateField()
    horaCita = models.TimeField()
    lugar = models.CharField(max_length=100)
    comentario = models.TextField(max_length=200)
    
    def __str__(self):
        return f"{self.clienteFK} {self.eventoFK} {self.fechaCita}"

class Paquete(models.Model):
    nombrePaquete = models.CharField(max_length=50)
    descripcionPaquete = models.CharField(max_length=200)
    precio = models.DecimalField(max_digits=10, decimal_places=2)
    
    def __str__(self):
        return f"{self.nombrePaquete} {self.precio}"