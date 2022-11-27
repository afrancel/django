from django.shortcuts import render, redirect
#from django.http import HttpResponse
from .models import bicicleta
from .forms import BicicletaForm

# Create your views here.
def inicio(request):
    return render(request, 'pages/inicio.html')
def nosotros(request):
    return render(request, 'pages/nosotros.html')

def bicis(request):
    bicis = bicicleta.objects.all()
    return render(request, 'bicis/index.html',{'bicis':bicis})
    
def crear(request):
    formulario = BicicletaForm(request.POST or None, request.FILES or None)
    if formulario.is_valid():
        formulario.save()
        return  redirect('bicis')
    return render(request, 'bicis/crear.html',{'formulario':formulario})

def editar(request, id):
    bicieditar = bicicleta.objects.get(id=id)
    formulario = BicicletaForm(request.POST or None, request.FILES or None,instance=bicieditar)
    if formulario.is_valid() and request.POST:
        formulario.save()
        return  redirect('bicis')
    return render(request, 'bicis/editar.html',{'formulario':formulario})

def eliminar(request, id):
    bicieliminar = bicicleta.objects.get(id=id)
    bicieliminar.delete()
    #return render(request, 'bicis/eliminar.html') podría ir a otra página, pero nos quedamos allí por eso
    #dejamos la linea siguiente y no esta
    return redirect('bicis')