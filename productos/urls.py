from django.urls import path
from . import views

urlpatterns = [
    path('Principal', views.Principal, name='Principal'),
    path('InicioSesion', views.InicioSesion, name='InicioSesion'),
    path('ayuda', views.ayuda, name='ayuda'),
    path('catalogo', views.catalogo, name='catalogo'),
]