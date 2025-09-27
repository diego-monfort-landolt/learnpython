import os
import threading
import tkinter as tk
from tkinter import filedialog, messagebox
from tkinter import ttk
import subprocess
import platform

# Farben für dunkles Design
BG = "#1e1e1e"
FG = "#dcdcdc"
ENTRY_BG = "#2d2d2d"
BTN_BG = "#3c3c3c"
ACCENT = "#5c5cff"

search_thread = None
stop_search = False
results = []

def browse_folder():
    folder = filedialog.askdirectory()
    path_var.set(folder)

def start_search():
    global search_thread, stop_search, results
    stop_search = False
    results = []
    result_list.delete(0, tk.END)
    progress.start()
    search_button.config(state=tk.DISABLED)
    cancel_button.config(state=tk.NORMAL)
    search_thread = threading.Thread(target=search_files)
    search_thread.start()

def cancel_search():
    global stop_search
    stop_search = True
    progress.stop()
    search_button.config(state=tk.NORMAL)
    cancel_button.config(state=tk.DISABLED)

def search_files():
    search_term = search_var.get().strip()
    search_path = path_var.get().strip() or "/"

    if not search_term:
        messagebox.showwarning("Fehlende Eingabe", "Bitte gib einen Suchbegriff ein.")
        cancel_search()
        return

    for root, dirs, files in os.walk(search_path):
        if stop_search:
            break
        for file in files:
            if stop_search:
                break
            if search_term.lower() in file.lower():
                full_path = os.path.join(root, file)
                results.append(full_path)
                result_list.insert(tk.END, full_path)

    progress.stop()
    search_button.config(state=tk.NORMAL)
    cancel_button.config(state=tk.DISABLED)

def open_selected(event):
    selection = result_list.curselection()
    if selection:
        path = result_list.get(selection[0])
        try:
            if platform.system() == "Windows":
                os.startfile(path)
            elif platform.system() == "Darwin":
                subprocess.call(["open", path])
            else:
                subprocess.call(["xdg-open", path])
        except Exception as e:
            messagebox.showerror("Fehler beim Öffnen", str(e))

# GUI Setup
root = tk.Tk()
root.title("Elegante Dateisuche")
root.geometry("720x540")
root.configure(bg=BG)

# Style für ttk
style = ttk.Style()
style.theme_use("clam")
style.configure("TProgressbar", troughcolor=ENTRY_BG, background=ACCENT, bordercolor=ENTRY_BG, lightcolor=ACCENT, darkcolor=ACCENT)

# Eingabefelder
frame = tk.Frame(root, bg=BG)
frame.pack(pady=20)

path_var = tk.StringVar()
search_var = tk.StringVar()

tk.Label(frame, text="Pfad:", bg=BG, fg=FG).grid(row=0, column=0, sticky="w", padx=5)
path_entry = tk.Entry(frame, textvariable=path_var, width=50, bg=ENTRY_BG, fg=FG, insertbackground=FG)
path_entry.grid(row=0, column=1, padx=5)
browse_btn = tk.Button(frame, text="Durchsuchen", command=browse_folder, bg=BTN_BG, fg=FG)
browse_btn.grid(row=0, column=2, padx=5)

tk.Label(frame, text="Suchbegriff:", bg=BG, fg=FG).grid(row=1, column=0, sticky="w", padx=5, pady=10)
search_entry = tk.Entry(frame, textvariable=search_var, width=50, bg=ENTRY_BG, fg=FG, insertbackground=FG)
search_entry.grid(row=1, column=1, padx=5, pady=10)

# Buttons
btn_frame = tk.Frame(root, bg=BG)
btn_frame.pack(pady=5)

search_button = tk.Button(btn_frame, text="Suchen", command=start_search, bg=ACCENT, fg="white", width=20)
search_button.pack(side=tk.LEFT, padx=10)

cancel_button = tk.Button(btn_frame, text="Abbrechen", command=cancel_search, bg=BTN_BG, fg=FG, width=20, state=tk.DISABLED)
cancel_button.pack(side=tk.LEFT, padx=10)

# Ladeindikator
progress = ttk.Progressbar(root, mode="indeterminate", length=300)
progress.pack(pady=10)

# Ergebnisfeld (Listbox mit Klickfunktion)
tk.Label(root, text="Ergebnisse (klickbar):", bg=BG, fg=FG).pack(pady=(10, 0))
result_list = tk.Listbox(root, height=15, bg=ENTRY_BG, fg=FG, selectbackground=ACCENT, activestyle="none")
result_list.pack(fill=tk.BOTH, expand=True, padx=10, pady=5)
result_list.bind("<Double-Button-1>", open_selected)

root.mainloop()
