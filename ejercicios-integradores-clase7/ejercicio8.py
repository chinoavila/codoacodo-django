#----------------------------------------------------------------------------------------
# 8. Vamos a definir ahora una “Cuenta Joven”, para ello vamos a crear una nueva clase 
# CuantaJoven que deriva de la clase creada en el punto 7. Cuando se crea esta nueva clase, 
# además del titular y la cantidad se debe guardar una bonificación que estará expresada en 
# tanto por ciento. Crear los siguientes métodos para la clase: 
# Un constructor. 
# Los setters y getters para el nuevo atributo. 
# En esta ocasión los titulares de este tipo de cuenta tienen que ser mayor de edad, por lo 
# tanto hay que crear un método es_titular_valido() que devuelve verdadero si el titular es 
# mayor de edad pero menor de 25 años y falso en caso contrario. 
# Además, la retirada de dinero sólo se podrá hacer si el titular es válido. 
# El método mostrar() debe devolver el mensaje de “Cuenta Joven” y la bonificación de la cuenta. 
#----------------------------------------------------------------------------------------

# Importo las clases Cuenta y Persona del ejercicio 6 y 7.
# Desde el archivo "ejericio7" se llama al archivo "ejercicio8"
# Por lo que importando el primero tengo acceso al código de ambos archivos
from ejercicio7 import Cuenta, Persona

class CuentaJoven(Cuenta):

    def __init__(self, titular, bonificacion = 0.00):
        super().__init__(titular)
        self._bonificacion = bonificacion

    @property
    def bonificacion(self):
        return float(self._bonificacion)
    
    @bonificacion.setter
    def bonificacion(self, nueva_bonificacion):
        if 0 <= float(nueva_bonificacion) <= 100:
            self._bonificacion = nueva_bonificacion
        else:
           print("El dato ingresado debe ser un número real mayor o igual a cero expresado en porcentaje: parte entera de 0-100 y 2 decimales.")

    def es_titular_valido(self):
        '''Devuelve un Boolean según si el Titular tiene entre 18 y 25 años de edad.'''
        return self._titular.es_mayor_de_edad() and self._titular.edad < 25
    
    def retirar(self, cantidad):
        '''
        Valida que el Titular tenga la edad permitida para hacer un retiro.

        Implementa el método "retirar()" de la clase "Cuenta".

        Si el Titular no es válido, imprime una cadena indicando el error.
        '''
        if self.es_titular_valido():
            super().retirar(cantidad)
        else:
            print("No se puede realizar el retiro. El titular ingresado no es válido.")

    def _mostrar(self):
        '''Imprime una cadena formateada con el la leyenda "Cuenta Joven. Bonificación: XX.XX%.".'''
        print("Cuenta Joven. Bonificación: {:.2f}%.".format(self._bonificacion))


# DESCOMENTAR TODAS LAS LINEAS DE ABAJO PARA PROBAR
print("\nEjercicio 8:\n")
objeto_persona = Persona("Alejandro Ávila", 29, "12345678")
objeto_cuenta_joven = CuentaJoven(objeto_persona, 25.3)
objeto_cuenta_joven.titular.mostrar() # muestro los datos del Titular
objeto_cuenta_joven._mostrar() # muestro la bonificación de la cuenta
objeto_cuenta_joven.ingresar(1000) # hago un ingreso
objeto_cuenta_joven.mostrar() # muestro el saldo actual de la cuenta
objeto_cuenta_joven.retirar(200) # intento retirar 200 (arroja Titular inválido por ser mayor de 25)
otro_objeto_persona = Persona("Javier Ávila", 23, "87654321") # creo otra persona con una edad válida
objeto_cuenta_joven.titular = otro_objeto_persona  # cambio la titularidad de la cuenta
objeto_cuenta_joven.bonificacion = 26 # cambio el valor de la bonificación
objeto_cuenta_joven.titular.mostrar() # compruebo que se actualizaron los datos del Titular
objeto_cuenta_joven._mostrar() # compruebo si la bonificacion se modificó
objeto_cuenta_joven.retirar(100) # intento nuevamente hacer un retiro
objeto_cuenta_joven.mostrar() # muestro el saldo final de la cuenta

print("\n------------------------\n")