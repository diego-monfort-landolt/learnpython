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

# Terminal löschen (Windows oder Linux/macOS)
os.system('cls' if os.name == 'nt' else 'clear')

print("💰 Bienvenido al analizador de ingresos 💰")
print("--------------------------------------------------")

# User-Eingabe
try:
    ingreso_manual = float(input("Ingresa tu ingreso mensual estimado (€): "))
    valor = '€'
    print(f"\nIngreso registrado: {ingreso_manual:.2f}{valor}\n")

    # Bewertung
    if ingreso_manual >= 10000:
        print("🔥 Estás en modo millonario. ¿Nos invitas algo?")
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

