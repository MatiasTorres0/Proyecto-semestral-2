from django.urls import path
from .views import inicio, registro_usuario,listado_productos, crear_cuenta,iniciosub, modificar_productos, eliminar_producto,codigo, carrito, productos, fecha,  despacho, nuevacontraseña, olvidecontraseña, quienessomos, retiro, solicituddespacho, subscripciones,productos,retirotienda

urlpatterns = [
    path('', inicio, name="inicio"),
    path('crear_cuenta/', crear_cuenta, name="crear_cuenta"),
    path('iniciosub',iniciosub, name="iniciosub"),
    path('codigo/', codigo, name="codigo"),
    path('productos/', productos, name="productos"),
    path('fecha/', fecha, name="fecha"),

    path('despacho/',despacho, name="despacho"),
    path('nuevacontraseña/', nuevacontraseña, name="nuevacontraseña"),
    path('olvidecontraseña',olvidecontraseña, name="olvidecontraseña"),
    path('quienessomos/', quienessomos, name="quienessomos"),
    path('retiro/', retiro, name="retiro"),
    path('solicituddespacho/', solicituddespacho, name="solicituddespacho"),
    path('subscripciones/', subscripciones, name="subscripciones"),
    path('productos/', productos, name="productos"),
    path('retirotienda/', retirotienda, name="retirotienda"),
    path('modificar-productos/<id>', modificar_productos, name="modificar_productos"),
    path ('carrito/', carrito, name="carrito"),
    path ('eliminar_producto/<id>', eliminar_producto, name="eliminar_producto"),
    path ('registro/',registro_usuario,name="registro_usuario"),
    path('listado_productos',listado_productos,name="listado_productos"),
]