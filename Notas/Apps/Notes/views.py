from django.shortcuts import render, redirect
from django.http import HttpResponse, JsonResponse
from Apps.Notes import models as models_notes
import json
from Apps.Notes import models as models_notas
from django.contrib.auth.models import User

# Create your views here.

def index_notes(request):
    if 'usuario' in request.session:
        categorias = models_notes.Categorias.objects.all().filter(usuario_id=request.user.id)
        return render(request, "navbar_notes.html", {"categorias":categorias})
    else:
        return redirect('/')

def obtenerNotas(request):
    datosNotas = []
    idCategoria = request.POST.get("idCategoria")

    if idCategoria=="":
        notas = models_notes.Notes.objects.filter(usuario_id=request.user.id)
        for nota in notas:
            datosNotas.append([nota.id, nota.titulo, nota.descripcion, nota.categoria_id, nota.usuario_id, nota.color, nota.fecha])
    else:
        notas = models_notes.Notes.objects.filter(categoria_id=idCategoria)
        for nota in notas:
            datosNotas.append([nota.id, nota.titulo, nota.descripcion, nota.categoria_id, nota.usuario_id, nota.color, nota.fecha])

    diccionario = {}
    diccionario['notas']=datosNotas
    return JsonResponse(diccionario)

def añadirCategoria(request):
    categoria_nueva = request.POST.get('categoria')
    id_usuario = request.user.id
    contador=0
    respuesta = {}

    categorias = models_notas.Categorias.objects.filter(usuario_id=id_usuario)

    for categoria in categorias:
        if categoria.titulo==categoria_nueva:
            contador+=1

    if(contador>0):
        print("Esa categoria ya existe")
        respuesta['verificacion']=True
        return JsonResponse(respuesta)
    else:
        print("Esa categoria no existe")
        categoria_agregada = models_notas.Categorias(titulo=categoria_nueva, usuario_id=id_usuario)
        categoria_agregada.save()

        respuesta['verificacion']=False
        respuesta['id'] = categoria_agregada.id
        respuesta['nombre']=categoria_nueva
        return JsonResponse(respuesta)

def eliminarCategoria(request):
    categoria = request.POST.get('id')
    respuesta = ""

    try:
        categoria_eliminada = models_notas.Categorias.objects.filter(id=categoria).delete()
        respuesta = "Categoria eliminada"
    except Exception as e:
        print(e)
        respuesta = "Error al eliminar la categoria"
    

    return HttpResponse(respuesta)

def eliminarNota(request):
    nota = request.POST.get('id')
    respuesta =""

    try:
        models_notas.Notes.objects.filter(id=nota).delete()
        respuesta = "Nota eliminada"
    except Exception as e:
        print(e)
        respuesta = "Error al eliminar la nota"


    return HttpResponse(respuesta)

def obtenerCategorias(request):
    categorias = models_notes.Categorias.objects.filter(usuario_id=request.user.id)
    arreglo_categorias = []

    for categoria in categorias:
        # print(categoria.titulo)
        arreglo_categorias.append(categoria.titulo)

    diccionario = {}
    diccionario['categorias'] = arreglo_categorias
    return JsonResponse(diccionario)

def añadirNota(request):
    titulo = request.POST.get('titulo')
    descripcion = request.POST.get('descripcion')
    categoria = request.POST.get('categoria')
    id_categorias = []
    respuesta = ""

    categorias = models_notas.Categorias.objects.filter(titulo=categoria, usuario_id=request.user.id)
    for categoria in categorias:
        id_categorias.append(categoria.id)

    if((len(id_categorias))==0):
        id_categorias.append(1)

    try:
        nota_nueva = models_notas.Notes(titulo=titulo,descripcion=descripcion,usuario_id=request.user.id,categoria_id=id_categorias[0],color="#FFF2AB")
        nota_nueva.save()
        respuesta = "Nota añadida"
    except Exception as e:
        print(e)
        respuesta = "Error al añadir la Nota"
    return HttpResponse(respuesta)

def cambiarTitulo(request):
    id = request.POST.get('id')
    titulo = request.POST.get('titulo')
    respuesta = ""
    print(titulo)

    print(id)
    print(titulo)

    try:
        nota_cambiada = models_notas.Notes.objects.filter(id=id)
        for nota in nota_cambiada:
            nota.titulo = titulo
            nota.save()
        respuesta = "Titulo cambiado correctamente"
    except Exception as e:
        print(e)
        respuesta = "Error al cambiar el titulo de la nota"

    return HttpResponse(respuesta)

def cambiarDescripcion(request):
    id = request.POST.get('id')
    descripcion = request.POST.get('descripcion')
    respuesta = ""

    # print(id)
    # print(descripcion)

    try:
        nota_cambiada = models_notas.Notes.objects.filter(id=id)
        for nota in nota_cambiada:
            nota.descripcion = descripcion
            nota.save()
        respuesta = "Nota cambiada correctamente"
    except Exception as e:
        print(e)
        respuesta = "Error al cambiar la nota"

    return HttpResponse(respuesta)

def cambiarColor(request):
    color = request.POST.get('color')
    id = request.POST.get('id')
    respuesta=""

    try:
        nota_cambiada = models_notas.Notes.objects.filter(id=id)
        for nota in nota_cambiada:
            nota.color = color
            nota.save()
        respuesta = "Nota cambiada correctamente"
    except Exception as e:
        print(e)
        respuesta = "Error al cambiar la nota"

    return HttpResponse(respuesta)

def enviarNota(request):
    id = request.POST.get('id')
    usuario = request.POST.get('usuario')
    respuesta = ""

    idNota = models_notas.Notes.objects.get(id=id).id
    tituloNota = models_notas.Notes.objects.get(id=id).titulo
    descripcionNota = models_notas.Notes.objects.get(id=id).descripcion
    colorNota = models_notas.Notes.objects.get(id=id).color
    fechaNota = models_notas.Notes.objects.get(id=id).fecha
    

    try:
        idUsuario = User.objects.get(username=usuario).id
        respuesta = True
    except Exception as e:
        print(e)
        respuesta=False

    if respuesta:
        if(idUsuario==request.user.id):
            return HttpResponse("Error: no te puedes enviar notas")
        else:
            nota_copiada = models_notas.Notes(titulo=tituloNota, descripcion=descripcionNota, categoria_id=1, usuario_id=idUsuario,color=colorNota,fecha=fechaNota)
            nota_copiada.save()
            return HttpResponse("Nota enviada correctamente")
    else:
        return HttpResponse("Error: ese usuario no existe")
