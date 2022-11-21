#Validar la hora de ir a casa

import time

hora = time.strftime('%H')
minutos = time.strftime('%M')

if int(hora) >= 19:
    print("Ya es hora de ir a casa")
else:
    hres = 18 - int(hora)
    mres = 59 - int(minutos)
    print("Todavia quedan", hres, "horas y" ,mres, "minutos para ir a casa")
