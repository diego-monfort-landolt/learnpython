import tkinter as tk
from tkinter import ttk
import webbrowser
import difflib
from collections import Counter
import re

# Temporärer Verlauf (nur im RAM)
verlauf = []
def finde_aehnliche_suchen(suchbegriff):
    if not verlauf:
        return []
    return difflib.get_close_matches(suchbegriff, verlauf, n=3, cutoff=0.4)

def extrahiere_keywords(verlauf):
    text = " ".join(verlauf).lower()
    # Nur Wörter mit mind. 3 Buchstaben, keine Zahlen/Symbole
    woerter = re.findall(r'\b[a-zäöüß]{3,}\b', text)
    haeufigkeit = Counter(woerter)
    return haeufigkeit.most_common(5)  # Top 5

def suche():
    suchbegriff = eingabe.get().strip()
    if not suchbegriff:
        return
    
    verlauf.append(suchbegriff)
    
    textfeld.configure(state="normal")
    textfeld.delete("1.0", tk.END)
    textfeld.insert(tk.END, f"🔍 Deine Suche: {suchbegriff}\n")
    
    # Ähnliche frühere Suchen
    vorschlaege = finde_aehnliche_suchen(suchbegriff)
    if vorschlaege:
        textfeld.insert(tk.END, "\n🧠 Ähnliche frühere Suchen:\n")
        for v in vorschlaege:
            textfeld.insert(tk.END, f"• {v}\n")
    
    # Beste Keywords
    keywords = extrahiere_keywords(verlauf)
    if keywords:
        textfeld.insert(tk.END, "\n📌 Top-Keywords bisher:\n")
        for wort, anzahl in keywords:
            textfeld.insert(tk.END, f"- {wort} ({anzahl}x)\n")
    
    textfeld.configure(state="disabled")
    
    # Google öffnen
    url = f"https://www.google.com/search?q={suchbegriff.replace(' ', '+')}"
    webbrowser.open(url)
    
    eingabe.delete(0, tk.END)

# Fenster
root = tk.Tk()
root.title("🔎 Suchassistent mit Keywords (nur temporär)")
root.geometry("520x400")
root.resizable(False, False)

# Moderner Stil
style = ttk.Style()
style.theme_use("clam")

ttk.Label(root, text="Suchbegriff eingeben:", font=("Segoe UI", 11)).pack(pady=(15, 5))

eingabe = ttk.Entry(root, width=50, font=("Segoe UI", 11))
eingabe.pack(pady=5)

ttk.Button(root, text="Suchen", command=suche).pack(pady=5)

textfeld = tk.Text(root, height=15, width=65, wrap="word", font=("Segoe UI", 10))
textfeld.pack(padx=10, pady=10)
textfeld.configure(state="disabled")

root.mainloop()