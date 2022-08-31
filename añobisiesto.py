año=int(input("Ingrese el año para saber si será bisiesto: "))

def bisiesto(año):
    if año % 4 == 0 and (año % 100 !=0 or año % 400 ==0):
        print (" Es bisiesto")
    else :
        print("no es bisiesto")

bisiesto(año)
