# IF - IF-Else
edad = 18
if edad >= 18:
    print("Eres mayor de edad")
else:
    print("Eres menor de edad")
    
    # if-elif-else
"""
  if condicion1:

   # Bloque de código a ejecutar si la condicion1 es verdadera
   instrucciones

elif condicion2:

   # Bloque de código a ejecutar si la condicion2 es verdadera
   instrucciones

else:

   # Bloque de código a ejecutar si ninguna condición anterior es verdadera
   instrucciones
  """
calificacion = 85
if calificacion >= 90:
    print("Excelente")
elif calificacion >= 80:
    print("Muy bien")
elif calificacion >= 70:
    print("Bien")
else: print("Necesitas mejorar")
# Ejemplo de uso de if-elif-else
# Verificar si un número es par o impar
numero = int(input("Ingresa un número: "))

# Usamos el operador módulo (%) para comprobar si el residuo es 0
if numero % 2 == 0:
    print("El número es par.")
else:
    print("El número es impar.")
