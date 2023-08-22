'''
7. Crea una clase llamada Cuenta que tendrá los siguientes atributos: titular (que es una
persona) y cantidad (puede tener decimales). El titular será obligatorio y la cantidad es
opcional. Crear los siguientes métodos para la clase:
Un constructor, donde los datos pueden estar vacíos.
Los setters y getters para cada uno de los atributos. El atributo no se puede modificar
directamente, sólo ingresando o retirando dinero.
mostrar(): Muestra los datos de la cuenta.
ingresar(cantidad): se ingresa una cantidad a la cuenta, si la cantidad introducida es
negativa, no se hará nada.
retirar(cantidad): se retira una cantidad a la cuenta. La cuenta puede estar en números rojos.
'''

from ejercicio6 import Persona
class Cuenta():
    '''
    Clase para representar una cuenta bancaria.

    Atributos
    ----------
    titular : Persona
    cantidad : float

    Métodos
    -------
    mostrar():
        Imprime los datos de la cuenta.
    ingresar(cantidad):
        Permite adicionar el valor del argumento al valor actual \
        del atributo "cantidad".
    retirar(cantidad):
        Permite sustraer el valor del argumento del valor actual \
        del atributo "cantidad".
    '''

    def __init__(self, nombre, edad, dni, cantidad = 0):
        '''
        Constructor: inicializa los atributos básicos de la persona.

        El argumento "titular" es obligatorio, debiendo pasarle un \
        objeto de clase Persona a partir de los parámetros recibidos \
        en los argumentos nombre, edad y dni.
        
        El argumento "cantidad" es opcional y de tipo float.
        '''
        self._titular = Persona(nombre, edad, dni)
        self._cantidad = 0
        if cantidad > 0:
            self.ingresar(cantidad)

    @property
    def titular(self):
        '''
        Obtener o establecer valor de atributo "titular".

        Al establecer un nuevo valor, se debe pasarle \
        un objeto de clase Persona.
        '''
        return self._titular

    @titular.setter
    def titular(self, nuevo_titular):
        if isinstance(nuevo_titular,Persona):
            self._titular = nuevo_titular
        else:
            print("El dato ingresado no corresponde \
                  a una instancia de la clase Persona.")

    @property
    def cantidad(self):
        '''
        Obtener valor de atributo "cantidad". \
        Propiedad de solo lectura.
        '''
        return self._cantidad

    def mostrar(self):
        '''Imprime una cadena formateada con el Titular y la Cantidad de la cuenta.'''
        print(f"Titular: {self._titular.nombre}, Cantidad: {self.cantidad}. ")

    def ingresar(self, cantidad):
        '''
        Permite adicionar el valor del argumento al valor actual \
        del atributo "cantidad".
        '''
        self._cantidad += float(cantidad)
        print(f"Se ingresó {cantidad}.")

    def retirar(self, cantidad):
        '''
        Permite sustraer el valor del argumento del valor actual \
        del atributo "cantidad".
        '''
        self._cantidad -= float(cantidad)
        print(f"Se retiró {cantidad}.")


# DESCOMENTAR TODAS LAS LINEAS DE ABAJO PARA PROBAR
# print("\nEjercicio 7:\n")
# objeto_cuenta = Cuenta("Alejandro Ávila",29,"12345678")
# objeto_cuenta.mostrar() # muestra la cuenta vacía
# objeto_cuenta.ingresar(1000)
# objeto_cuenta.mostrar() # debe mostrar 1000 en la cuenta
# objeto_cuenta.retirar("300")
# objeto_cuenta.mostrar() # debe mostrar 700 en la cuenta
# print("\n------------------------\n")
