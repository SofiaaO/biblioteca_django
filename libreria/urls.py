from django.urls import path
from . import views

urlpatterns = [
    path('', views.inicio, name='inicio'),

    path('autores/', views.lista_autores, name='lista_autores'),
    path('autores/crear', views.crear_autores, name='crear_autores'),
    path('autores/modificar/<int:pk>/', views.modificar_autores, name='modificar_autores'),
    path('autores/eliminar/<int:pk>/', views.eliminar_autores, name='eliminar_autores'),

    path('libros/', views.lista_libros, name='lista_libros'),
    path('libros/crear', views.crear_libros, name='crear_libros'),
    path('libros/modificar/<int:pk>/', views.modificar_libros, name='modificar_libros'),
    path('libros/eliminar/<int:pk>/', views.eliminar_libros, name='eliminar_libros'),
]
