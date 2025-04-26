import os
import shutil
import subprocess
import time
from tkinter import messagebox, Tk
import tkinter as tk

def clear_teams_cache():
    try:
        # Dirección de la carpeta de caché de Teams
        teams_cache_path = os.path.join(os.getenv('APPDATA'), 'Microsoft', 'Teams')

        # Eliminar todos los archivos en la carpeta de Teams (caché)
        if os.path.exists(teams_cache_path):
            for root, dirs, files in os.walk(teams_cache_path, topdown=False):
                for name in files:
                    os.remove(os.path.join(root, name))
                for name in dirs:
                    os.rmdir(os.path.join(root, name))
            print("Caché de Teams eliminada correctamente.")
        else:
            print("No se encontró la carpeta de caché de Teams.")
    except Exception as e:
        print(f"Error al limpiar la caché de Teams: {e}")

def clear_outlook_cache():
    try:
        # Dirección de la carpeta de caché de Outlook
        outlook_cache_path = os.path.join(os.getenv('LOCALAPPDATA'), 'Microsoft', 'Outlook')

        # Eliminar todos los archivos de la caché de Outlook
        if os.path.exists(outlook_cache_path):
            for root, dirs, files in os.walk(outlook_cache_path, topdown=False):
                for name in files:
                    os.remove(os.path.join(root, name))
            print("Caché de Outlook eliminada correctamente.")
        else:
            print("No se encontró la carpeta de caché de Outlook.")
    except Exception as e:
        print(f"Error al limpiar la caché de Outlook: {e}")

def clear_all_cache():
    try:
        # Limpiar caché de Teams y Outlook
        clear_teams_cache()
        clear_outlook_cache()
        
        # Limpiar otras carpetas comunes de caché del sistema
        temp_folder = os.getenv('TEMP')
        if os.path.exists(temp_folder):
            print(f"Limpieza de caché en la carpeta: {temp_folder}")
            for root, dirs, files in os.walk(temp_folder):
                for file in files:
                    try:
                        os.remove(os.path.join(root, file))
                    except Exception as e:
                        print(f"Error al eliminar {file}: {e}")
            print("Caché general del sistema eliminada correctamente.")
        
        # Mostrar ventana emergente con mensaje de éxito
        show_success_message("¡Caché eliminada con éxito!", "Caché del sistema y de aplicaciones limpiada.")

    except Exception as e:
        print(f"Error al limpiar la caché general: {e}")
        show_error_message("Error al limpiar la caché", str(e))

def show_success_message(title, message):
    # Crear una ventana oculta para mostrar la alerta
    root = Tk()
    root.withdraw()  # Ocultar la ventana principal
    messagebox.showinfo(title, message)
    root.quit()

def show_error_message(title, message):
    # Crear una ventana oculta para mostrar la alerta de error
    root = Tk()
    root.withdraw()  # Ocultar la ventana principal
    messagebox.showerror(title, message)
    root.quit()

def restart_computer():
    try:
        print("Reiniciando el equipo...")
        time.sleep(2)
        # Ejecutar el comando para reiniciar el sistema
        subprocess.run(["shutdown", "/r", "/f", "/t", "0"], check=True)
    except Exception as e:
        print(f"Error al reiniciar el equipo: {e}")

def upgrade_computer():
    try:
        print("Iniciando la actualización del sistema...")
        time.sleep(2)
        # Ejecutar el comando de PowerShell para actualizar el sistema (puede requerir permisos de administrador)
        subprocess.run(["powershell", "Install-Module", "PSWindowsUpdate", "-Force", "-Confirm:$false"], check=True)
        subprocess.run(["powershell", "Get-WindowsUpdate", "-AcceptAll", "-AutoReboot"], check=True)
    except Exception as e:
        print(f"Error al realizar la actualización del sistema: {e}")

def show_menu():
    print("\nSeleccione una opción:")
    print("1. Limpiar la caché de Teams")
    print("2. Limpiar la caché de Outlook")
    print("3. Reiniciar el equipo")
    print("4. Hacer un upgrade del equipo")
    print("5. Limpiar todas las cachés (Teams, Outlook, y caché del sistema)")
    print("6. Salir")

def main():
    while True:
        show_menu()

        choice = input("Ingrese el número de la opción (1/2/3/4/5/6): ")

        if choice == '1':
            clear_teams_cache()
        elif choice == '2':
            clear_outlook_cache()
        elif choice == '3':
            restart_computer()
        elif choice == '4':
            upgrade_computer()
        elif choice == '5':
            clear_all_cache()
        elif choice == '6':
            print("¡Gracias por usar el script! Adiós.")
            break  # Salir del bucle y terminar el programa
        else:
            print("Opción no válida. Por favor, elija una opción válida (1/2/3/4/5/6).")

if __name__ == "__main__":
    main()
