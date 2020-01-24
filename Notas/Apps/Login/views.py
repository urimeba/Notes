from django.shortcuts import render, redirect, HttpResponse
from django.contrib import messages
from django.contrib.auth.forms import UserCreationForm
import json
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login
from Apps.Notes import views as views_notas

# Create your views here.

def index_login(request):
    if 'usuario' in request.session:
        return redirect(views_notas.index_notes)
    else:
        return render(request, "home.html")

def RegistroUsuarios(request):
    return render(request, "registro.html")

def iniciarSesion(request):
    usuario = request.POST['usuario']
    contraseña = request.POST['contraseña']

    user = authenticate(username=usuario,password=contraseña)

    if user is not None:
        if user.is_active:
            login(request, user)
            request.session['usuario'] = usuario
            return HttpResponse("1")
        else:
            return HttpResponse("Datos incorrectos")
    else:
        return HttpResponse("Datos incorrectos")

def registrarUsuario(request):
    respuesta = ""

    datos = request.POST.get("datosUsuario[]")
    datos = json.loads(datos)

    usuario = datos[0]
    contraseña = datos[1]
    nombre = datos[2]
    apellido = datos[3]
    correo = datos[4]

    try:
        usuarios = User.objects.get(email=correo)
        respuesta = True
    except Exception as e:
        print(e)
        respuesta = False
    
    if respuesta:
        respuesta = "Registro fallido: ya existe un usuario con ese correo"
    else:
        try:
            user = User.objects.create_user(usuario, correo, contraseña)
            user.first_name = nombre
            user.last_name = apellido
            user.save()
            respuesta = "Registro exitoso"
        except Exception as e:
            print(e)
            respuesta = "Registro fallido: el usuario ya existe"
    return HttpResponse(respuesta)


def cerrar_sesion(request):
    print(request.session['usuario'])
    del request.session['usuario']
    return redirect('/')