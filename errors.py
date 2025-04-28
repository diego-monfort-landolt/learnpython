def mi_funcion(): # Falta los dos puntos
    print("Hola")
"""
  Ocurre cuando el código no sigue las reglas de sintaxis de Python, como olvidar dos puntos después de una declaración de función o un bucle.
"""

print(variable_no_definida) # Ocurre cuando se hace referencia a una variable o función que no ha sido definida.

# Error de tipo
resultado = 5 + "10" # Ocurre cuando se intenta realizar una operación entre tipos de datos incompatibles, como sumar un número y una cadena.
# Esto generará un TypeError porque no se puede sumar un entero y una cadena.

# Error de indice
lista = [1, 2, 3]
print(lista[3])  # Ocurre cuando se intenta acceder a un índice fuera del rango válido de una lista o secuencia
# En este caso, la lista tiene índices 0, 1 y 2, por lo que el índice 3 está fuera de rango.
# Esto generará un IndexError.