def numerosSociables (list):
    sumasdivi = []
    
    for i in range (2,10900):  #recorrer numeros del 2 a 29
        #recorrer divisores de ese numero i
        
        numero = i
        divisores = []
        for j in range (i+i):
            
            if j > 0:
                if (numero % j == 0):
                    divisores.append(j) 
            

        suma=1
        for k in range (1,len(divisores)-1):  #no nos fijamos el divisor como su mismo numero
            suma = suma + divisores [k]
        
        if numero == suma:
            
            list.append (numero)  # append de los perfectos
            

        sumasdivi.append (suma)
        # busqueda de amigos, orden 3

        for p in range (len(sumasdivi)):
            if sumasdivi [p] == numero:
                
                if suma == p+2:
                    if p+2 != numero:  #append de los que son amigos
                        
                        list.append (numero)
                        list.append (p+2)

    return list

numsoc = []
print (numerosSociables (numsoc))