import time
def medir_tiempo(func):
    def wrapper(*args, **kwargs):
        inicio = time.time()  # Tiempo inicial
        resultado = func(*args, **kwargs)  # Ejecutar la función
        fin = time.time()  # Tiempo final
        duracion = fin - inicio  # Duración en segundos
        print(f"Tiempo de ejecución de {func.__name__}: {duracion:.6f} segundos")
        return resultado  # Retornar el resultado de la función
    return wrapper

def sumatoria_div (n):  #buscar divisores de un numero 
    suma = 1
    raiz = int(n ** 0.5)  # Raíz cuadrada para optimizar
    for x in range(2, raiz + 1):
        if n % x == 0:
            complemento = n // x
            suma += x
            if complemento != x:
                suma += complemento
    return suma


def es_primo(n):
    if n <= 1:
        return False  # Los números menores o iguales a 1 no son primos
    if n <= 3:
        return True   # 2 y 3 son primos
    if n % 2 == 0 or n % 3 == 0:
        return False  # Descartar múltiplos de 2 y 3

    i = 5
    while (i * i) <= n:
        if (n % i == 0) or ((n % (i + 2)) == 0):
            return False
        i += 6  # Saltar múltiplos de 2 y 3

    return True


@medir_tiempo
def conjunto_primos(numero):
    # Crear un conjunto para almacenar números primos
    primos = set()
    
    for i in range(2, numero + 1):  # Desde 2 hasta N (inclusive)
        if es_primo(i):
            primos.add(i)  # Si es primo, agregar al conjunto
    
    return primos


conjunto_primos (1000000000000000000)