#----------------------------------------------------------------------------------------
# 7. Crea una clase llamada Cuenta que tendrá los siguientes atributos: titular (que es una 
# persona) y cantidad (puede tener decimales). El titular será obligatorio y la cantidad es 
# opcional. Crear los siguientes métodos para la clase: 
# Un constructor, donde los datos pueden estar vacíos. 
# Los setters y getters para cada uno de los atributos. El atributo no se puede modificar 
# directamente, sólo ingresando o retirando dinero. 
# mostrar(): Muestra los datos de la cuenta. 
# ingresar(cantidad): se ingresa una cantidad a la cuenta, si la cantidad introducida es 
# negativa, no se hará nada. 
# retirar(cantidad): se retira una cantidad a la cuenta. La cuenta puede estar en números rojos. 
#----------------------------------------------------------------------------------------

from ejercicio6 import Persona

class Cuenta():

    def __init__(self, titular):
        self._titular = titular
        self._cantidad = 0

    @property
    def titular(self):
        return self._titular
    
    @titular.setter
    def titular(self, nuevo_titular):
        self._titular = nuevo_titular

    @property
    def cantidad(self):
        return self._cantidad

    def mostrar(self):
        '''Imprime una cadena formateada con el Titular y la Cantidad de la cuenta.'''
        print("Titular: {}, Cantidad: {}. ".format(self._titular._nombre, self.cantidad))

    def ingresar(self, cantidad):
        self._cantidad += float(cantidad)
        print("Se ingresó {}.".format(cantidad))

    def retirar(self, cantidad):
        self._cantidad -= float(cantidad)
        print("Se retiró {}.".format(cantidad))


# DESCOMENTAR TODAS LAS LINEAS DE ABAJO PARA PROBAR
# print("\nEjercicio 7:\n")
# objeto_persona = Persona("Alejandro Ávila",29,"12345678")
# objeto_cuenta = Cuenta(objeto_persona)
# objeto_cuenta.mostrar() # muestra la cuenta vacía
# objeto_cuenta.ingresar(1000)
# objeto_cuenta.mostrar() # debe mostrar 1000 en la cuenta
# objeto_cuenta.retirar("300")
# objeto_cuenta.mostrar() # debe mostrar 700 en la cuenta
# print("\n------------------------\n")