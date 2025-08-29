from django.contrib import admin
from .models import Cliente, Evento, Paquete, Cita

# Register your models here.
admin.site.register(Cliente)
admin.site.register(Evento)
admin.site.register(Paquete)
admin.site.register(Cita)