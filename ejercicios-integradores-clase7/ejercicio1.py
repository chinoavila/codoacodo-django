'''
----------------------------------------------------------------------------------------
 1. Escribir una función que calcule el máximo común divisor entre dos números. 
----------------------------------------------------------------------------------------
'''

from math import gcd

def maximo_comun_divisor(arg_x, arg_y):
    '''Devuelve un str formateado indicando el MCD entre dos valores int.'''
    return f"El máximo común divisor entre {arg_x} y {arg_y} es: {gcd(arg_x, arg_y)}."

print("\nEjercicio 1:\n")
print(maximo_comun_divisor(5, 3))
print("\n------------------------\n")
