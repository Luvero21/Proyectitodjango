from django import forms
from accounts.models import Extra
from django.contrib.auth.forms import UserCreationForm, UserChangeForm, PasswordChangeForm
from django.contrib.auth.models import User


class formularioRegistro(UserCreationForm):
        email = forms.EmailField()
        username = forms.CharField(label="Nombre de usuario", max_length=150)
        password1 = forms.CharField(label='Contraseña', widget=forms.PasswordInput)
        password2 = forms.CharField(label='Repetir Contraseña', widget=forms.PasswordInput)
        pais = forms.CharField(label='Pais', max_length=150)
        avatar = forms.ImageField(required=False)
        class Meta:
            model = User
            fields = ['username', 'email', 'password1', 'password2','pais', 'avatar']
            help_text = {key:'' for key in fields}


class EdicionPerfil(UserChangeForm):
         email = forms.EmailField()
         class Meta:
                model = Extra
                fields = [
                        'email', 'pais','avatar'
                ]   
                  

class password(PasswordChangeForm):
        old_password=forms.CharField(label='Contraseña actual',widget=forms.PasswordInput())
        new_password1=forms.CharField(label='Contraseña nueva',widget=forms.PasswordInput())
        new_password2=forms.CharField(label='Repita contraseña nueva',widget=forms.PasswordInput())

