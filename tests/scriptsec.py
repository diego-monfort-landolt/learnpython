import subprocess
import os
from datetime import datetime

# Nombre del archivo de informe
reporte = "informe_seguridad.txt"

def obtener_usuarios():
    resultado = subprocess.run("net user", capture_output=True, text=True, shell=True)
    return resultado.stdout

def usuarios_admin():
    resultado = subprocess.run("net localgroup Administradores", capture_output=True, text=True, shell=True)
    return resultado.stdout

def comprobar_bitlocker():
    resultado = subprocess.run("manage-bde -status", capture_output=True, text=True, shell=True)
    return resultado.stdout

def usuarios_activos():
    resultado = subprocess.run("query user", capture_output=True, text=True, shell=True)
    return resultado.stdout

def generar_informe():
    with open(reporte, "w", encoding="utf-8") as f:
        f.write("🛡️ INFORME DE SEGURIDAD DEL SISTEMA\n")
        f.write(f"Generado el: {datetime.now()}\n")
        f.write("="*50 + "\n\n")

        f.write("👥 Usuarios registrados en el sistema:\n")
        f.write(obtener_usuarios() + "\n")

        f.write("🔑 Usuarios con privilegios de administrador:\n")
        f.write(usuarios_admin() + "\n")

        f.write("🔒 Estado del disco y cifrado (BitLocker):\n")
        f.write(comprobar_bitlocker() + "\n")

        f.write("👤 Usuarios activos actualmente:\n")
        f.write(usuarios_activos() + "\n")

    print(f"✅ Informe generado correctamente: {reporte}")

if __name__ == "__main__":
    generar_informe()
