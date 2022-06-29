from dataclasses import field
from rest_framework import serializers
from .models import Producto 

class ProductoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Producto
        fields = ['nombre', 'peso', 'precio','infomacion', 'stock', 'tipo']


