# Generated by Django 4.2.6 on 2023-11-19 07:29

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('inicio', '0004_producto_stock'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='itempedido',
            name='pedido',
        ),
        migrations.RemoveField(
            model_name='itempedido',
            name='producto',
        ),
        migrations.RemoveField(
            model_name='pedido',
            name='cliente',
        ),
        migrations.RemoveField(
            model_name='pedido',
            name='productos',
        ),
        migrations.DeleteModel(
            name='UsuarioIngresado',
        ),
        migrations.DeleteModel(
            name='ItemPedido',
        ),
        migrations.DeleteModel(
            name='Pedido',
        ),
    ]