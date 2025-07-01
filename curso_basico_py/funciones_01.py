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
#con retornos de varios valores

# def multiple_return_saludo():
#   return 'Hola', 'Python', 'Diego'
# greet, name = multiple_return_saludo()
# print(greet)
# print(name)

# Con un numero variable de argumentos

def variable_arg_greet(*names):
  for name in names:
    print(f'Hola {name}')
variable_arg_greet('Python', 'Learning', 'Diego')

# Con un numero variable de argumentos con palabra clave

def variable_key_arg_greet(**names):
  for key, value in names.items():
    print(f'{value} ({key})')
    
variable_key_arg_greet(
  language='Python', 
  name='Diego', 
  age=34, 
  alias='D' 
  )