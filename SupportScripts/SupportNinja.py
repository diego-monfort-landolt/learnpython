import os
import shutil
import subprocess
import time
import winreg
from pathlib import Path
import sys

# ANSI-Farben
RED = "\033[91m"
GREEN = "\033[92m"
YELLOW = "\033[93m"
BLUE = "\033[94m"
CYAN = "\033[96m"
RESET = "\033[0m"
BOLD = "\033[1m"

def print_header():
    os.system("cls")
    print(BOLD + CYAN + "====================================" + RESET)
    print(BOLD + BLUE + "        SUPPORT NINJA  ⚡  v1.1      " + RESET)
    print(BOLD + CYAN + "====================================" + RESET)

def clear_teams_cache():
    print(YELLOW + "🧹 Teams Cache wird gelöscht..." + RESET)

    teams_paths = [
        Path(os.environ["APPDATA"]) / "Microsoft" / "Teams",
        Path(os.environ["LOCALAPPDATA"]) / "Microsoft" / "Teams",
        Path(os.environ["LOCALAPPDATA"]) / "Microsoft" / "TeamsMeetingAddin",
        Path(os.environ["LOCALAPPDATA"]) / "Microsoft" / "TeamsPresenceAddin"
    ]

    for p in teams_paths:
        if p.exists():
            shutil.rmtree(p, ignore_errors=True)
            print(GREEN + f"✔ Gelöscht: {p}" + RESET)

    print(CYAN + "🔄 Teams wird neu gestartet..." + RESET)
    subprocess.Popen(["cmd", "/c", "start", "teams"])

def clear_outlook_cache():
    print(YELLOW + "🧹 Outlook Cache wird gelöscht..." + RESET)

    outlook_path = Path(os.environ["LOCALAPPDATA"]) / "Microsoft" / "Outlook"
    if outlook_path.exists():
        shutil.rmtree(outlook_path, ignore_errors=True)
        print(GREEN + "✔ Outlook Cache gelöscht." + RESET)
    else:
        print(YELLOW + "ℹ Kein Outlook Cache gefunden." + RESET)

    print(CYAN + "🔄 Outlook wird neu gestartet..." + RESET)
    subprocess.Popen(["cmd", "/c", "start", "outlook"])

def enable_disabled_outlook_addins():
    print(YELLOW + "🔍 Suche nach deaktivierten Outlook Add-ins..." + RESET)

    reg_path = r"Software\Microsoft\Office\16.0\Outlook\Resiliency\DisabledItems"

    try:
        key = winreg.OpenKey(winreg.HKEY_CURRENT_USER, reg_path, 0, winreg.KEY_ALL_ACCESS)
    except FileNotFoundError:
        print(GREEN + "✔ Keine deaktivierten Add-ins gefunden." + RESET)
        return

    try:
        i = 0
        while True:
            value = winreg.EnumValue(key, i)
            print(RED + f"⚠ Deaktiviertes Add-in gefunden: {value[0]}" + RESET)
            i += 1
    except OSError:
        pass

    winreg.DeleteKey(winreg.HKEY_CURRENT_USER, reg_path)
    print(GREEN + "✔ Alle deaktivierten Add-ins wurden wieder aktiviert." + RESET)

    print(CYAN + "🔄 Outlook wird neu gestartet..." + RESET)
    subprocess.Popen(["cmd", "/c", "start", "outlook"])

def run_gpupdate():
    print(YELLOW + "🔄 Gruppenrichtlinien werden aktualisiert (gpupdate /force)..." + RESET)
    subprocess.call(["cmd", "/c", "gpupdate /force"])
    print(GREEN + "✔ gpupdate /force abgeschlossen." + RESET)

def flush_dns():
    print(YELLOW + "🌐 DNS Cache wird geleert (ipconfig /flushdns)..." + RESET)
    subprocess.call(["cmd", "/c", "ipconfig /flushdns"])
    print(GREEN + "✔ DNS Cache geleert." + RESET)

def self_delete():
    print(RED + "🗑 Script wird gelöscht..." + RESET)

    script_path = Path(sys.argv[0]).resolve()
    delete_cmd = f'del "{script_path}"'

    subprocess.Popen(["cmd", "/c", delete_cmd])
    print(GREEN + "✔ Script wird nach Beenden der Sitzung entfernt." + RESET)
    time.sleep(1)
    sys.exit()

def main():
    while True:
        print_header()
        print(BOLD + "Menü:" + RESET)
        print(f"{GREEN}[1]{RESET} Teams Cache löschen + Teams neu starten")
        print(f"{GREEN}[2]{RESET} Outlook Cache löschen + Outlook neu starten")
        print(f"{GREEN}[3]{RESET} Deaktivierte Outlook Add-ins aktivieren + Outlook neu starten")
        print(f"{GREEN}[4]{RESET} gpupdate /force ausführen")
        print(f"{GREEN}[6]{RESET} DNS Cache leeren (ipconfig /flushdns)")
        print(f"{RED}[5]{RESET} Script löschen")
        print(f"{YELLOW}[0]{RESET} Beenden\n")

        choice = input("Auswahl: ").strip()

        if choice == "1":
            clear_teams_cache()
        elif choice == "2":
            clear_outlook_cache()
        elif choice == "3":
            enable_disabled_outlook_addins()
        elif choice == "4":
            run_gpupdate()
        elif choice == "6":
            flush_dns()
        elif choice == "5":
            self_delete()
        elif choice == "0":
            break
        else:
            print(RED + "❌ Ungültige Eingabe." + RESET)
        input("\nWeiter mit Enter...")

if __name__ == "__main__":
    main()
