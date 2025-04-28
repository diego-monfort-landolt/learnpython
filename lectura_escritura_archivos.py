"""
Para leer el contenido de un archivo, primero debemos abrirlo utilizando la función open() en modo de lectura ("r"). Luego, podemos leer el contenido del archivo utilizando métodos como read() o readlines().
"""

archivo = open("datos.txt", "r")
contenido = archivo.read()
print(contenido)
archivo.close()
"""
Para escribir datos en un archivo, lo abrimos en modo de escritura ("w") utilizando la función open(). Si el archivo no existe, se creará automáticamente. Si el archivo ya existe, su contenido se sobrescribirá.
"""
archivo = open("datos.txt", "w")
archivo.write("Hola, un Test Nuevo!")
archivo.write("\nEste es un nuevo contenido.")
archivo.close()

# Es importante cerrar siempre los archivos después de utilizarlos para liberar los recursos del sistema. -archivo.close()

# En este caso, el archivo se abre utilizando la declaración with y se cierra automáticamente una vez que se sale del bloque with, incluso si ocurre una excepción.
with open("datos.txt", "r") as archivo:
    contenido = archivo.read()
    print(contenido)
    