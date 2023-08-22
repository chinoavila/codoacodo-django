'''
----------------------------------------------------------------------------------------
 2. Escribir una función que calcule el mínimo común múltiplo entre dos números
----------------------------------------------------------------------------------------
'''

from math import lcm

def minimo_comun_multiplo(arg_x, arg_y):
    '''Devuelve un str formateado indicando el MCM entre dos valores int.'''
    return f"El mínimo común múltiplo entre {arg_x} y {arg_y} es: {lcm(arg_x, arg_y)}."

print("\nEjercicio 2:\n")
print(minimo_comun_multiplo(5, 3))
print("\n------------------------\n")
