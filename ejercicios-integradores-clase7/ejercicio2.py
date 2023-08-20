#----------------------------------------------------------------------------------------
# 2. Escribir una función que calcule el mínimo común múltiplo entre dos números
#----------------------------------------------------------------------------------------

from math import lcm

def minimo_comun_multiplo(x, y):
    '''Devuelve un str formateado indicando el MCM entre dos valores int.'''
    return "El mínimo común múltiplo entre {} y {} es: {}.".format(x, y, lcm(x,y))

print("\nEjercicio 2:\n")
print(minimo_comun_multiplo(5,3))
print("\n------------------------\n")