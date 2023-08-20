#----------------------------------------------------------------------------------------
# 6. Crear una clase llamada Persona. Sus atributos son: nombre, edad y DNI. Construya los 
# siguientes métodos para la clase: 
# Un constructor, donde los datos pueden estar vacíos. 
# Los setters y getters para cada uno de los atributos. Hay que validar las entradas de 
# datos. 
# mostrar(): Muestra los datos de la persona. 
# Es_mayor_de_edad(): Devuelve un valor lógico indicando si es mayor de edad
#----------------------------------------------------------------------------------------

# importo re para validar el DNI utilizando una expresión regular
import re

class Persona():
    def __init__(self, nombre="", edad=0, dni=""):
        self._nombre = nombre
        self._edad = edad
        self._dni = dni

    @property
    def nombre(self):
        return self._nombre

    @nombre.setter
    def nombre(self, nombre_nuevo):
        if nombre_nuevo.replace(" ", "").isalpha():
            self._nombre = nombre_nuevo
        else:
            print("El dato ingresado debe ser una cadena sin números.")

    @property
    def edad(self):
        return self._edad

    @edad.setter
    def edad(self, edad_nuevo):
        if int(edad_nuevo) >= 0:
            self._edad = edad_nuevo
        else:
            print("El dato ingresado debe ser un número entero positivo.")

    @property
    def dni(self):
        return self._dni

    @dni.setter
    def dni(self, dni):
        REGEXP = r'^\d{7,8}$'
        if re.match(REGEXP, dni) is not None:
            self._dni = dni
        else:
            print("El formato del dato ingresado no es correcto.")

    def mostrar(self):
        '''Imprime una cadena formateada con el DNI, Nombre y Edad.'''
        cadena = "DNI: {}, Nombre: {}, Edad: {}. ".format(self._dni, self._nombre, self._edad)
        cadena += 'Mayor de edad' if self.es_mayor_de_edad() else 'Menor de edad.'
        print(cadena)

    def es_mayor_de_edad(self):
        '''Devuelve un Boolean según si la edad del Titular es mayor a 18 años.'''
        return self._edad >= 18


# DESCOMENTAR TODAS LAS LINEAS DE ABAJO PARA PROBAR
# print("\nEjercicio 6:\n")
# objeto_persona = Persona()
# objeto_persona.nombre = "Alejandro Ávila"
# objeto_persona.edad = 29
# objeto_persona.dni = "12345678"
# objeto_persona.mostrar()
# print("\n------------------------\n")