from django.shortcuts import render, redirect
from .models import Evento
from .forms import EventoForm

def homeEvent(request):
    tipoEvento = Evento.objects.all()
    context = {'tipoEvento': tipoEvento}
    return render(request, 'eventos/homeEvent.html', context)

# Create your views here.
def agregarEvent(request):
    if request.method == 'POST':
        form = EventoForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('eventos')
    else:
        form= EventoForm()
    
    context = {'form': form}
    return render(request, 'eventos/agregarEvent.html', context)

def eliminarEvent(request, tipoEvento_id):
    tipoEvento = Evento.objects.get(id=tipoEvento_id)
    tipoEvento.delete()
    return redirect("eventos")

def editarEvent(request, tipoEvento_id):
    tipoEvento = Evento.objects.get(id=tipoEvento_id)
    if request.method == "POST":
        form = EventoForm(request.POST, instance=tipoEvento)
        if form.is_valid():
            form.save()
            return redirect("eventos")
    else:
        form = EventoForm(instance=tipoEvento)
    context = {"form": form}
    return render(request, "eventos/editarEvento.html", context)