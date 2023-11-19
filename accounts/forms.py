from django import forms
from django.contrib.auth.forms import UserCreationForm, UserChangeForm, PasswordChangeForm
from django.contrib.auth.models import User


class formularioRegistro(UserCreationForm):
        email = forms.EmailField()
        password1 = forms.CharField(label='Contraseña', widget=forms.PasswordInput)
        password2 = forms.CharField(label='Repetir Contraseña', widget=forms.PasswordInput)
        
        class Meta:
            model = User
            fields = ['username', 'email', 'password1', 'password2']
            help_text = {key:'' for key in fields}
        
class EdicionPerfil(UserChangeForm):
        password = None
        email = forms.EmailField(label='Nuevo email')
        first_name = forms.CharField(label='Nuevo Nombre', required=False)
        last_name = forms.CharField(label='Nuevo Apellido', required=False)
        pais = forms.CharField(max_length=100,required=False)
        avatar = forms.ImageField(required=False)
        class Meta:
                model = User
                fields = [
                        'email','first_name', 'last_name','pais','avatar'
                ]     

                

class password(PasswordChangeForm):
        old_password=forms.CharField(label='Contraseña actual',widget=forms.PasswordInput())
        new_password1=forms.CharField(label='Contraseña nueva',widget=forms.PasswordInput())
        new_password2=forms.CharField(label='Repita contraseña nueva',widget=forms.PasswordInput())
        