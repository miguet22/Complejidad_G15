import time
import math

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
    raiz = int(math.isqrt(n))  # Raíz cuadrada para optimizar
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



@medir_tiempo    
def numeros_sociables (N,rango):
    conjuntos_encontrados=set ()
    
    c_primos = conjunto_primos (N)
    for i in range (2,N):
        if any(i in internos for internos in conjuntos_encontrados):
            continue  # Si el número está en un conjunto, saltarlo

        

        secuencia = []
        conjunto = set ()
        conjunto.add (i)  #posible conjunto social
        secuencia.append (i)  #array con numeros

        sumatoria = sumatoria_div (i)
        
        if sumatoria not in c_primos:
            
            conjunto.add(sumatoria)
            secuencia.append (sumatoria)

            numero_analizar = sumatoria
            

            ciclo_invalido = False
            
            for _ in range(1, rango):  # Cambiar de `veces` a un bucle fijo
                sumatoria = sumatoria_div(numero_analizar)
                
                if sumatoria in c_primos:
                    ciclo_invalido = True
                    break  # Si es primo, el ciclo no es válido
                
                conjunto.add(sumatoria)
                secuencia.append(sumatoria)
                numero_analizar = sumatoria

            if not ciclo_invalido:
                
                if secuencia[0] == secuencia[rango] and  ( (len (conjunto)) == rango):
                    print (f"*Conjunto social: {secuencia [0:rango]}")
                    conjunto = frozenset (conjunto)
                    conjuntos_encontrados.add (conjunto)

n = int (input ("Ingrese un numero tope: "))
rangee = int (input ("Ingrese un orden social: "))

print ("Conjuntos sociales del orden elegido: ")
numeros_sociables (n,rangee)