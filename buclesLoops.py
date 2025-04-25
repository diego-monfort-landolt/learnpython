"""
for variable in secuencia:

Bloque de código a repetir
instrucciones

"""

frutas = ["manzana", "banana", "naranja"]


for fruta in frutas:
    print(fruta)
"""
    En este ejemplo, el bucle for itera sobre la lista frutas. En cada iteración, la variable fruta toma el valor de un elemento de la lista, y se ejecuta el bloque de código dentro del bucle. En este caso, se imprime cada fruta en una línea separada.
"""

# While

"""
  while condicion:
  Bloque de código a repetir instrucciones
"""

# se ejecuta sin parar

# while contador < 5:

#     print(contador)
#     contador += 1
#     break
    
# print("\nNumeros del 1 al 5 multiplicados por 2 con bucle while: ")

contador = 0
while True:

    print(contador)
    contador += 1
    
    if contador == 5:
        break
    
zähler = 1
while zähler <= 10:
    print(zähler)
    zähler += 1
    
# ejemplo sumar 1 10
suma = 0
for numero in range(1, 11):
    suma += numero
    print(f"La suma de los números del 1 al 10 es: {suma}")
    
numero = int(input("Ingresa un número: "))
# Usar un bucle for para generar la tabla
print(f"Tabla de multiplicar del {numero}:")
for i in range(1, 11):
    resultado = numero * i
    print(f"{numero} x {i} = {resultado}")
#numero inicial
numero_inicial = 1
print(f'Numeros pares del 1 al 20:')
while numero_inicial <= 20:
    if numero_inicial % 2 == 0:
        print(numero_inicial)
    else:
        print(f"{numero_inicial} no es par")
    numero_inicial += 1
    
    for i in range(1, 21):
        if i % 3 == 0 and i % 5 == 0:
            print('Fizzbuzz')
        elif i % 3 == 0:
            print('Fizz')
        elif i % 5 == 0:
            print('Buzz')
        else: 
            print(i)