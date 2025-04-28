

persona = {
  "nombre": "Juan", 
  "edad": 25, 
  "ciudad": "Madrid"
  }
print(persona["nombre"])  # Imprime "Juan"
print(persona["edad"])    # Imprime 25
print(persona["ciudad"])  # Imprime "Madrid"
"""
keys(): devuelve una vista de todas las claves del diccionario.
values(): devuelve una vista de todos los valores del diccionario.
items(): devuelve una vista de todos los pares clave-valor del diccionario.
update(otro_diccionario): actualiza el diccionario con los pares clave-valor de otro diccionario.
"""
# Ejemplo de uso de keys(), values() e items()

print(persona.keys())    # Imprime dict_keys(["nombre", "edad", "ciudad"])
print(persona.values())  # Imprime dict_values(["Juan", 25, "Madrid"])
print(persona.items())   # Imprime dict_items([("nombre", "Juan"), ("edad", 25), ("ciudad", "Madrid")])

# persona.update se mete un nuevo dato
persona.update({"profesion": "Ingeniero"})
print(persona)  # Imprime {"nombre": "Juan", "edad": 25, "ciudad": "Madrid", "profesion": "Ingeniero"}

# Creacion y operaciones basicas
frutas = {
  "manzana",
  "banana",
  "naranja"
}
numeros = set([1, 2, 3, 4, 5])


conjunto1 = {1, 2, 3}
conjunto2 = {3, 4, 5}


union = conjunto1 | conjunto2
print(union)  # Imprime {1, 2, 3, 4, 5}


interseccion = conjunto1 & conjunto2
print(interseccion)  # Imprime {3}


diferencia = conjunto1 - conjunto2
print(diferencia)  # Imprime {1, 2}


diferencia_simetrica = conjunto1 ^ conjunto2
print(diferencia_simetrica)  # Imprime {1, 2, 4, 5}

"""
add(elemento): agrega un elemento al conjunto.
remove(elemento): elimina un elemento del conjunto. Si el elemento no existe, genera un error.
discard(elemento): elimina un elemento del conjunto si está presente. Si el elemento no existe, no hace nada.
clear(): elimina todos los elementos del conjunto.
"""

frutas = {"manzana", "banana", "naranja"}


frutas.add("pera")
print(frutas)  # Imprime {"manzana", "banana", "naranja", "pera"}


frutas.remove("banana")
print(frutas)  # Imprime {"manzana", "naranja", "pera"}


frutas.discard("uva")
print(frutas)  # Imprime {"manzana", "naranja", "pera"}


frutas.clear()
print(frutas)  # Imprime set()
# tests
persona = {
  "id": 199,
  "nombre": "Juan", 
  "edad": 25, 
  "b-day": "1998-01-01",
  "telefono": "123456789",
  "ciudad": "Madrid"
  }

print(persona.keys())
print(persona.values())


