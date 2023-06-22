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

    resultado = f"""
    <h2>Números de [{a}, {b}]</h2>
    Resultado:<br>
    <ul>
    """
    arraynumero= []
    for numero in numeros_primos:
        resultado += f"<li>{numero}</li>"
        arraynumero.append(numero)
    resultado += "</ul>"

    return render(request, "rango.html", {"resultado": arraynumero, 'a':a, 'b':b})
