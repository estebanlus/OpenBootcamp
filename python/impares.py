#Obtener los numeros impares de una lista
import functools

prueba = list(range(100))

#resultado = [item for item in prueba if (item % 2) != 0]

resultado = list(filter(lambda x: x % 2 != 0, prueba))
print(resultado)

sumatoria = functools.reduce(lambda a, b: a+b, resultado)
print(f'La sumatoria es: {sumatoria}')
