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

@medir_tiempo
def numeros_sociables (N,rango):
    conjuntos_encontrados=set ()

    for i in range (2,N):

        encontrado = False


        if len (conjuntos_encontrados) > 0 :
            for internos in conjuntos_encontrados: #para evitar buscar un conjunto ya encontrado
                if i in internos: 
                    encontrado= True
                    break

        if  not encontrado:

            secuencia = []
            conjunto = set ()
            conjunto.add (i)  #posible conjunto social
            secuencia.append (i)  #array con numeros



            sumatoria = sumatoria_div (i)

            conjunto.add(sumatoria)
            secuencia.append (sumatoria)

            numero_analizar = sumatoria
            veces = 1

            while veces <= rango :


                divisores_actual = 1
                fin = (numero_analizar//2) + 1

                for k in range (2,fin):

                    if numero_analizar % k == 0:
                        divisores_actual = divisores_actual + k

                conjunto.add (divisores_actual)
                secuencia.append (divisores_actual)
                numero_analizar = divisores_actual

                veces = veces + 1



            if secuencia[0] == secuencia[rango] and  ( (len (conjunto)) == rango):
                print (f"*Conjunto social: {secuencia [0:rango]}")
                conjunto = frozenset (conjunto)
                conjuntos_encontrados.add (conjunto)


n = int (input ("Ingrese un numero tope: "))
rangee = int (input ("Ingrese un orden social: "))

print ("Conjuntos sociales del orden elegido: ")
numeros_sociables (n,rangee)