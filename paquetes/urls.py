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
from django.contrib import admin
from django.urls import path, include
from paquetes import views

urlpatterns = [
    path("", views.home_Paquete, name="paquetes"),
    path("editar/<int:Paquetes_id>/", views.editar_paquete, name="editar_paquete"),
    path("eliminar/<int:Paquetes_id>/", views.eliminar_paquete, name="eliminar_paquete"),
    path("agregar/", views.agregar_paquete, name="agregar_paquete"),
]
