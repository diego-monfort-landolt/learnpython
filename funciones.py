def saludo():
    print("¡Hola, mundo!")


saludo()  # Imprime "¡Hola, mundo!"


def saludo(nombre):
    print(f"¡Hola, {nombre}!")
saludo("Juan")  # Imprime "¡Hola, Juan!"

def suma(a, b):
    return a + b


resultado = suma(3, 4)
print(resultado)  # Imprime 7

cuadrado = lambda x: x ** 2
print(cuadrado(5))  # Imprime 25

def funcion():
    variable_local = 10
    print(variable_local)  # Accesible dentro de la función


variable_global = 20


def funcion2():
    print(variable_global)  # Accesible desde cualquier lugar


funcion()  # Imprime 10
funcion2()  # Imprime 20
print(variable_global)  # Imprime 20
print(variable_local)  # Genera un error, la variable no está definida en este alcance.