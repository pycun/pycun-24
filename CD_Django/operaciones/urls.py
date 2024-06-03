from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('par/', views.detectar_par, name='detectar_par'),
    path('sumar/', views.sumar, name='sumar'),
    path('restar/', views.restar, name='restar'),
    path('multiplicar/', views.multiplicar, name='multiplicar'),
    path('dividir/', views.dividir, name='dividir'),
]