import os
import shutil
import subprocess

# Pfad zur Batch- und PowerShell-Skriptdatei
batch_script_path = 'clear_cache.bat'
powershell_script_path = 'clear_cache.ps1'

# Funktionen zum Löschen von Cache-Dateien (Wie im vorherigen Beispiel)
def delete_google_chrome_cache():
    chrome_cache_paths = [
        os.path.expanduser(r'~\AppData\Local\Google\Chrome\User Data\Default\Cache'),
        os.path.expanduser(r'~\AppData\Local\Google\Chrome\User Data\Default\Cookies')
    ]
    for path in chrome_cache_paths:
        if os.path.exists(path):
            try:
                shutil.rmtree(path)
                print(f"Google Chrome Cache gelöscht: {path}")
            except Exception as e:
                print(f"Fehler beim Löschen von Google Chrome Cache: {e}")

def delete_edge_cache():
    edge_cache_paths = [
        os.path.expanduser(r'~\AppData\Local\Microsoft\Edge\User Data\Default\Cache'),
        os.path.expanduser(r'~\AppData\Local\Microsoft\Edge\User Data\Default\Cookies')
    ]
    for path in edge_cache_paths:
        if os.path.exists(path):
            try:
                shutil.rmtree(path)
                print(f"Microsoft Edge Cache gelöscht: {path}")
            except Exception as e:
                print(f"Fehler beim Löschen von Microsoft Edge Cache: {e}")

def delete_outlook_cache():
    outlook_cache_paths = [
        os.path.expanduser(r'~\AppData\Local\Microsoft\Outlook\Offline Address Books'),
        os.path.expanduser(r'~\AppData\Local\Microsoft\Outlook\Temp')
    ]
    for path in outlook_cache_paths:
        if os.path.exists(path):
            try:
                shutil.rmtree(path)
                print(f"Outlook Cache gelöscht: {path}")
            except Exception as e:
                print(f"Fehler beim Löschen von Outlook Cache: {e}")

def delete_onedrive_cache():
    onedrive_cache_path = os.path.expanduser(r'~\AppData\Local\Microsoft\OneDrive\cache')
    if os.path.exists(onedrive_cache_path):
        try:
            shutil.rmtree(onedrive_cache_path)
            print(f"OneDrive Cache gelöscht: {onedrive_cache_path}")
        except Exception as e:
            print(f"Fehler beim Löschen von OneDrive Cache: {e}")

def delete_ms_teams_cache():
    teams_cache_paths = [
        os.path.expanduser(r'~\AppData\Roaming\Microsoft\Teams\Cache'),
        os.path.expanduser(r'~\AppData\Roaming\Microsoft\Teams\Cookies'),
        os.path.expanduser(r'~\AppData\Roaming\Microsoft\Teams\blob_storage'),
        os.path.expanduser(r'~\AppData\Roaming\Microsoft\Teams\databases')
    ]
    for path in teams_cache_paths:
        if os.path.exists(path):
            try:
                shutil.rmtree(path)
                print(f"MS Teams Cache gelöscht: {path}")
            except Exception as e:
                print(f"Fehler beim Löschen von MS Teams Cache: {e}")

def delete_cisco_vpn_cache():
    cisco_vpn_cache_path = os.path.expanduser(r'~\AppData\Local\Cisco\Cisco AnyConnect Secure Mobility Client\logs')
    if os.path.exists(cisco_vpn_cache_path):
        try:
            shutil.rmtree(cisco_vpn_cache_path)
            print(f"Cisco VPN Cache gelöscht: {cisco_vpn_cache_path}")
        except Exception as e:
            print(f"Fehler beim Löschen von Cisco VPN Cache: {e}")

# Funktionen zum Erstellen der Batch- und PowerShell-Skripte
def create_batch_script():
    batch_script_content = '''@echo off
echo Lösche Google Chrome Cache...
rmdir /s /q "%USERPROFILE%\\AppData\\Local\\Google\\Chrome\\User Data\\Default\\Cache"
rmdir /s /q "%USERPROFILE%\\AppData\\Local\\Google\\Chrome\\User Data\\Default\\Cookies"

echo Lösche Microsoft Edge Cache...
rmdir /s /q "%USERPROFILE%\\AppData\\Local\\Microsoft\\Edge\\User Data\\Default\\Cache"
rmdir /s /q "%USERPROFILE%\\AppData\\Local\\Microsoft\\Edge\\User Data\\Default\\Cookies"

echo Lösche Outlook Cache...
rmdir /s /q "%USERPROFILE%\\AppData\\Local\\Microsoft\\Outlook\\Offline Address Books"
rmdir /s /q "%USERPROFILE%\\AppData\\Local\\Microsoft\\Outlook\\Temp"

echo Lösche OneDrive Cache...
rmdir /s /q "%USERPROFILE%\\AppData\\Local\\Microsoft\\OneDrive\\cache"

echo Lösche MS Teams Cache...
rmdir /s /q "%USERPROFILE%\\AppData\\Roaming\\Microsoft\\Teams\\Cache"
rmdir /s /q "%USERPROFILE%\\AppData\\Roaming\\Microsoft\\Teams\\Cookies"
rmdir /s /q "%USERPROFILE%\\AppData\\Roaming\\Microsoft\\Teams\\blob_storage"
rmdir /s /q "%USERPROFILE%\\AppData\\Roaming\\Microsoft\\Teams\\databases"

echo Lösche Cisco VPN Cache...
rmdir /s /q "%USERPROFILE%\\AppData\\Local\\Cisco\\Cisco AnyConnect Secure Mobility Client\\logs"

echo Cache-Bereinigung abgeschlossen!
pause'''

    with open(batch_script_path, 'w') as file:
        file.write(batch_script_content)
        print("Batch-Skript wurde erstellt.")

def create_powershell_script():
    ps_script_content = '''Write-Host "Lösche Google Chrome Cache..."
Remove-Item -Recurse -Force "$env:USERPROFILE\\AppData\\Local\\Google\\Chrome\\User Data\\Default\\Cache"
Remove-Item -Recurse -Force "$env:USERPROFILE\\AppData\\Local\\Google\\Chrome\\User Data\\Default\\Cookies"

Write-Host "Lösche Microsoft Edge Cache..."
Remove-Item -Recurse -Force "$env:USERPROFILE\\AppData\\Local\\Microsoft\\Edge\\User Data\\Default\\Cache"
Remove-Item -Recurse -Force "$env:USERPROFILE\\AppData\\Local\\Microsoft\\Edge\\User Data\\Default\\Cookies"

Write-Host "Lösche Outlook Cache..."
Remove-Item -Recurse -Force "$env:USERPROFILE\\AppData\\Local\\Microsoft\\Outlook\\Offline Address Books"
Remove-Item -Recurse -Force "$env:USERPROFILE\\AppData\\Local\\Microsoft\\Outlook\\Temp"

Write-Host "Lösche OneDrive Cache..."
Remove-Item -Recurse -Force "$env:USERPROFILE\\AppData\\Local\\Microsoft\\OneDrive\\cache"

Write-Host "Lösche MS Teams Cache..."
Remove-Item -Recurse -Force "$env:USERPROFILE\\AppData\\Roaming\\Microsoft\\Teams\\Cache"
Remove-Item -Recurse -Force "$env:USERPROFILE\\AppData\\Roaming\\Microsoft\\Teams\\Cookies"
Remove-Item -Recurse -Force "$env:USERPROFILE\\AppData\\Roaming\\Microsoft\\Teams\\blob_storage"
Remove-Item -Recurse -Force "$env:USERPROFILE\\AppData\\Roaming\\Microsoft\\Teams\\databases"

Write-Host "Lösche Cisco VPN Cache..."
Remove-Item -Recurse -Force "$env:USERPROFILE\\AppData\\Local\\Cisco\\Cisco AnyConnect Secure Mobility Client\\logs"

Write-Host "Cache-Bereinigung abgeschlossen!"'''

    with open(powershell_script_path, 'w') as file:
        file.write(ps_script_content)
        print("PowerShell-Skript wurde erstellt.")

# Überprüfen, ob Python installiert ist
def is_python_installed():
    try:
        subprocess.check_output(["python", "--version"], stderr=subprocess.STDOUT)
        return True
    except subprocess.CalledProcessError:
        return False

# Skripte erstellen und ausführen
def main():
    if is_python_installed():
        print("Python ist installiert. Starte Python-Skript...")
        subprocess.run(["python", __file__])
    else:
        print("Python ist nicht installiert. Erstelle und starte Batch- oder PowerShell-Skript...")
        create_batch_script()
        create_powershell_script()

        # Automatisch das Batch-Skript oder PowerShell-Skript ausführen
        if os.name == 'nt':  # Nur für Windows
            subprocess.run([batch_script_path], shell=True)

if __name__ == "__main__":
    main()
