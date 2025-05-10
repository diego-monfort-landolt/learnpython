import psutil
import subprocess
import threading
import time

# Funktion, um die aktuell angemeldeten Benutzer anzuzeigen
def get_logged_in_users():
    users = psutil.users()
    if not users:
        print("Keine Benutzer sind momentan eingeloggt.")
    else:
        for user in users:
            # Überprüfen, ob die Attribute existieren, bevor sie verwendet werden
            name = user.name if hasattr(user, 'name') else 'Unbekannt'
            host = user.host if hasattr(user, 'host') else 'Unbekannt'
            terminal = user.term if hasattr(user, 'term') else 'Unbekannt'
            print(f"Benutzer: {name} - Host: {host} - Terminal: {terminal}")

# Funktion, um einen Windows Defender Scan zu starten
def run_windows_defender_scan():
    print("Starte Windows Defender Scan...")
    subprocess.run(["powershell", "-Command", "Start-MpScan -ScanType FullScan"])

# Funktion zur kontinuierlichen Überwachung von Benutzern
def monitor_users():
    while True:
        print("\nÜberwache angemeldete Benutzer:")
        get_logged_in_users()
        time.sleep(60)  # Alle 60 Sekunden die Benutzer anzeigen

# Funktion zur kontinuierlichen Ausführung des Virenscans
def monitor_virus_scan():
    while True:
        print("\nStarte Virenscan...")
        run_windows_defender_scan()
        time.sleep(3600)  # Alle 3600 Sekunden (1 Stunde) den Scan ausführen

# Funktion, die beide Aufgaben im Hintergrund ausführt
def run_background_tasks():
    user_thread = threading.Thread(target=monitor_users)
    virus_thread = threading.Thread(target=monitor_virus_scan)

    user_thread.daemon = True  # Damit die Threads beim Beenden des Programms automatisch beendet werden
    virus_thread.daemon = True

    user_thread.start()
    virus_thread.start()

    # Halte das Skript am Laufen, um die Hintergrundprozesse zu ermöglichen
    while True:
        time.sleep(1)

# Start des Programms
if __name__ == "__main__":
    print("Starte das Systemüberwachungs-Skript...")
    run_background_tasks()
