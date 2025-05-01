import os
import subprocess
import tkinter as tk
from tkinter import messagebox
from tkinter import ttk

# Funktion: Cache löschen
def clear_cache():
    # Neues Fenster mit Ladebalken öffnen
    show_progress("🔄 Cache wird gelöscht", "Bitte warten, der Cache wird gelöscht. Dies kann einen Moment dauern.")
    try:
        os.system("del /s /q %temp%\\*")
        os.system("del /s /q C:\\Windows\\Temp\\*")
        # Ladebalken fortsetzen
        progress_bar['value'] = 100
        window.update_idletasks()
        messagebox.showinfo("Erfolg", "✅ Cache erfolgreich gelöscht.")
    except Exception as e:
        messagebox.showerror("Fehler", str(e))
    finally:
        window.destroy()  # Fenster schließen, wenn abgeschlossen

# Funktion: DNS flush
def flush_dns():
    # Neues Fenster mit Ladebalken öffnen
    show_progress("🔄 DNS-Cache wird geleert", "Bitte warten, der DNS-Cache wird geleert.")
    subprocess.run("ipconfig /flushdns", shell=True)
    # Ladebalken fortsetzen
    progress_bar['value'] = 100
    window.update_idletasks()
    messagebox.showinfo("Erledigt", "🌐 DNS-Cache wurde erfolgreich geleert.")
    window.destroy()  # Fenster schließen

# Funktion: Gruppenrichtlinien aktualisieren
def update_gp():
    # Neues Fenster mit Ladebalken öffnen
    show_progress("🔄 Gruppenrichtlinien werden aktualisiert", "Bitte warten, Gruppenrichtlinien werden aktualisiert.")
    subprocess.run("gpupdate /force", shell=True)
    # Ladebalken fortsetzen
    progress_bar['value'] = 100
    window.update_idletasks()
    messagebox.showinfo("Erledigt", "🛠️ Gruppenrichtlinien erfolgreich aktualisiert.")
    window.destroy()  # Fenster schließen

# Funktion: Neustart
def restart_pc():
    # Bestätigung, bevor Neustart durchgeführt wird
    confirm = messagebox.askyesno("Neustart", "PC jetzt neustarten? Dies könnte einige Sekunden dauern.")
    if confirm:
        # Neues Fenster mit Ladebalken öffnen
        show_progress("🔄 Neustart des PCs", "Der Computer wird neu gestartet. Speichern Sie Ihre Arbeit.")
        os.system("shutdown /r /t 3")
        progress_bar['value'] = 100
        window.update_idletasks()
        window.destroy()  # Fenster schließen

# Funktion: Updates prüfen
def check_updates():
    # Neues Fenster mit Ladebalken öffnen
    show_progress("🔄 Es wird nach Windows-Updates gesucht", "Bitte warten, wir prüfen auf Updates. Dies kann einige Minuten dauern.")
    subprocess.run("winget upgrade --all", shell=True)
    # Ladebalken fortsetzen
    progress_bar['value'] = 100
    window.update_idletasks()
    messagebox.showinfo("Updates", "📦 Updateprüfung abgeschlossen.")
    window.destroy()  # Fenster schließen

# Funktion: Ladebalken und Fortschrittsbeschreibung anzeigen
def show_progress(title, description):
    global window, progress_bar
    window = tk.Toplevel()  # Erstelle ein neues Fenster (Popup)
    window.title(title)
    window.geometry("300x150")
    window.configure(bg="#f4f4f4")
    
    # Beschreibung hinzufügen
    label = tk.Label(window, text=description, font=("Segoe UI", 10), bg="#f4f4f4", fg="#333")
    label.pack(pady=10)

    # Ladebalken
    progress_bar = ttk.Progressbar(window, length=250, mode='indeterminate')
    progress_bar.pack(pady=10)
    progress_bar.start()  # Starten des Ladebalkens

    # Fenster im Vordergrund halten
    window.attributes('-topmost', True)

# GUI
root = tk.Tk()
root.title("🧰 Systemwartung")
root.geometry("420x360")
root.configure(bg="#f4f4f4")

# Immer im Vordergrund halten
root.attributes('-topmost', True)

# Optional: Icon setzen
try:
    root.iconbitmap("icon.ico")
except:
    pass  # Falls kein Icon vorhanden

# Überschrift
tk.Label(
    root,
    text="🧰 Systemwartung",
    font=("Segoe UI", 16, "bold"),
    bg="#f4f4f4",
    fg="#333",
    anchor="w"
).pack(padx=20, pady=(15, 10), fill="x")

# Stil für alle Buttons (abgerundete Ecken)
def make_button(text, command):
    return tk.Button(
        root,
        text=text,
        command=command,
        anchor="w",  # Links ausgerichtet (Icon + Text)
        justify="left",
        font=("Segoe UI", 11),
        width=40,
        bg="#e0e0e0",
        fg="#111",
        relief="solid",  # Relief auf "solid" gesetzt
        bd=1,  # Minimale Dicke des Rahmens (1px)
        padx=10,
        pady=6,  # Vertikaler Abstand für größere Buttons
        highlightthickness=0,  # Keine Umrandung um den Button
        overrelief="sunken"
    )

# Buttons platzieren
make_button("🧹  Cache löschen", clear_cache).pack(pady=4)
make_button("🌐  DNS-Cache leeren", flush_dns).pack(pady=4)
make_button("🛠️  Gruppenrichtlinien aktualisieren", update_gp).pack(pady=4)
make_button("📦  Windows Updates prüfen", check_updates).pack(pady=4)

# Trennlinie + Beenden-Button (abgerundet und mit Abstand oben)
beenden_button = make_button("❌  Beenden", root.quit)
beenden_button.config(bg="#f44336", fg="#fff", relief="raised")
beenden_button.pack(pady=(20, 10))  # Mehr Abstand nach oben

# Start GUI
root.mainloop()
