# Generated by Django 4.2.6 on 2023-11-22 03:43

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('inicio', '0005_remove_itempedido_pedido_remove_itempedido_producto_and_more'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Usuario',
        ),
    ]