import os 
os.system('clear')
# limpiar la consola despues de ejecutar el programa

print('\n Valores booleanos basicos: ')
print('True:', True)
print('False:', False)

#operares comparacion
print('\n Operadores de comparacion: ')
print('1 == 1:', 1 == 1) # True igualdad
print('1 != 1:', 1 != 1) # False desigualdad ! =
print('1 <= 1:', 1 <= 1) # True menor o igual que
print('5 < 3:', 5 < 3) # False
print('5 > 3:', 5 > 3) # True

print('5 <= 3:', 5 <= 3) # False (menor o igual que)
# comparacion de cadenas
# jedesr buchstabe hat seine eigene nummer diese wird dan so berechnet um einen true und false zu erhalten
print('Pera < manzana:', 'Pera' < 'manzana') # True
print('Pera > manzana:', 'Pera' > 'manzana') # False
print('Hola == hola:', 'Hola' == 'HOla')# False (diferente)
print('Pera == manzana:', 'Pera' == 'manzana') # False    
print('Pera != manzana:', 'Pera' != 'manzana') # True
print('Pera <= manzana:', 'Pera' <= 'manzana') # True (menor o igual que)
print('Pera >= manzana:', 'Pera' >= 'manzana') # False (mayor o igual que)

print('and:')
print('A   B    A and B')
print('True True:', True and True) # True
print('True False:', True and False) # False
print('False True:', False and True) # False
print('False False:', False and False) # False
print('or:')
print('A   B    A or B')
print('True True:', True or True) # True
print('True False:', True or False) # True
print('False True:', False or True) # True
print('False False:', False or False) # False

print('not:')
print('A    not A') 
print('True:', True) # True
print('not True:', not True) # False
print('False:', False) # False
print('not False:', not False) # True


