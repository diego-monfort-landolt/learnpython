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