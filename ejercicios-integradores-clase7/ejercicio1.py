#----------------------------------------------------------------------------------------
# 1. Escribir una función que calcule el máximo común divisor entre dos números. 
#----------------------------------------------------------------------------------------

from math import gcd

def maximo_comun_divisor(x, y):
    '''Devuelve un str formateado indicando el MCD entre dos valores int.'''
    return "El máximo común divisor entre {} y {} es: {}.".format(x, y, gcd(x,y))

print("\nEjercicio 1:\n")
print(maximo_comun_divisor(5,3))
print("\n------------------------\n")