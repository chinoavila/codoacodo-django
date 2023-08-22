'''
3. Escribir un programa que reciba una cadena de caracteres y devuelva un diccionario con
cada palabra que contiene y la cantidad de veces que aparece (frecuencia).
'''

STR_PALABRAS = "No se que poner acá pero vamos a completar con lo que sale."
list_palabras = STR_PALABRAS.split()
dict_palabras = { palabra.lower(): list_palabras.count(palabra) for palabra in list_palabras }

print("\nEjercicio 3:\n")
print(dict_palabras)
print("\n------------------------\n")
