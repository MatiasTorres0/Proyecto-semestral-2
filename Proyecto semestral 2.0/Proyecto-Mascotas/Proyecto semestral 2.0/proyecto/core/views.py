from urllib.request import Request
from django.shortcuts import render

# Create your views here.
def inicio(request):
    return render(request,'core/inicio.html')

def codigo(request):
    return render(request,'core/codigo.html')

def crear_cuenta(request):
    return render(request,'core/crear_cuenta.html')

def iniciosub(request):
    return render(request,'core/iniciosub.html')

def productos(request):
    return render(request,'core/productos.html')

def subscripciones(request):
    return render(request,'core/subscripciones.html')

def quienessomos(request):
    return render(request,'core/quienessomos.html')

def retiro(request):
    return render(request,'core/retiro.html')

def fecha(request):
    return render(request, 'core/fecha.html')

def iniciosub(request):
    return render(request,'core/iniciosub.html')

def despacho(request):
    return render(request,'core/despacho.html')

def nuevacontraseña(request):
    return render(request,'core/nuevacontraseña.html')

def olvidecontraseña(request):
    return render(request,'core/olvidecontraseña.html')

def iniciarseccion(request):
    return render(request,'core/iniciarseccion.html')
def solicituddespacho(request):
    return render(request,'core/solicituddespacho.html')

def productos(request):
    product= Producto.objects.all()
    data={
        'productos':product()
    }
    return render(request,'core/productos.html',data)