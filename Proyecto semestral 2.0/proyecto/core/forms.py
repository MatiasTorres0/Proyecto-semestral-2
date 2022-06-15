from django.contrib.auth.forms import UserCreationForm
from django import forms
from django.contrib.auth.models import User
from django.forms import ModelForm
from .models import Producto

class CustomUserForm(UserCreationForm):
    
    class Meta:

        model=User
        fields=['first_name','last_name','email','username','password1','password2']



class ProductoForm(ModelForm):
    nombre=forms.CharField(max_length=200)
    precio=forms.IntegerField()
    stock=forms.IntegerField()
    class Meta:
        model=Producto
        fields=['nombre', 'peso', 'precio', 'infomacion', 'stock','tipo']






    #nombre= models.CharField(max_length=200)
    # peso=models.IntegerField()
    # precio= models.IntegerField()
    # infomacion=models.CharField(max_length=2000)
    # stock=models.IntegerField()
    # tipo=models.ForeignKey(Tipo, on_delete=CASCADE)

