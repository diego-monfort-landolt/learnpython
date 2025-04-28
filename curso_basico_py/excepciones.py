"""
Try
El bloque try contiene el código que puede generar una excepción. Si ocurre una excepción dentro del bloque try, el flujo de ejecución se transfiere al bloque except correspondiente.
"""
try:
    # Código que puede generar una excepción
    resultado = 10 / 0  # División por cero
    print(resultado)
except ZeroDivisionError:
    print("Error: División por cero")
    
"""
Except
El bloque except especifica el tipo de excepción que se desea capturar y manejar. Puedes tener múltiples bloques except para manejar diferentes tipos de excepciones.
"""
try:
    # Código que puede generar una excepción
    resultado = 10 / 0  # División por cero
    print(resultado)
except ZeroDivisionError:
    print("Error: División por cero")
except ValueError:
    print("Error: Valor inválido")
    
"""
Finally
El bloque finally es opcional y se ejecuta siempre, independientemente de si ocurrió una excepción o no. Se utiliza comúnmente para realizar tareas de limpieza o liberación de recursos
"""

try:
    # Código que puede generar una excepción
    archivo = open("archivo.txt", "r")
    # Realizar operaciones con el archivo
except FileNotFoundError:
    print("Error: Archivo no encontrado")
finally:
    archivo.close()  # Cerrar el archivo siempre, incluso si ocurre una excepción
"""
Excepciones personalizadas
Además de las excepciones incorporadas en Python, también puedes crear tus propias excepciones personalizadas. Esto es útil cuando deseas manejar situaciones específicas de tu programa.

Para crear una excepción personalizada, debes crear una clase que herede de la clase base Exception o de una de sus subclases.
"""

def funcion():
    # Código que puede generar una excepción personalizada
    if condicion: 
        raise Exception("Descripción del error")
try:
    funcion()
except Exception as e:
    print(f"Error: {str(e)}")
