'''
6. Crear una clase llamada Persona. Sus atributos son: nombre, edad y DNI. Construya los 
siguientes métodos para la clase: 
Un constructor, donde los datos pueden estar vacíos. 
Los setters y getters para cada uno de los atributos. Hay que validar las entradas de datos.
mostrar(): Muestra los datos de la persona.
Es_mayor_de_edad(): Devuelve un valor lógico indicando si es mayor de edad.

'''

# importo re para validar el DNI utilizando una expresión regular
import re

class Persona():
    '''
    Clase para representar una persona.

    Atributos
    ----------
    nombre : str
    edad : int
    dni : str

    Métodos
    -------
    mostrar():
        Imprime los datos de la persona.
    es_mayor_de_edad():
        Retorna Boolean si la persona cumple con la mayoría de edad.
    '''

    def __init__(self, nombre="", edad=0, dni=""):
        '''Constructor: inicializa los atributos básicos de la persona.'''
        self.nombre = nombre
        self.edad = edad
        self.dni = dni

    @property
    def nombre(self):
        ''' 
        Obtener o establecer valor de atributo "nombre".

        Al establecer un nuevo valor, se verifica que el \
        valor sea de tipo str y no contenga números.
        '''
        return self._nombre

    @nombre.setter
    def nombre(self, nombre_nuevo):
        if nombre_nuevo == "" or nombre_nuevo.replace(" ", "").isalpha():
            self._nombre = nombre_nuevo
        else:
            print("El dato ingresado debe ser una cadena sin números.")

    @property
    def edad(self):
        ''' 
        Obtener o establecer valor de atributo "edad".

        Al establecer un nuevo valor, se verifica que el \
        valor sea de tipo int y que no sea menor a cero.
        '''
        return self._edad

    @edad.setter
    def edad(self, edad_nuevo):
        if int(edad_nuevo) >= 0:
            self._edad = edad_nuevo
        else:
            print("El dato ingresado debe ser un número entero positivo.")

    @property
    def dni(self):
        ''' 
        Obtener o establecer valor de atributo "dni".

        Al establecer un nuevo valor, se verifica que el \
        valor sea de tipo str y que el formato del \
        mismo sea de 7 a 8 digitos decimales.
        '''
        return self._dni

    @dni.setter
    def dni(self, dni):
        regex = r'^\d{7,8}$'
        if dni == "" or re.match(regex, dni) is not None:
            self._dni = dni
        else:
            print("El formato del dato ingresado no es correcto.")

    def mostrar(self):
        '''Imprime una cadena formateada con el DNI, Nombre y Edad.'''
        cadena = f"DNI: {self._dni}, Nombre: {self._nombre}, Edad: {self._edad}. "
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
