from django.db import models
from eventos.models import Evento
from todo.models import Cliente

# Create your models here.
class Cita(models.Model):
    clienteFK = models.ForeignKey(Cliente, on_delete=models.CASCADE)
    eventoFK = models.ForeignKey(Evento, on_delete=models.CASCADE)
    fechaCita = models.DateField()
    horaCita = models.TimeField()
    lugar = models.CharField(max_length=100)
    comentario = models.TextField(max_length=200)
    
    def __str__(self):
        return f"{self.clienteFK} {self.eventoFK} {self.fechaCita}"