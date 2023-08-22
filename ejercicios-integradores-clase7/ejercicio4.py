'''
4. Escribir una función que reciba una cadena de caracteres y devuelva un diccionario con cada
palabra que contiene y la cantidad de veces que aparece (frecuencia). Escribir otra función
que reciba el diccionario generado con la función anterior y devuelva una tupla con la
palabra más repetida y su frecuencia.
'''

def convertir_a_diccionario(arg_str):
    '''Devuelve un dict con las palabras y su frecuencia de repetición dentro del parámetro str.'''
    list_palabras = arg_str.split()
    dict_palabras = {palabra.lower(): list_palabras.count(palabra) for palabra in list_palabras}
    return dict_palabras

def palabra_mas_repetida(arg_dict):
    '''Devuelve un tuple con la palabra más repetida y su frecuencia'''
    str_palabra = max(arg_dict, key=arg_dict.get, default=None)
    int_frecuencia = arg_dict.get(palabra, 0)
    return str_palabra, int_frecuencia

STR_PALABRAS = "No se que poner acá pero vamos a completar con lo que sale."
palabras = convertir_a_diccionario(STR_PALABRAS)
palabra, frecuencia = palabra_mas_repetida(palabras)
print("\nEjercicio 4:\n")
print(f'La palabra más repetida es "{palabra}" (frecuencia:{frecuencia}).')
print("\n------------------------\n")
