from django.urls import path
from accounts.views import login, registro, editar_perfil, detalleUsuario, cambioPassword
from django.contrib.auth.views import LogoutView
from accounts.views import ListaUsuariosView

urlpatterns = [
    path('login/',login, name='login'),
    path('logout/', LogoutView.as_view(template_name='accounts/logout.html'), name='logout'),
    path('registrarse/', registro, name='registrate' ),
    path('perfil/editar/', editar_perfil, name='editar_perfil'),
    path('lista_usuarios/', ListaUsuariosView.as_view(), name='lista_usuarios'),
    path('perfil/detalleUsuario/', detalleUsuario, name='detalleUsuario'),
    path('perfil/editar/password', cambioPassword.as_view(), name='cambioPassword')
]

