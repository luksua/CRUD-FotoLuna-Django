from django.shortcuts import render
from django.shortcuts import render, redirect

from .models import Cita
from citas.forms import CitaForm

# Create your views here.
def home(request):
    citas = Cita.objects.all()
    context = {'citas': citas}
    return render(request, 'home.html', context )

def agregar(request):
    if request.method == "POST":
        form = CitaForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')
    else:
        form = CitaForm()
        
    context = {'form': form}
    return render(request, 'agregar.html', context)

def eliminar(request, id_cita):
    cita = Cita.objects.get(id=id_cita)
    cita.delete()
    return redirect("home")

def editar(request, id_cita):
    cita = Cita.objects.get(id=id_cita)
    if request.method == "POST":
        form = CitaForm(request.POST, instance=cita)
        if form.is_valid:
            form.save()
            return redirect("home")
    else:
        form = CitaForm(instance=cita)
    context = {"form": form}
    return render(request, "editar.html", context)