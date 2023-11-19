from django.urls import path
from accounts.views import login, registro, editar_perfil, detalleUsuario, cambioPassword,lista_registrados
from django.contrib.auth.views import LogoutView

urlpatterns = [
    path('login/',login, name='login'),
    path('logout/', LogoutView.as_view(template_name='accounts/logout.html'), name='logout'),
    path('registrarse/', registro, name='registrate' ),
    path('perfil/editar/', editar_perfil, name='editar_perfil'),
    path('perfil/listaRegistrados/', lista_registrados, name='lista_registrados'),
    path('perfil/detalleUsuario/', detalleUsuario, name='detalleUsuario'),
    path('perfil/editar/password', cambioPassword.as_view(), name='cambioPassword')
]

