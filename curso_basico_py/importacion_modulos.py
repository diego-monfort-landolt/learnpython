import math
from math import sqrt
import mi_modulo
import operaciones
import utilidades


resultado = math.sqrt(25)
print(resultado)  # Imprime 5.0

resultado = sqrt(25)
print(resultado)  # Imprime 5.0


import random
import datetime

"""
Math
Proporciona funciones matemáticas, como sqrt() (raíz cuadrada), sin() (seno), cos() (coseno), entre otras.
Random
Ofrece funciones para generar números aleatorios, como random() (número aleatorio entre 0 y 1), randint() (número entero aleatorio en un rango), entre otras.
DateTime
Permite trabajar con fechas y horas, como datetime.now() (fecha y hora actual), datetime.date() (fecha), datetime.time() (hora), entre otras.
"""


numero_aleatorio = random.randint(1, 10)
print(numero_aleatorio)  # Imprime un número entero aleatorio entre 1 y 10


fecha_actual = datetime.datetime.now()
print(fecha_actual)  # Imprime la fecha y hora actual

# import von einem doc -func -import und der name des modules
mi_modulo.saludar("Juan")  # Imprime "Hola, Juan!"
resultado = mi_modulo.calcular_suma(5, 3)
print(resultado)  # Imprime 8


resultado = operaciones.sumar(5, 3)
utilidades.imprimir_mensaje(f"El resultado de la suma es: {resultado}")


nombre = utilidades.obtener_nombre_usuario()
utilidades.imprimir_mensaje(f"Hola, {nombre}!")