nombre = 'Diego'
bienvenida = f'Hola {nombre} espero que estes bien! '
del nombre
#"Diego" mit in ist es drin und mit not in es falso
print("Diego" not in bienvenida)

myvariable = 'Diego dice que '
new_variable = 'Python es genial'
end_var = '!'
print(myvariable + new_variable + end_var)
print(type(print(myvariable + new_variable + end_var))) # Tipo 'NoneType'


# Funciones del sistema
print(len(bienvenida)) # Imprime la longitud de la cadena
print(bienvenida.upper()) # Imprime la cadena en mayúsculas 
print(bienvenida.lower()) # Imprime la cadena en minúsculas
print(bienvenida.strip()) # Elimina los espacios en blanco al principio y al final de la cadena
print(bienvenida.replace('Diego', 'Andres')) # Reemplaza 'Diego'
print(bienvenida.split()) # Divide la cadena en una lista de palabras

# inputs
first_name = input('¿Cuál es tu nombre? ')
age = input('¿Cuántos años tienes? ')
locaation = input('¿Dónde vives? ')
print(f'Hola {first_name}, tienes {age} años y vives en {locaation}.') 

# cmbios tipos
name = age
name = 'Diego'

age = 34
print(name)
print(age)

# Forzamos el tipo 
address: str = 'Calle 123'
address: int = 123
print(type(address))

nombre = "Juan"
edad = 25
altura = 1.75
es_estudiante = True