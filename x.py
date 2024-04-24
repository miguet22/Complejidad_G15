x = int (input ("Ingrese un numero: "))
print (x//2)
divisores = 0
for i in range (1,(x//2)+1):
    print (f"pasada : {i}")
    if (x % i == 0) :
        divisores = divisores + i

print (divisores)