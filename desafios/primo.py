#Determinar si un numero es primo

def es_primo(valor, n=2):
    
    if (n >= valor):
        print(f'{valor} es un número primo')
        return True
    elif (valor % n != 0):
        return es_primo(valor, n+1)
    else:
        print(f'{valor} no es primo, es divisible por {n}')

es_primo(333)
