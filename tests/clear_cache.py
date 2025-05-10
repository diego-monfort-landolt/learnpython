import os
import shutil
import ctypes
import sys
import subprocess

"""
###------------------>---------------------###
CMD als admin öffnen Script abspielen -> cache wird gelöscht
###------------------>---------------------###


"""
def is_admin():
    try:
        return ctypes.windll.shell32.IsUserAnAdmin()
    except:
        return False

# === Funktion: Ordner löschen ===
def delete_folder(path, name=""):
    try:
        if os.path.exists(path):
            shutil.rmtree(path)
            print(f"[✓] {name} gelöscht: {path}")
        else:
            print(f"[ ] {name} nicht gefunden.")
    except Exception as e:
        print(f"[!] Fehler beim Löschen von {name}: {e}")

# === Funktion: Datei löschen ===
def delete_file(path, name=""):
    try:
        if os.path.exists(path):
            os.remove(path)
            print(f"[✓] {name} gelöscht: {path}")
        else:
            print(f"[ ] {name} nicht gefunden.")
    except Exception as e:
        print(f"[!] Fehler beim Löschen von {name}: {e}")

# === Funktion: Browser-Prozesse beenden ===
def kill_browsers():
    browsers = ["chrome.exe", "firefox.exe", "msedge.exe"]
    for b in browsers:
        subprocess.call(f"taskkill /f /im {b}", shell=True)
        print(f"[✓] {b} beendet (falls offen)")

# === Hauptfunktion ===
def main():
    if not is_admin():
        print("[!] Bitte starte das Skript als Administrator.")
        ctypes.windll.shell32.ShellExecuteW(None, "runas", sys.executable, __file__, None, 1)
        sys.exit()

    print("📦 Starte Browserbereinigung...\n")

    kill_browsers()

    user = os.getenv("USERNAME")
    localappdata = os.getenv("LOCALAPPDATA")
    appdata = os.getenv("APPDATA")

    # Chrome
    delete_folder(os.path.join(localappdata, r"Google\Chrome\User Data\Default\Cache"), "Chrome Cache")
    delete_file(os.path.join(localappdata, r"Google\Chrome\User Data\Default\Cookies"), "Chrome Cookies")

    # Edge
    delete_folder(os.path.join(localappdata, r"Microsoft\Edge\User Data\Default\Cache"), "Edge Cache")
    delete_file(os.path.join(localappdata, r"Microsoft\Edge\User Data\Default\Cookies"), "Edge Cookies")

    # Firefox
    firefox_profile_path = os.path.join(appdata, r"Mozilla\Firefox\Profiles")
    if os.path.exists(firefox_profile_path):
        for profile in os.listdir(firefox_profile_path):
            cache2_path = os.path.join(firefox_profile_path, profile, "cache2")
            cookies_path = os.path.join(firefox_profile_path, profile, "cookies.sqlite")
            delete_folder(cache2_path, "Firefox Cache")
            delete_file(cookies_path, "Firefox Cookies")

    print("\n✅ Bereinigung abgeschlossen.")

if __name__ == "__main__":
    main()
