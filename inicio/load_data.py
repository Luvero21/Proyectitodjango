from django.core.management.base import BaseCommand
from inicio.models import Cliente, Producto, Pedido

class Command(BaseCommand):
    help = 'Carga datos iniciales en la base de datos'

    def handle(self, *args, **options):
        # Aquí puedes crear objetos y guardarlos en la base de datos
        Cliente.objects.create(nombre='Gustavo', direccion='Moreno 88', telefono='2615675543', email='ejemplo@hotmail.com')
        Producto.objects.create(nombre='Hamburguesa', descripcion='Descripción de la hamburguesa', precio=2999.99)
        Producto.objects.create(nombre='Papas Fritas', descripcion='Descripción de las papas fritas', precio=3393.99)
        Pedido.objects.create(cliente_id=1, total=6398.98)  # Asocia el pedido al cliente de ejemplo

        self.stdout.write(self.style.SUCCESS('Datos cargados con éxito'))
