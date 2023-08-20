#----------------------------------------------------------------------------------------
# 5. Sabiendo que ValueError es la excepción que se lanza cuando no podemos convertir una 
# cadena de texto en su valor numérico, escriba una función get_int() que lea un valor entero 
# del usuario y lo devuelva, iterando mientras el valor no sea correcto. Intente resolver el 
# ejercicio tanto de manera iterativa como recursiva. 
#----------------------------------------------------------------------------------------

def get_int():
    '''Solicita un número entero al usuario e imprime una cadena formateada indicando su valor.'''
    numero_entero = int(input("Por favor, ingrese un número entero:"))
    print("\nEl número ingresado es {}.\n".format(numero_entero))

def get_int_iterativa():
    '''Solicita un valor al usuario y valida que éste sea un número entero (emulando un bucle Do While).'''
    while True:
        try:
            get_int()
            break
        except ValueError:
            print("El valor ingresado no es un número entero. Reintentar...")

def get_int_recursiva():
    '''Solicita un valor al usuario y valida que sea un número entero (aplicando recursividad).'''
    try:
        get_int()
    except ValueError:
        print("El valor ingresado no es un número entero. Reintentar...")
        return get_int_recursiva()

print("\nEjercicio 5:\n")
print("Forma iterativa:\n")
get_int_iterativa()
print("Forma recursiva:\n")
get_int_recursiva()

# ***DISCULPAS POR ADELANTADO POR DESVIARME DE LA CONSIGNA***
# A modo de práctica, tomé la función recursiva y apliqué un decorador
# (no pido puntos extras jaja es sólo práctica)

def validacion_recursiva(func):
    '''Aplica recursividad a función que genere una excepción por ValueError.'''
    def wrapper():
        try:
            return func()
        except ValueError:
            print("El valor ingresado no es un número entero. Reintentar...")
            return wrapper()  # Llamada recursiva para reintentar
    return wrapper

@validacion_recursiva
def get_int_recursiva_decorada():
    '''Solicita un valor al usuario y valida que sea un número entero (aplicando recursividad).'''
    get_int()

print("Forma recursiva con decorador (debería tener el mismo resultado anterior):\n")
get_int_recursiva_decorada()
print("\n------------------------\n")

# Agradecería una devolución y recomendación de ésto último (perdón de nuevo)
# porque aún no lo apliqué en proyectos, pero me interesa hacerlo a futuro
# ya que considero que es muy útil para modularizar funciones "genéricas"