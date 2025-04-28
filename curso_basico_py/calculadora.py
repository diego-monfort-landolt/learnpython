# Menú de cálculo simple basado en la selección del usuario
print("Selecciona una operación:")
print("1. Suma")
print("2. Resta")
print("3. Multiplicación")
print("4. División")
print("5. Salir")

# Recibimos la opción del usuario
opcion = int(input("Ingresa el número de la operación (1-5): "))  # Cambiamos el rango a 1-5

# Si el usuario elige salir, finalizamos antes de pedir números
if opcion == 5:
    print("Gracias por usar la calculadora. ¡Adiós!")
# Continuamos con las demás operaciones solo si la opción no es salir
else:
    numero1 = float(input("Ingresa el primer número: "))
    numero2 = float(input("Ingresa el segundo número: "))

    # Condicionales para realizar la operación seleccionada
    if opcion == 1:
        print(f"El resultado de la suma es: {numero1 + numero2}")
    elif opcion == 2:
        print(f"El resultado de la resta es: {numero1 - numero2}")
    elif opcion == 3:
        print(f"El resultado de la multiplicación es: {numero1 * numero2}")
    elif opcion == 4:
        # Verificamos que no se divida entre 0
        if numero2 != 0:
            print(f"El resultado de la división es: {numero1 / numero2}")
        else:
            print("Error: No se puede dividir entre cero.")
    else:
        print("Opción no válida.")
