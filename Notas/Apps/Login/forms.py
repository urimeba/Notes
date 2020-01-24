from django import forms
from Apps.Login import models as models_login
from django.contrib.auth.models import User as users
from django.contrib.auth.forms import 

class IniciarSesion(forms.ModelForm):
    class Meta:
        model = models_login.Usuarios
        fields = [
            'usuario',
            'contraseña'
        ]

        labels = {
            'usuario' : 'Usuario',
            'contraseña': 'Contraseña', 
        }

        widgets = {
            'usuario': forms.TextInput(attrs={'class':'form-control', 'placeholder':'usuario', 'required':'true'}),
            'contraseña' : forms.PasswordInput(attrs={'class':'form-control', 'placeholder':'password', 'required':'true'})
        }

class RegistroUsuarios(forms.ModelForm):
    class Meta:
        model = users
        fields = [
            'username',
            'password',
            'first_name',
            'email',

        ]

        labels = {
            'username':'Usuario',
            'password':'Contraseña',
            'first_name':'Nombre completo',
            'email':'Correo electrónico'
        }

        widgets = {
            'username': forms.TextInput(attrs={'class':'form-control', 'placeholder':'usuario'}),
            'password' : forms.PasswordInput(attrs={'class':'form-control', 'placeholder':'password'}),
            'first_name': forms.TextInput(attrs={'class':'form-control', 'placeholder':'nombre','required':'true'}),
            'email': forms.EmailInput(attrs={'class':'form-control', 'placeholder':'correo','required':'true'}),
        }
