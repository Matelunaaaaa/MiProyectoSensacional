from django.urls import path
from . import views

urlpatterns = [
    path('Principal', views.Principal, name='Principal'),
]