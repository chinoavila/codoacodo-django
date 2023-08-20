#----------------------------------------------------------------------------------------
# 4. Escribir una función que reciba una cadena de caracteres y devuelva un diccionario con cada 
# palabra que contiene y la cantidad de veces que aparece (frecuencia). Escribir otra función 
# que reciba el diccionario generado con la función anterior y devuelva una tupla con la 
# palabra más repetida y su frecuencia. 
#----------------------------------------------------------------------------------------

def convertir_a_diccionario(cadena):
    '''Devuelve un dict con las palabras y su frecuencia de repetición dentro del parámetro str.'''
    arreglo_palabras = cadena.split()
    diccionario_palabras = {palabra.lower(): arreglo_palabras.count(palabra) for palabra in arreglo_palabras}
    return diccionario_palabras

def palabra_mas_repetida(diccionario):
    '''Devuelve un tuple con la palabra más repetida y su frecuencia'''
    palabra = max(diccionario, key=diccionario.get, default=None)
    frecuencia = diccionario.get(palabra, 0)
    return palabra, frecuencia

cadena = "No se que poner acá pero vamos a completar con lo que sale."
diccionario_palabras = convertir_a_diccionario(cadena)
palabra, frecuencia = palabra_mas_repetida(diccionario_palabras)
print("\nEjercicio 4:\n")
print('La palabra más repetida es "{}" (frecuencia:{}).'.format(palabra, frecuencia))
print("\n------------------------\n")

