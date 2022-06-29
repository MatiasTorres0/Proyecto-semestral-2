from urllib.request import Request
from django.shortcuts import render
from .models import Producto
from .forms import ProductoForm
from .forms import CustomUserForm
from django.contrib.auth import login,authenticate
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required, permission_required
from django.shortcuts import render, redirect

# rest_framework
from rest_framework import viewsets
from .serializers import ProductoSerializer
# Create your views here.
def inicio(request):
    return render(request,'core/inicio.html')



def codigo(request):
    return render(request,'core/codigo.html')

def crear_cuenta(request):
    return render(request,'core/crear_cuenta.html')

def iniciosub(request):
    return render(request,'core/iniciosub.html')

# @login_required
# def productos(request):
#     return render(request,'core/productos.html')

def subscripciones(request):
    return render(request,'core/subscripciones.html')

def quienessomos(request):
    return render(request,'core/quienessomos.html')
@login_required
def retiro(request):
    return render(request,'core/retiro.html')
@login_required
def fecha(request):
    return render(request, 'core/fecha.html')

def iniciosub(request):
    return render(request,'core/iniciosub.html')
@login_required
def despacho(request):
    return render(request,'core/despacho.html')

def nuevacontraseña(request):
    return render(request,'core/nuevacontraseña.html')

def olvidecontraseña(request):
    return render(request,'core/olvidecontraseña.html')
@permission_required(['core.add_producto'])
def modificar_productos(request, id):
    productos=Producto.objects.get(id=id)
    data={
        'form':ProductoForm(instance=productos)
    }
    if request.method == 'POST':
        formulario = ProductoForm(data=request.POST , instance=productos)
        if formulario.is_valid():
            formulario.save()
            data['mensaje']="Modificado correctamente"
            data['form'] = formulario

    return render(request,'core/modificar_productos.html',data)
@login_required
def solicituddespacho(request):
    return render(request,'core/solicituddespacho.html')
@login_required
def productos(request):
    product= Producto.objects.all()
    data={
        'product':product
    }
    return render(request,'core/productos.html',data)
@login_required
def retirotienda(request):
    return render(request,'core/retirotienda.html')

@login_required
def eliminar_producto(request,id):
    product=Producto.objects.get(id=id)
    product.delete()
    return redirect(to="listado_productos")

def registro_usuario(request):
    data={
        'form':CustomUserForm()
    }
    if request.method == 'POST':
        formulario=CustomUserForm(request.POST)
        if formulario.is_valid():
            formulario.save()
            username= formulario.cleaned_data['username']
            password= formulario.cleaned_data['password']
            user= authenticate(username=username,password=password)
            login(request,user)
            return redirect(to="home")
    return render(request,'registration/registro.html',data)

@permission_required(['core.edit_producto'])
def listado_productos(request):
    product= Producto.objects.all()
    data={
        'product':product
    }
    return render(request, 'core/listado_productos.html' ,data)

def carrito(request):
    product= Producto.objects.all()
    data={
        'product':product
        
        }
    return render(request,'core/carrito.html',data)


class ProductoViewSet(viewsets.ModelViewSet):
    queryset = Producto.objects.all()
    serializer_class = ProductoSerializer


