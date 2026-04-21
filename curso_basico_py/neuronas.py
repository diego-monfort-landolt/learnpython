potencial_reposo = -60
umbral_excitacion = range(-50, -70)
mV = int(input('Ingesa los mV a ejecutar en la neurona: '))

resultado = potencial_reposo+mV
print(f'La neurona ahora tiene un potencial de {resultado}mV ')

if resultado in umbral_excitacion:
  print('Neurona Exito')
else:
  print('No ha pasado nada')
  