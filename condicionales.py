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
numero = int(input("Averiguamos si tu numero es par o inpar, Ingresa un número: "))

# Usamos el operador módulo (%) para comprobar si el residuo es 0
if numero % 2 == 0:
    print("El número es par.")
else:
    print("El número es impar.")
    
    
    
estado_batteria = int(input("Ingresa tu porcentaje de Bateria: "))

if estado_batteria >= 90:
    print("Batería llena")
elif estado_batteria >= 80: 
    print("Batería alta")
elif estado_batteria >= 70:
    print("Batería ok")
elif estado_batteria >= 50:   
    print("Batería Media")
elif estado_batteria >= 30:
    print("Batería baja")
else:
    print("Batería crítica")
    
  # test de if-elif-else
    
horas_de_trabajo = int(input("Ingresa tus Horas Trabajadas: "))
if horas_de_trabajo > 8:
    print("Has trabajado más de 8 horas")
elif horas_de_trabajo == 8:
    print("Has trabajado exactamente 8 horas")
else:
    print("Has trabajado menos de 8 horas")
  
# Tempratura
  
tempratura = float(input("Ingresa la temperatura en grados Celsius: "))

if tempratura == 0:
    print("Hace Frío...")
elif tempratura > 0 and tempratura <= 20:
    print("Se está perfecto, no hace calor ni frío")
elif tempratura > 20 and tempratura <= 30:
    print("Hace calor")
else:
    print("Hace calor extremo")
    
# Eingabe: Alter des Benutzers
alter = int(input("Ingresa tu edad: "))

# Alterskategorien überprüfen
if alter >= 0 and alter <= 12:
   print('eres un niño')
elif alter >= 13 and alter <= 19:
    print('eres un adolescente')
elif alter >= 20 and alter <= 65:
    print('eres un adulto')
else:
  print('eres un anciano')

