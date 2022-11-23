#Ordenar una lista de paises ingresadas por el usuario
resultado = set()

entrada = input("Ingrese una lista de paises separados por coma (,): ")

paises = entrada.split(', ')

for item in paises:
    resultado.add(item.capitalize())

resPais = list()
for item in resultado:
    resPais.append(item)

resPais.sort()

print(list(resPais))
