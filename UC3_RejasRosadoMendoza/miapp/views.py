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

    
def is_prime(num):
    if num < 2:
        return False
    for i in range(2, int(num**0.5) + 1):
        if num % i == 0:
            return False
    return True

def rango(request,a=1,b=100):
    numeros_primos = [num for num in range(a, b + 1) if is_prime(num)]

    arraynumero= []
    for numero in numeros_primos:
        arraynumero.append(numero)

    return render(request, "rango.html", {
        "resultado": arraynumero, 
        'a':a, 
        'b':b
        })
   
   
def examen(request):
        titulo = "Github del Proyecto"
        estudiante1 = "Andres Rejas"
        github1 = "https://github.com/andres98R/UC3_Parte01.git"
        estudiante2 = "David Rosado"
        github2 = "https://github.com/DavidRosVal/UC3-Parte02.git"
        estudiante3 = "Jairo Mendoza"
        github3 = "https://github.com/Jairodaniel-17/Uc3Parte03.git"
        estudiante4 = "Andres Rejas"
        github4 = "https://github.com/andres98R/UC3-Parte04.git"

        return render(request, 'examen.html',{
            'titulo':titulo,
            'estudiante1':estudiante1,
            'estudiante2':estudiante2,
            'estudiante3':estudiante3,
            'estudiante4':estudiante4,
            'github1':github1,
            'github2':github2,
            'github3':github3,
            'github4':github4,
        })
