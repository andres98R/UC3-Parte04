from django.shortcuts import render

# Create your views here.
def index(request):
    return render(request, 'index.html')

def inicio(request):
    cursos = ['Simulación de Sistemas',
'Lenguaje de programación III',
'Desarrollo de Aplicaciones para Móviles',
'Arquitectura de Computadoras',
'Sistemas Operativos',
'Sistemas de Información',
'Introducción a la Robótica']

    return render(request, 'inicio.html',{
        'cursos':cursos
    })