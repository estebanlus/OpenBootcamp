#Determinar si un año es bisiesto

def esBisiesto(anio):
    if anio % 4 == 0:
        return True
    else:
        return False

if esBisiesto(2020):
    print("Es bisiesto")
else:
    print("No es bisiesto")
