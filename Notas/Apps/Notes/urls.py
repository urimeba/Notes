"""Notas URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from django.conf.urls import url
from Apps.Notes import views as views_notes

# AGREGANGO LOS ARCHIVOS URLS DE LAS APLICACIONES, PARA QUE LA TOME COMO UNA DIRECCION URL
urlpatterns = [
    path('', views_notes.index_notes, name="index_notes"),
    path('obtenerNotas', views_notes.obtenerNotas, name="obtenerNotas"),
    path('añadirCategoria', views_notes.añadirCategoria, name="añadirCategoria"),
    path('eliminarCategoria', views_notes.eliminarCategoria, name="eliminarCategoria"),
    path('añadirNota', views_notes.añadirNota, name="añadirNota"),
    path('eliminarNota', views_notes.eliminarNota, name="eliminarNota"),
    path('obtenerCategorias', views_notes.obtenerCategorias, name="obtenerCategorias"),
    path('cambiarDescripcion', views_notes.cambiarDescripcion, name="cambiarDescripcion"),
    path('cambiarTitulo', views_notes.cambiarTitulo, name="cambiarTitulo"),
    path('cambiarColor', views_notes.cambiarColor, name="cambiarColor"),
    path('enviarNota', views_notes.enviarNota, name="enviarNota"),
]