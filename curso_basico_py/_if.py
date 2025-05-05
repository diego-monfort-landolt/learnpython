import os
# limpiar la consola despues de ejecutar el programa
os.system('clear')


nota = 5
if nota >= 9:
  print('Excelente')
elif nota >= 7:
  print('Bien') 
elif nota >= 5:
  print('Regular')
else:
  print('Vuelvo a estudiar')
  
edad = 19
tienes_carnet = True
if edad >= 18 and tienes_carnet:
  print('Puedes conducir')
else: 
  print('No puedes conducir')
  # con or solo tiene que estar una condicion en true para aceptar
  if edad >= 18 or tienes_carnet:
    print('Puedes conducir aqui')
  else:
    print('Paga la multa, YA!')
    
    # con not se niega la condicion
es_fin_de_semana = False
if not es_fin_de_semana:
  print('A trabajar!')
else:
  print('Porfin llego el fin de semana')