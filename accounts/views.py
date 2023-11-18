from django.shortcuts import render, redirect
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import authenticate, login as django_login
from accounts.forms import formularioRegistro, password, EdicionPerfil
from django.contrib.auth.decorators import login_required
from django.contrib.auth.views import PasswordChangeView
from django.urls import reverse_lazy
from accounts.models import Extra
from django.contrib.auth.models import User
from django.views.generic import ListView


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
        formulario=formularioRegistro(request.POST, request.FILES)
        if formulario.is_valid():
            
            nuevo_usuario=formulario.save()
            Extra.objects.create(user=nuevo_usuario)
              
            return redirect('login')        
    
    return render (request, 'accounts/registros.html', {'formulario_registro': formulario})



@login_required
def detalleUsuario(request):
    usuario = request.user
    try:
        datos_extra = Extra.objects.get(user=usuario)
        avatar = datos_extra.avatar
    except Extra.DoesNotExist:
        avatar = None

    print("Contenido de extra_info:", datos_extra) 
    return render(request, 'accounts/detalleUsuario.html', {'usuario': usuario, 'extra_info': datos_extra, 'avatar': avatar})

def editar_perfil(request):
    try:
    
     datos_extra = request.user.extra
     
    except Extra.DoesNotExist:
        datos_extra = Extra(user=request.user)
    
    formulario = EdicionPerfil(instance=datos_extra)
    
    if request.method == 'POST':
        formulario = EdicionPerfil(request.POST, request.FILES, instance=datos_extra)
        
        if formulario.is_valid():
            formulario.save()
            return redirect('detalleUsuario')
    
    return render(request, 'accounts/editar_perfil.html', {'formulario': formulario})

class ListaUsuariosView(ListView):
    model = Extra
    template_name = 'accounts/lista_usuarios.html'
    context_object_name = 'extras'

class cambioPassword (PasswordChangeView):
    form_class=password
    template_name= 'accounts/cambioPassword.html'
    success_url= reverse_lazy('detalleUsuario')
    

