from django import forms
from .models import Producto
from .models import Cliente


class ClienteForm(forms.ModelForm):
    class Meta:
        model = Cliente
        fields = ['nombre', 'direccion', 'telefono', 'email']
       
class actualizarClienteFormulario(forms.Form):
    nombre = forms.CharField(max_length=100)
    direccion = forms.CharField(max_length=200)
    telefono = forms.CharField(max_length=20)
    email = forms.EmailField()


class ActualizarProductoFormulario(forms.ModelForm):
    class Meta:
        model = Producto
        fields = ['nombre', 'descripcion', 'precio', 'stock', 'imagen']
        widgets = {
            'descripcion': forms.Textarea(),
            'imagen': forms.FileInput(),
        }
        

    
    
    