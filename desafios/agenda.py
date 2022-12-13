#Gestion de una agenda telefonica

agenda = dict()

while(1):
    print("Seleccione alguna de las siguientes opciones:")
    print("1. Añadir una persona a la agenda")
    print("2. Buscar una persona")
    entrada = input("Opción: ")
        
    if(entrada == "1"):
        nombre = input("Ingrese el nombre: ")
        telefono = input("Ingrese el telefono: ")
        print(f'Agendar a {nombre} con el número {telefono}')
        agenda[nombre] = telefono
    elif(entrada == "2"):
        nombre = input("Ingrese el nombre a buscar: ")
        print(f'Buscando a  {nombre}')
        for item in agenda:
            if (item.startswith(nombre)):
                print(f'{item} tiene el número {agenda[item]}')
    else:
        break
