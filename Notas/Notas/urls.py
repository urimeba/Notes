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

# AGREGANGO LOS ARCHIVOS URLS DE LAS APLICACIONES, PARA QUE LA TOME COMO UNA DIRECCION URL
urlpatterns = [
    path('Administrador/', admin.site.urls),

    # COMENTAMOS LAS APLICACIONES. MIENTRAS LAS NECESITAMOS, LAS DESCOMENTAMOS PARA AGREGARLAS
    # path('Inicio/', include('Apps.Inicio.urls')),
    path('', include('Apps.Login.urls')),
    path('Notes/', include('Apps.Notes.urls')),
    # path('Perfil/', include('Apps.Perfil.urls')),
]