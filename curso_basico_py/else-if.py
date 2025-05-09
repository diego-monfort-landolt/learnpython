# import os
# os.system('cls' if os.name == 'nt' else 'clear')  # für Windows/Linux

# ingreso_manual = 500
# valor = ' €'

# print(f"Ingreso detectado: {ingreso_manual}{valor}")

# if ingreso_manual > 6000:
#     print('💸 Eres un PRO! Estás a modo lujo...')
# elif ingreso_manual > 3000:
#     print('🚀 Creo que vas por muy buen camino...')
# elif ingreso_manual > 300:
#     print('😬 Uff... Algo es algo, sigue luchando!')
# else:
#     print('💀 SOS pobre... perdona...')
    
    
    
import os

# Limpiar terminal
os.system('cls' if os.name == 'nt' else 'clear')

print("💰 Bienvenido al analizador de ingresos 💰")
print("--------------------------------------------------")

# Entrada del usuario
try:
    ingreso_manual = float(input("Ingresa tu ingreso mensual estimado (€): "))
    valor = '€'
    print(f"\nIngreso registrado: {ingreso_manual:.2f}{valor}\n")

    # Evaluación de ingresos
    if ingreso_manual >= 10000:
        print("🔥 Estás en modo MILLONARIO. ¿Nos invitas algo?")
        
        celebracion = input("¿Vas a celebrarlo? (sí/no): ").strip().lower()

        if celebracion in ['sí', 'si', 's']:
            print("\n🍾 Sacando el champán...")
            print("🥂 Un poco de vodka para el estilo...")
            print("💃 ¡Una noche de discoteca te espera! 🎉")
        else:
            print("\n😔 Entiendo... a veces el dinero no lo es todo.")
    
    elif ingreso_manual >= 6000:
        print("💎 Eres un PRO! Vives con estilo.")
    elif ingreso_manual >= 3000:
        print("🚀 Vas por muy buen camino. Sigue así.")
    elif ingreso_manual >= 1000:
        print("🙂 No está mal, pero siempre se puede mejorar.")
    elif ingreso_manual >= 300:
        print("😬 Uff... Algo entra, pero ajusta el cinturón.")
    else:
        print("💀 SOS pobre... perdona... busca soluciones.")

except ValueError:
    print("❌ Entrada no válida. Por favor, ingresa un número.")
