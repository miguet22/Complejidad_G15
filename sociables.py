def sumatoria_div (n):
    divisores = 1
    for x in range (2,(n//2)+1):
        
        if (n % x == 0) :
            divisores = divisores + x

    return divisores


def numeros_sociables (N,rango):
    for i in range (2,N):
    
        secuencia = []
        numeros_act = set ()
        numeros_act.add (i)
        secuencia.append (i)

        
        sumatoria = sumatoria_div (i)
    
        numeros_act.add(sumatoria)
        secuencia.append (sumatoria)
        
        numero_analizar = sumatoria
        veces = 1

        print (f"Rango { rango}")
        while veces <= rango :
            
            divisores_actual = 1
            
            for k in range (2,( (numero_analizar//2) + 1 )):
                
                if numero_analizar % k == 0:
                    divisores_actual = divisores_actual + k
        
            numeros_act.add (divisores_actual)
            secuencia.append (divisores_actual)
            numero_analizar = divisores_actual
            veces = veces + 1

        print (secuencia)
        
        if secuencia[0] == secuencia[rango-1] and  ( (len (numeros_act)) == rango):
            print (f"Conjunto social: {numeros_act}")
    
        
n = int (input ("Ingrese un numero: "))
rangee = int (input ("Ingrese un orden social: "))

numeros_sociables (n,rangee)
            

        
        
    