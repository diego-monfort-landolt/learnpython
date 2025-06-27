import os
# Limpiar pantalla
os.system('cls' if os.name == 'nt' else 'clear')
# Mostrar menú
print('Menú')
print('1- Pizza de la casa')
print('2- Pizza Prosciutto')
print('3- Pizza Vegetariana') 
print('4- Pizza de la casa con extra')
print('5- Pizza Hawaiana')
print('6- Menú especial: 1 Pizza y 1 bebida')

# Capturar la elección del usuario
opcion = input('Por favor, elige una opción (1-6): ')
# Conversión de tipo
try:
    opcion = int(opcion)  # Convertir la entrada a número
    if opcion in [1, 2, 3, 4, 5, 6]:
        print('Preparando la pizza...')
        if opcion == 6:
            print('Preparando la pizza y la bebida...')
    else:
        print('Opción no válida')
        exit()
    # Pregunta adicional sobre la bebida
    bebida = input('¿Deseas una bebida con tu pizza? (si/no): ').strip().lower()
    if bebida == 'si':
        print('Por favor, elige tu bebida:')
        print('1 - Cola')
        print('2 - Fanta')
        print('3 - Cerveza')
        # Capturar la elección de bebida
        bebida_opcion = input('Tu elección (1-3): ').strip()
        # Validación de la entrada
        if bebida_opcion == '1':
            print('Cola añadida a tu pedido.')
        elif bebida_opcion == '2':
            print('Fanta añadida a tu pedido.')
        elif bebida_opcion == '3':
            print('Cerveza añadida a tu pedido.')
        else:
            print('Entrada no válida, por favor elige un número entre 1 y 3.')
    elif bebida == 'no':
        print('Ok, sin bebida.')
    else:
        print('Entrada no válida, por favor responde con "sí" o "no".')
except ValueError:
    print('Por favor, introduce un número válido.')