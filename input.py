nombre = input("Ingresa tu nombre: ")
edad = input("Ingresa tu edad: ")


print("Hola, " + nombre + "!")
print("Tienes " + edad + " años.")


edad = int(input("Ingresa tu edad: "))


if edad >= 18:
    print("Eres mayor de edad.")
else:
    print("Eres menor de edad.")
    

nombre_uno = "Juan"
edad_uno = 25


print(f"Hola, mi nombre es {nombre_uno} y tengo {edad_uno} años.")

# En este caso, las variables se incrustan dentro de la cadena utilizando llaves {} y se precede la cadena con la letra f para indicar que es una f-string.