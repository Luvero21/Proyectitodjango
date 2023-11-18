from django.urls import path
from inicio.views import nosotros, actualizar_producto, actualizar_cliente, eliminar_producto, eliminar_cliente, agregarcliente, crearProducto, inicio, detalle_cliente, confirmacion_registro, lista_productos,lista_clientes,detalle_producto,formulario_cliente
from django.conf.urls.static import static
from django.conf import settings

urlpatterns =[
    path('', inicio, name='inicio'),
    path('nosotros',nosotros , name='nosotros'),
    path('agregarcliente',agregarcliente, name='agregar_cliente'),
    path('detallecliente/<int:cliente_id>/', detalle_cliente, name='detalle_cliente'),
    path('listaproductos/', lista_productos, name='lista_productos'),
    path('listaproductos/<int:producto_id>/eliminar', eliminar_producto, name='eliminar_producto'),
    path('listaproductos/<int:producto_id>/actualizar', actualizar_producto, name='actualizar_producto'),    
    path('listaclientes/<int:cliente_id>>/eliminar', eliminar_cliente, name='eliminar_cliente'),
    path('listaclientes/<int:cliente_id>/actualizar', actualizar_cliente, name='actualizar_cliente'),
    path('listaclientes/<int',lista_clientes, name='lista_clientes'),
    path('detalleproducto/<int:producto_id>/', detalle_producto, name='detalle_producto'),
    path('formulariocliente/', formulario_cliente, name='formulariocliente_sin_id'),
    path('confirmacionregistro/',confirmacion_registro, name='confirmacion_registro'),
    path('formulaireproducto/', crearProducto, name='formulaire'),
    path('confirmacionregistro/<int:cliente_id>/eliminar', eliminar_cliente, name='eliminar_cliente')
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

