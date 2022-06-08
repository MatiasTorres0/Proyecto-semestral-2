from django.urls import path
from .views import inicio, crear_cuenta,iniciosub, codigo, productos, fecha, iniciarseccion, despacho, nuevacontraseña, olvidecontraseña, quienessomos, retiro, solicituddespacho, subscripciones,productos

urlpatterns = [
    path('', inicio, name="inicio"),
    path('crear_cuenta/', crear_cuenta, name="crear_cuenta"),
    path('iniciosub',iniciosub, name="iniciosub"),
    path('codigo/', codigo, name="codigo"),
    path('productos/', productos, name="productos"),
    path('fecha/', fecha, name="fecha"),
    path('iniciarseccion/',iniciarseccion, name="iniciarseccion"),
    path('despacho/',despacho, name="despacho"),
    path('nuevacontraseña/', nuevacontraseña, name="nuevacontraseña"),
    path('olvidecontraseña',olvidecontraseña, name="olvidecontraseña"),
    path('quienessomos/', quienessomos, name="quienessomos"),
    path('retiro/', retiro, name="retiro"),
    path('solicituddespacho/', solicituddespacho, name="solicituddespacho"),
    path('subscripciones/', subscripciones, name="subscripciones"),
    path('productos/', productos, name="productos"),
]