def sumatoria_div (n):
    divisores = 0
    for x in range (1,(n//2)+1):
        
        if (n % x == 0) :
            divisores = divisores + x

    return divisores


def numeros_sociables (N,rango):
    for i in range (2,N):
    
        
        numeros_act = [] 
        numeros_act.append (i)

        
        suma = sumatoria_div (i)
        
        
        numeros_act.append (suma)
        
        veces = 1

        while veces <= rango :
            
            divisores_actual = 1
            
            for k in range (2,numeros_act[veces]):
                
                if numeros_act [veces] % k == 0:
                    divisores_actual = divisores_actual + k
        
            numeros_act.append (divisores_actual)
            veces = veces + 1
            
        
        if numeros_act [0] == numeros_act [rango]:
            
            print (f"Conjunto social: {numeros_act}")
    
        
n = int (input ("Ingrese un numero: "))
rangee = int (input ("Ingrese un orden social: "))

numeros_sociables (n,rangee)
            

        
        
    