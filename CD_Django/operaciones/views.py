from django.http import JsonResponse
from django.shortcuts import render

def home(request):
    return render(request, 'operaciones/home.html')


# def detectar_par(request):
#     par = request.GET.get('a')
#     resultado = False
#     if int(par) % 2 == 0:
#         resultado = True
#     return JsonResponse({'resultado': resultado})


def detectar_par(request):
    par = request.GET.get('a')
    try:
        numero = int(par)
    except (ValueError, TypeError):
        return JsonResponse({'error': 'El parámetro debe ser un número entero'}, status=400)

    resultado = (numero % 2 == 0)
    return JsonResponse({'resultado': resultado})

# def sumar(request):
#     a = float(request.GET.get('a', 0))
#     b = float(request.GET.get('b', 0))
#     resultado = a + b
#     return JsonResponse({'resultado': resultado})

def sumar(request):
    try:
        a = int(request.GET.get('a'))
        b = int(request.GET.get('b'))
    except (ValueError, TypeError):
        return JsonResponse({'error': 'Los parámetros deben ser números enteros'}, status=400)

    resultado = a + b
    return JsonResponse({'resultado': resultado})

def restar(request):
    a = float(request.GET.get('a', 0))
    b = float(request.GET.get('b', 0))
    resultado = a - b
    return JsonResponse({'resultado': resultado})

def multiplicar(request):
    a = float(request.GET.get('a', 0))
    b = float(request.GET.get('b', 0))
    resultado = a * b
    return JsonResponse({'resultado': resultado})

def dividir(request):
    a = float(request.GET.get('a', 0))
    b = float(request.GET.get('b', 1))
    if b == 0:
        return JsonResponse({'error': 'No se puede dividir por cero'}, status=400)
    resultado = a / b
    return JsonResponse({'resultado': resultado})