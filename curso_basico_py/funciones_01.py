"""
funciones definidas por el usuario
"""
# Simple
import os
os.system('cls')

def saludo():
    print('Hola Python!')
saludo()

#con retorno

def return_saludo():
    return 'Hola Python!'
print(return_saludo())

# Con argumento

def arg_saludo(name):
  print(f'Hola {name}')
  
arg_saludo('Diego')

# Con argumentos

def arg_saludo(saludo, name):
  print(f'{saludo}, {name}')
  
arg_saludo('Hi', 'Diego')

# con argumento preterminado
def defaoult_arg_saludo(name='Diego'):
  print(f'Hola {name}')
  
defaoult_arg_saludo()
