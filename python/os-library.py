#Imprimir todos los ficheros existentes en la carpeta de Descargas

import os

ruta = '/Users/estebanlusbietti/Downloads'
listaArchivos = os.scandir(ruta)

for item in listaArchivos:
    if item.is_file():
        print(f'{item.name} es un archivo')
