from django.shortcuts import render, redirect
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.contrib.auth import authenticate, login as django_login
from accounts.forms import formularioRegistro, password, EdicionPerfil
from django.contrib.auth.decorators import login_required
from django.contrib.auth.views import PasswordChangeView
from django.urls import reverse_lazy
from accounts.models import Extra


def login(request):
    
    formulario= AuthenticationForm()
    
    
    if request.method == 'POST':
        formulario = AuthenticationForm(data=request.POST)
        if formulario.is_valid():
            usuario=formulario.cleaned_data.get('username')
            contraseña=formulario.cleaned_data.get('password')
           
            user= authenticate(username=usuario,password=contraseña)
            
            if user:
                django_login(request,user)
                return redirect('inicio') 
            
        formulario.fields['username'].widget.attrs['placeholder'] = 'Nombre de usuario'
        formulario.fields['password'].widget.attrs['placeholder'] = 'Contraseña'

    return render (request , 'accounts/login.html', {'formulario_login': formulario})

def registro (request):
    formulario=formularioRegistro()
    
    if request.method == 'POST':
        formulario=formularioRegistro(request.POST)
        if formulario.is_valid():
            
            formulario.save()
              
            return redirect('login')        
    
    return render (request, 'accounts/registros.html', {'formulario_registro': formulario})

def lista_registrados(request):
    usuarios = Extra.objects.all()
    return render(request, 'accounts/lista_registrados.html', {'usuarios': usuarios})


@login_required
def detalleUsuario(request):
    extra_info = request.user.extra
    
    return render(request, 'accounts/detalleUsuario.html', {'extra_info': extra_info })

    

def editar_perfil(request):
    
    datos_extra = request.user.extra
    
    formulario = EdicionPerfil(instance=request.user, initial={'pais': datos_extra.pais, 'avatar': datos_extra.avatar})
    
    if request.method == 'POST':
        formulario = EdicionPerfil(request.POST, request.FILES, instance=request.user)
        
        if formulario.is_valid():
            
            nuevo_pais = formulario.cleaned_data.get('pais')
            nueva_avatar = formulario.cleaned_data.get('avatar')
            
            if nuevo_pais:
                datos_extra.pais = nuevo_pais
            if nueva_avatar:
                datos_extra.avatar = nueva_avatar
            
            datos_extra.save()
            formulario.save()
            
            return redirect('detalleUsuario')
    
    return render(request, 'accounts/editar_perfil.html', {'formulario': formulario})


class cambioPassword (PasswordChangeView):
    form_class=password
    template_name= 'accounts/cambioPassword.html'
    success_url= reverse_lazy('detalleUsuario')
    

