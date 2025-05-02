import os
import subprocess
import tkinter as tk
from tkinter import messagebox
import shutil
import time

# === Funktionen ===

def clear_outlook_cache():
    try:
        paths = [
            os.path.expandvars(r"%LOCALAPPDATA%\Microsoft\Outlook"),
            os.path.expandvars(r"%APPDATA%\Microsoft\Outlook"),
            os.path.expandvars(r"%TEMP%")
        ]
        for path in paths:
            if os.path.exists(path):
                shutil.rmtree(path)
        messagebox.showinfo("Erfolg", "✅ Outlook-Cache gelöscht.")
    except Exception as e:
        messagebox.showerror("Fehler", f"Fehler: {str(e)}")

def create_outlook_profile_and_start():
    try:
        messagebox.showinfo("Profil", "Outlook-Profil wird erstellt.")
        profile = "NewOutlookProfile"
        subprocess.run(f"outlook.exe /Profile {profile}", shell=True)
        time.sleep(10)
        subprocess.run(f"start outlook.exe /profile {profile}", shell=True)
    except Exception as e:
        messagebox.showerror("Fehler", str(e))

def flush_dns():
    subprocess.run("ipconfig /flushdns", shell=True)
    messagebox.showinfo("Erledigt", "DNS-Cache geleert.")

def update_gp():
    subprocess.run("gpupdate /force", shell=True)
    messagebox.showinfo("Erledigt", "Gruppenrichtlinien aktualisiert.")

def check_updates():
    subprocess.run("winget upgrade --all", shell=True)
    messagebox.showinfo("Updates", "Updates geprüft.")

def quit_app():
    root.quit()

# === GUI ===

root = tk.Tk()
root.title("Systemwartung")
root.geometry("500x500")
root.resizable(False, False)
root.configure(bg="white")

# Icon oben links setzen (optional)
try:
    root.iconbitmap("mein_icon.ico")  # Stelle sicher, dass mein_icon.ico im selben Ordner liegt
except:
    pass

# === Button-Funktion mit Hover ===

def create_button(text, command):
    btn = tk.Button(
        root,
        text=text,
        command=command,
        font=("Segoe UI Emoji", 11),
        width=45,
        height=2,
        bg="#ffffff",         # Standard-Hintergrund
        fg="#333333",         # Textfarbe
        activeforeground="#000000",
        relief="groove",
        bd=2,
        anchor="w",           # Text links im Button
        padx=10
    )

    # Hover-Farben
    hover_bg = "#e6e6e6"
    normal_bg = "#ffffff"

    # Hover-Events
    def on_enter(e): btn['background'] = hover_bg
    def on_leave(e): btn['background'] = normal_bg

    btn.bind("<Enter>", on_enter)
    btn.bind("<Leave>", on_leave)

    btn.pack(pady=8, padx=20, anchor="w", fill="x")

# === Buttons erstellen ===

create_button("🧹  Outlook-Cache löschen", clear_outlook_cache)
create_button("🌐  DNS-Cache leeren", flush_dns)
create_button("🛠️  Gruppenrichtlinien aktualisieren", update_gp)
create_button("📦  Windows Updates prüfen", check_updates)
create_button("💼  Neues Outlook-Profil starten", create_outlook_profile_and_start)

# === Beenden-Button mit eigenem Hover ===

quit_btn = tk.Button(root, text="❌  Beenden", font=("Segoe UI", 11), width=20,
                     bg="#d9534f", fg="white", command=quit_app)
quit_btn.pack(pady=20)

def on_enter_quit(e): quit_btn['bg'] = "#c9302c"
def on_leave_quit(e): quit_btn['bg'] = "#d9534f"

quit_btn.bind("<Enter>", on_enter_quit)
quit_btn.bind("<Leave>", on_leave_quit)

# Start GUI
root.mainloop()
