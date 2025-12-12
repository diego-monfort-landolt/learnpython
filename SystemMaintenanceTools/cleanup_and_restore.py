
import os
import shutil
import subprocess
import webbrowser
import platform

def clear_folder(path, description):
    if os.path.exists(path):
        print(f"Lösche {description} in {path}...")
        try:
            shutil.rmtree(path)
            os.makedirs(path, exist_ok=True)
            print(f"{description} erfolgreich gelöscht und neu erstellt.")
        except Exception as e:
            print(f"Fehler beim Löschen von {description}: {e}")
    else:
        print(f"{description} nicht gefunden: {path}")

def clear_temp_cache():
    clear_folder(os.getenv('TEMP'), "Temp-Cache")

def clear_teams_cache():
    teams_path = os.path.expanduser(r'~\\AppData\\Roaming\\Microsoft\\Teams')
    clear_folder(teams_path, "Teams-Cache")

def clear_outlook_cache():
    outlook_path = os.path.expanduser(r'~\\AppData\\Local\\Microsoft\\Outlook')
    clear_folder(outlook_path, "Outlook-Cache")

def reactivate_addins():
    print("Reaktiviere Outlook-Add-ins...")
    try:
        subprocess.run([
            "reg", "add",
            r"HKEY_CURRENT_USER\\Software\\Microsoft\\Office\\16.0\\Outlook\\Resiliency\\DisabledItems",
            "/v", "AddinEnable", "/t", "REG_DWORD", "/d", "1", "/f"
        ], check=True)
        print("Add-ins erfolgreich reaktiviert.")
    except Exception as e:
        print(f"Fehler beim Reaktivieren der Add-ins: {e}")

def open_browser():
    print("Öffne Standardbrowser...")
    webbrowser.open("https://www.microsoft.com")

def flush_dns():
    print("Leere DNS-Cache...")
    subprocess.run(["ipconfig", "/flushdns"], shell=True)

def restart_pc():
    print("Starte PC neu...")
    subprocess.run(["shutdown", "/r", "/t", "0"], shell=True)

def shutdown_pc():
    print("Fahre PC herunter...")
    subprocess.run(["shutdown", "/s", "/t", "0"], shell=True)

def show_system_info():
    print("Systeminformationen:")
    print(f"OS: {platform.system()} {platform.release()}")
    print(f"Version: {platform.version()}")
    print(f"Architektur: {platform.machine()}")
    print(f"Prozessor: {platform.processor()}")

def main_menu():
    while True:
        print("\n=== System Maintenance Toolkit ===")
        print("1. Temp-Cache löschen")
        print("2. Teams-Cache löschen")
        print("3. Outlook-Cache löschen")
        print("4. Outlook-Add-ins reaktivieren")
        print("5. Browser öffnen")
        print("6. DNS-Cache leeren")
        print("7. PC neu starten")
        print("8. PC herunterfahren")
        print("9. Systeminformationen anzeigen")
        print("0. Beenden")

        choice = input("Wähle eine Option: ")

        if choice == "1":
            clear_temp_cache()
        elif choice == "2":
            clear_teams_cache()
        elif choice == "3":
            clear_outlook_cache()
        elif choice == "4":
            reactivate_addins()
        elif choice == "5":
            open_browser()
        elif choice == "6":
            flush_dns()
        elif choice == "7":
            restart_pc()
        elif choice == "8":
            shutdown_pc()
        elif choice == "9":
            show_system_info()
        elif choice == "0":
            print("Beende das Programm...")
            break
        else:
            print("Ungültige Auswahl, bitte erneut versuchen.")

if __name__ == "__main__":
    main_menu()
