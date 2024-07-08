from django.urls import path
from . import views
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('Principal', views.Principal, name='Principal'),
    path('InicioSesion', views.InicioSesion, name='InicioSesion'),
    path('ayuda', views.ayuda, name='ayuda'),
    path('catalogo', views.catalogo, name='catalogo'),
    path('razas', views.razas, name='razas'),
    path('registrarse', views.registrarse, name='registrarse'),
    path('login/', auth_views.LoginView.as_view(), name='login'),
    path('Principal/', views.Principal, name='Principal'),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),
    path('admin', views.admin, name='admin'),
    path('borrar_cliente/<str:pk>', views.borrar_cliente, name='borrar_cliente'),
    path('editar_cliente/<str:pk>', views.editar_cliente, name='editar_cliente'),
    path('editarClientes', views.editarClientes, name='editarClientes')

]
