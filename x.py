def sumatoria_div(n):
    divisores = 1
    for x in range(2, (n // 2) + 1):
        if n % x == 0:
            divisores += x
    return divisores


def numeros_sociables(N, rango):
    for i in range(2, N):
        secuencia = []
        numeros_act = set()
        numero_analizar = i

        # Crear la secuencia con un máximo de longitud igual al rango
        for _ in range(rango + 1):  # rango + 1 para verificar el ciclo
            if numero_analizar in numeros_act:
                break  # Si ya está en el set, hemos encontrado un ciclo
            numeros_act.add(numero_analizar)
            secuencia.append(numero_analizar)
            numero_analizar = sumatoria_div(numero_analizar)

        # Comprobar si es un conjunto sociable del rango especificado
        if len(secuencia) == rango + 1 and secuencia[0] == secuencia[-1]:
            print("Conjunto sociable:", secuencia)

n = int (input ("Ingrese un numero: "))
rangee = int (input ("Ingrese un orden social: "))

numeros_sociables (n,rangee)