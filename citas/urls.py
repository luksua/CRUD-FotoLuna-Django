from citas import views
from django.urls import path
from citas import views

urlpatterns = [
    path("", views.home, name="home"),
    path("agregar/", views.agregar, name="agregar"),
    path("eliminar/<int:id_cita>/", views.eliminar, name="eliminar"),
    path("editar/<int:id_cita>/", views.editar, name="editar"),
]
