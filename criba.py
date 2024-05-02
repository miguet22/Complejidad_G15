def conjunto_primos(numero):
    primos = [True] * (numero + 1)  # Inicialmente, asumimos que todos son primos
    primos[0] = primos[1] = False  # 0 y 1 no son primos

    # Comenzamos desde el primer número primo, que es 2
    p = 2
    while p * p <= numero:  # Solo necesitamos llegar hasta la raíz cuadrada de n
        if primos[p]:  # Si el número es considerado primo
            # Marcamos todos sus múltiplos como no primos
            for i in range(p * p, numero + 1, p):
                primos[i] = False
        p += 1

    # Recopilamos todos los números que siguen siendo True
    lista_primos = [x for x in range(numero + 1) if primos[x]]
    return lista_primos