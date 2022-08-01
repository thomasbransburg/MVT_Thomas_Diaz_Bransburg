from django.http import HttpResponse
from django.shortcuts import render
from django.template import Template,Context,loader


from familia.models import familiares

# Create your views here.
def miembros_familia(request):
    
    datos_familia = familiares.objects.all() #como traer el sql

    integrantes = []

    for persona in datos_familia:    #lista
        integrantes.append(persona.nombre)
        integrantes.append(persona.edad)
        integrantes.append(persona.nacimiento)

    data = {"familiares" : integrantes} #aca se crea el diccionario

    archivo = open("/Users/thomasbranburg/Documents/coder house/Desafio/MVT_Thomas_Diaz_Bransburg/MVT_Thomas_Diaz_Bransburg/Templates/index.html","r")

    contenido_html = archivo.read()
    archivo.close()

    plantilla = Template(contenido_html)

    contexto = Context(data) #le doy el contexto al diccionario

    doc_render = plantilla.render(contexto)

    return HttpResponse(doc_render)
    
    