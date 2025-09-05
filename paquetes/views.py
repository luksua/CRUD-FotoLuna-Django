from django.shortcuts import render, redirect
from .models import Paquete
from .forms import PaqueteForm 

def home_Paquete(request):
    paquetes = Paquete.objects.all()
    context = {"paquetes": paquetes}
    return render(request, "paquetes/homePaquete.html", context)

def agregar_paquete(request):
    if request.method == "POST":
        form = PaqueteForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("paquetes")
    else:
        form = PaqueteForm()
    context = {"form": form}
    return render(request, "paquetes/agregaPaquete.html", context)

def editar_paquete(request, Paquetes_id):
    paquete = Paquete.objects.get(id=Paquetes_id)
    if request.method == "POST":
        form = PaqueteForm(request.POST, instance=paquete)
        if form.is_valid():
            form.save()
            return redirect("paquetes")
    else:
        form = PaqueteForm(instance=paquete)
        context={"form": form, "paquete": paquete}
    return render(request, "paquetes/editPaquete.html", context)


def eliminar_paquete(request, Paquetes_id):
    paquete= Paquete.objects.get(id=Paquetes_id)
    paquete.delete()
    return redirect("paquetes")