import os
import shutil
import subprocess
import webbrowser
import tkinter as tk
from tkinter import messagebox, simpledialog

# ---- Konfiguration der Cache-Pfade ----
CHROME_CACHE_PATH = os.path.expanduser("~\\AppData\\Local\\Google\\Chrome\\User Data\\Default\\Cache")
EDGE_CACHE_PATH = os.path.expanduser("~\\AppData\\Local\\Microsoft\\Edge\\User Data\\Default\\Cache")
TEMP_CACHE_PATH = os.environ.get('TEMP')

# ---- URLs ----
COMPANY_PORTAL_URL = "https://www.unternehmensportal.de"
OFFICE_PASSWORD_RESET_URL = "https://account.microsoft.com/security"

# ---- Cache Funktionen ----
def clear_chrome_cache():
    if os.path.exists(CHROME_CACHE_PATH):
        try:
            shutil.rmtree(CHROME_CACHE_PATH)
            return True, "Chrome Cache wurde erfolgreich gelöscht."
        except Exception as e:
            return False, f"Fehler beim Löschen des Chrome Caches: {e}"
    else:
        return False, "Chrome Cache-Ordner nicht gefunden."

def clear_edge_cache():
    if os.path.exists(EDGE_CACHE_PATH):
        try:
            shutil.rmtree(EDGE_CACHE_PATH)
            return True, "Edge Cache wurde erfolgreich gelöscht."
        except Exception as e:
            return False, f"Fehler beim Löschen des Edge Caches: {e}"
    else:
        return False, "Edge Cache-Ordner nicht gefunden."

def clear_temp_files():
    try:
        deleted_files = 0
        for root, dirs, files in os.walk(TEMP_CACHE_PATH):
            for file in files:
                try:
                    os.remove(os.path.join(root, file))
                    deleted_files += 1
                except:
                    pass
        return True, f"{deleted_files} temporäre Dateien wurden gelöscht."
    except Exception as e:
        return False, f"Fehler beim Löschen temporärer Dateien: {e}"

def clear_browser_cache():
    browser_choice = simpledialog.askstring("Browser-Auswahl", "Welchen Browser möchten Sie bereinigen? (Edge/Chrome)")
    if browser_choice:
        browser_choice = browser_choice.lower()
        if browser_choice == 'chrome':
            return clear_chrome_cache()
        elif browser_choice == 'edge':
            return clear_edge_cache()
        else:
            return False, "Ungültige Auswahl. Nur 'Chrome' oder 'Edge'."
    return False, "Keine Auswahl getroffen."

# ---- Systemfunktionen ----
def update_policies():
    try:
        subprocess.run(["gpupdate", "/force"], check=True)
        subprocess.run(["ipconfig", "/flushdns"], check=True)
        subprocess.Popen("cmd /c echo Richtlinien aktualisiert && pause", shell=True)
        return True, "Richtlinien erfolgreich aktualisiert und DNS-Cache geleert."
    except Exception as e:
        return False, f"Fehler beim Aktualisieren der Richtlinien: {e}"

def defrag_drive():
    try:
        if os.name == 'nt':
            subprocess.run(["defrag", "C:", "/O"], check=True)
            return True, "Festplatte wurde erfolgreich defragmentiert."
        else:
            return False, "Nur auf Windows verfügbar."
    except Exception as e:
        return False, f"Fehler bei der Defragmentierung: {e}"

# ---- Portale ----
def open_company_portal():
    try:
        webbrowser.open(COMPANY_PORTAL_URL)
        return True, "Unternehmensportal wurde geöffnet."
    except Exception as e:
        return False, f"Fehler beim Öffnen des Portals: {e}"

def open_office_password_reset():
    try:
        webbrowser.open(OFFICE_PASSWORD_RESET_URL)
        return True, "Passwort-Seite geöffnet."
    except Exception as e:
        return False, f"Fehler beim Öffnen der Passwortseite: {e}"

# ---- Google-Suche ----
def search_google():
    query = search_entry.get()
    if query:
        webbrowser.open(f"https://www.google.com/search?q={query}")
        search_entry.delete(0, tk.END)
    else:
        messagebox.showwarning("Hinweis", "Bitte einen Suchbegriff eingeben.")

# ---- Aktionen Ausführen ----
def run_action(action_name):
    actions = {
        "Browser-Cache löschen": clear_browser_cache,
        "Temporäre Dateien löschen": clear_temp_files,
        "Richtlinien aktualisieren": update_policies,
        "Festplatte defragmentieren": defrag_drive,
        "Unternehmensportal öffnen": open_company_portal,
        "Office Passwort zurücksetzen": open_office_password_reset,
    }

    if action_name in actions:
        result, msg = actions[action_name]()
        if result:
            messagebox.showinfo("Erfolg", msg)
            reset_checkbox(action_name)
        else:
            messagebox.showerror("Fehler", msg)

def finish_program():
    root.quit()

def reset_checkbox(action_name):
    if action_name in check_vars:
        check_vars[action_name].set(False)

# ---- GUI ----
root = tk.Tk()
root.title("🛠️ System-Wartung & Tools")
root.geometry("500x560")
root.resizable(False, False)

# Optional: eigenes Icon setzen (.ico-Datei erforderlich)
try:
    root.iconbitmap("C:/Pfad/zum/icon.ico")  # Pfad ggf. anpassen
except:
    pass  # Falls Icon nicht gefunden wird, trotzdem starten

# Titel
tk.Label(root, text="🧰 System-Wartung & Tools", font=("Segoe UI", 13, "bold")).pack(pady=10)

# Suchleiste
search_frame = tk.Frame(root)
search_frame.pack(pady=10)

tk.Label(search_frame, text="🔍 Anleitung oder Problem suchen:", font=("Segoe UI", 10)).pack(pady=5)
search_entry = tk.Entry(search_frame, width=50)
search_entry.pack(pady=5)
tk.Button(search_frame, text="Suchen", command=search_google, bg="#2196F3", fg="white", padx=10, pady=5).pack()

# Optionen
frame = tk.Frame(root)
frame.pack(pady=5)

options = [
    "Browser-Cache löschen",
    "Temporäre Dateien löschen",
    "Richtlinien aktualisieren",
    "Festplatte defragmentieren",
    "Unternehmensportal öffnen",
    "Office Passwort zurücksetzen"
]

check_vars = {}
for option in options:
    var = tk.BooleanVar()
    checkbutton = tk.Checkbutton(frame, text=option, variable=var, font=("Segoe UI", 10))
    checkbutton.pack(anchor="w", padx=20, pady=5)
    check_vars[option] = var

# Buttons
button_frame = tk.Frame(root)
button_frame.pack(pady=20)

tk.Button(button_frame, text="Ausführen", command=lambda: [run_action(opt) for opt, val in check_vars.items() if val.get()],
          bg="#4CAF50", fg="white", padx=15, pady=6).grid(row=0, column=0, padx=10)

tk.Button(button_frame, text="Beenden", command=finish_program,
          bg="#f44336", fg="white", padx=15, pady=6).grid(row=0, column=1, padx=10)

# Fußzeile
footer = tk.Label(root, text="© 2025 IT Support Tool", font=("Segoe UI", 8), fg="gray")
footer.pack(side="bottom", pady=5)

root.mainloop()
