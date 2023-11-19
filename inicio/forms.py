from django import forms
from .models import Producto
from .models import Cliente, Usuario

class ProductoForm(forms.ModelForm):
    class Meta:
        model = Producto
        fields = ['nombre', 'descripcion', 'precio','stock', 'imagen']


class ClienteForm(forms.ModelForm):
    class Meta:
        model = Cliente
        fields = ['nombre', 'direccion', 'telefono', 'email']

class UsuarioForm(forms.ModelForm):
    class Meta:
        model = Usuario
        fields = [
            'nombre_usuario',
            'nombre',
            'email',
            'edad',
            'password'
        ]

        
class actualizarClienteFormulario(forms.Form):
    nombre = forms.CharField(max_length=100)
    direccion = forms.CharField(max_length=200)
    telefono = forms.CharField(max_length=20)
    email = forms.EmailField()

class actualizarUsuarioFormulario (forms.Form):
    nombre_usuario = forms.CharField(max_length=100)
    nombre = forms.CharField(max_length=100)
    email = forms.EmailField(max_length=100)
    edad = forms.IntegerField()
    password = forms.CharField(widget=forms.PasswordInput)


class ActualizarProductoFormulario(forms.ModelForm):
    class Meta:
        model = Producto
        fields = ['nombre', 'descripcion', 'precio', 'stock', 'imagen']
        widgets = {
            'descripcion': forms.Textarea(),
            'imagen': forms.FileInput(),
        }
        

    
    
    