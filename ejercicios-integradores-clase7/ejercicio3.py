#----------------------------------------------------------------------------------------
# 3. Escribir un programa que reciba una cadena de caracteres y devuelva un diccionario con 
# cada palabra que contiene y la cantidad de veces que aparece (frecuencia).
#----------------------------------------------------------------------------------------

cadena = "No se que poner acá pero vamos a completar con lo que sale."
arreglo_palabras = cadena.split()
diccionario_palabras = { palabra.lower(): arreglo_palabras.count(palabra) for palabra in arreglo_palabras }
print("\nEjercicio 3:\n")
print(diccionario_palabras)
print("\n------------------------\n")