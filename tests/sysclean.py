import os
import shutil
import subprocess
from datetime import datetime
from pathlib import Path
import platform

LOG_FILE = Path("tool_log.txt")

def log_action(action: str):
    with LOG_FILE.open("a", encoding="utf-8") as f:
        f.write(f"[{datetime.now()}] {action}\n")

def confirm(prompt: str) -> bool:
    choice = input(f"{prompt} (j/n): ").lower()
    return choice == "j"

def option1_clear_cache():
    print("Option 1: Cache und Zwischenspeicher leeren...")
    if not confirm("Sind Sie sicher, dass Sie den Temp-Ordner löschen möchten?"):
        return
    temp_dir = Path(os.environ.get("TEMP", "C:\\Windows\\Temp"))
    if temp_dir.exists():
        shutil.rmtree(temp_dir, ignore_errors=True)
        print(f"Temp-Ordner {temp_dir} gelöscht.")
        log_action(f"Temp-Ordner {temp_dir} gelöscht")
    # DNS-Flush
    try:
        subprocess.run(["ipconfig", "/flushdns"], check=True, shell=True)
        print("DNS-Cache geleert.")
        log_action("DNS-Cache geleert")
    except Exception as e:
        print(f"Fehler beim DNS-Flush: {e}")
        log_action(f"Fehler beim DNS-Flush: {e}")

def option2_outlook_profile():
    print("Option 2: Outlook Cache löschen und neues Profil erstellen...")
    if not confirm("Sind Sie sicher, dass Sie den Outlook-Cache löschen möchten?"):
        return
    outlook_cache = Path(os.environ["LOCALAPPDATA"]) / "Microsoft" / "Outlook"
    if outlook_cache.exists():
        shutil.rmtree(outlook_cache, ignore_errors=True)
        print("Outlook Cache gelöscht.")
        log_action("Outlook Cache gelöscht")

    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    profile_name = f"Profil_{timestamp}"
    print(f"Neues Outlook-Profil: {profile_name}")
    log_action(f"Neues Outlook-Profil erstellt: {profile_name}")

    try:
        subprocess.run(["outlook.exe", f"/profiles {profile_name}"], shell=True)
        print("Outlook mit neuem Profil gestartet.")
        log_action("Outlook gestartet")
    except Exception as e:
        print(f"Fehler beim Starten von Outlook: {e}")
        log_action(f"Fehler beim Starten von Outlook: {e}")

def option3_sort_images():
    print("Option 3: Bilder nach Datum sortieren...")
    downloads = Path.home() / "Downloads"
    target_dir = downloads / "Bilder_sortiert"
    target_dir.mkdir(exist_ok=True)

    moved_files = 0
    for file in downloads.iterdir():
        if file.suffix.lower() in [".jpg", ".jpeg", ".png", ".gif", ".bmp"]:
            date_str = datetime.fromtimestamp(file.stat().st_mtime).strftime("%Y-%m-%d")
            date_folder = target_dir / date_str
            date_folder.mkdir(exist_ok=True)
            shutil.move(str(file), date_folder / file.name)
            print(f"{file.name} → {date_folder}")
            moved_files += 1
    log_action(f"{moved_files} Bilder sortiert")
    print(f"{moved_files} Bilder wurden sortiert.")

def option4_clear_recycle_bin():
    print("Option 4: Papierkorb leeren...")
    try:
        subprocess.run(["powershell", "-command", "Clear-RecycleBin -Force"], shell=True)
        print("Papierkorb geleert.")
        log_action("Papierkorb geleert")
    except Exception as e:
        print(f"Fehler beim Leeren des Papierkorbs: {e}")
        log_action(f"Fehler beim Leeren des Papierkorbs: {e}")

def option5_system_info():
    print("Option 5: Systeminformationen anzeigen...")
    info = {
        "OS": platform.system(),
        "Version": platform.version(),
        "Benutzer": os.getlogin(),
        "Downloads-Größe": sum(f.stat().st_size for f in (Path.home()/ "Downloads").iterdir() if f.is_file()) // (1024*1024)
    }
    for k, v in info.items():
        print(f"{k}: {v}")
    log_action("Systeminformationen angezeigt")

def main():
    while True:
        print("\nBitte wählen Sie eine Option:")
        print("1. Cache und Temp-Ordner leeren")
        print("2. Outlook Cache löschen und neues Profil erstellen")
        print("3. Bilder im Download-Ordner nach Datum sortieren")
        print("4. Papierkorb leeren")
        print("5. Systeminformationen anzeigen")
        print("6. Beenden")

        choice = input("Ihre Wahl (1-6): ")

        if choice == "1":
            option1_clear_cache()
        elif choice == "2":
            option2_outlook_profile()
        elif choice == "3":
            option3_sort_images()
        elif choice == "4":
            option4_clear_recycle_bin()
        elif choice == "5":
            option5_system_info()
        elif choice == "6":
            print("Programm beendet.")
            break
        else:
            print("Ungültige Auswahl.")

if __name__ == "__main__":
    main()
