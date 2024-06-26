from django.urls import path
from . import views

urlpatterns = [
    path('Principal/<int:pk>/', views.Principal, name='Principal'),
    path('InicioSesion/<int:pk>/', views.InicioSesion, name='InicioSesion'),
    path('ayuda/<int:pk>/', views.ayuda, name='ayuda'),
    path('catalogo/<int:pk>/', views.catalogo, name='catalogo'),
    path('razas/<int:pk>/', views.razas, name='razas'),
    path('registrarse/<int:pk>/', views.registrarse, name='registrarse'),
    path('create/', views.usuario_create, name='usuario_create'),
    path('login/', views.login_view, name='login_view')
]