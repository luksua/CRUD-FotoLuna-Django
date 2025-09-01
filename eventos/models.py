from django.db import models

# Create your models here.
class Evento(models.Model):
    tipoEvento = models.CharField(max_length=50)
    
    def __str__(self):
        return self.tipoEvento