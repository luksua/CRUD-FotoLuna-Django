"""
URL configuration for tareas project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from citas import views
from django.urls import path
from citas import views

urlpatterns = [
    path("", views.homeCita, name="homeCita"),
    path("agregar/", views.agregarCita, name="agregarCita"),
    path("eliminar/<int:id_cita>/", views.eliminarCita, name="eliminarCita"),
    path("editar/<int:id_cita>/", views.editarCita, name="editarCita"),
]