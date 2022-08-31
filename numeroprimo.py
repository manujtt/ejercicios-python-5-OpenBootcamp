numero= int(input("Ingresa el número entero: "))
esPrimo= True
for i in range(2,numero):
        if numero%i==0:
           esPrimo = False
           break

if esPrimo:
    print("Es numero Primo")
else:
    print("No es numero primo")
            
        
    
