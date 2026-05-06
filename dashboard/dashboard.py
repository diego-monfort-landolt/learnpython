import tkinter as tk
from tkinter import ttk, messagebox, filedialog
from collections import Counter
import matplotlib
matplotlib.use("TkAgg")
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from matplotlib.figure import Figure
import os
import pandas as pd
import datetime

# -----------------------------
# Einfache, lokale "Datenhaltung"
# -----------------------------
DATA_FILE = "patienten_eintraege.txt"

class MedicalDashboardApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Medical Dashboard | Demo | Diego Monfort")
        self.root.geometry("900x650")

        # Datenstruktur: Liste von Dicts
        self.entries = []
        self.filtered_entries = []

        self._build_ui()
        self._load_from_file()
        self._refresh_list()
        self._update_donut()

    # -----------------------------
    # UI Aufbau
    # -----------------------------
    def _build_ui(self):
        main_frame = ttk.Frame(self.root, padding=10)
        main_frame.pack(fill="both", expand=True)

        input_frame = ttk.LabelFrame(main_frame, text="Neuer Eintrag", padding=10)
        input_frame.pack(fill="x")

        # Name
        ttk.Label(input_frame, text="Name:").grid(row=0, column=0, sticky="w")
        self.name_var = tk.StringVar()
        self.name_entry = ttk.Entry(input_frame, textvariable=self.name_var, width=30)
        self.name_entry.grid(row=0, column=1, sticky="w", padx=5, pady=2)

        # Kategorie
        ttk.Label(input_frame, text="Kategorie:").grid(row=1, column=0, sticky="w")
        self.category_var = tk.StringVar()
        self.category_combo = ttk.Combobox(
            input_frame,
            textvariable=self.category_var,
            values=["Verletzungen", "Herzprobleme", "Wundenpflege"],
            state="readonly",
            width=27
        )
        self.category_combo.grid(row=1, column=1, sticky="w", padx=5, pady=2)
        self.category_combo.current(0)

        # Geschlecht
        ttk.Label(input_frame, text="Geschlecht:").grid(row=2, column=0, sticky="w")
        self.gender_var = tk.StringVar()
        self.gender_combo = ttk.Combobox(
            input_frame,
            textvariable=self.gender_var,
            values=["Mann", "Frau"],
            state="readonly",
            width=27
        )
        self.gender_combo.grid(row=2, column=1, sticky="w", padx=5, pady=2)
        self.gender_combo.current(0)

        # Speichern
        save_button = ttk.Button(input_frame, text="Eintrag speichern", command=self._save_entry)
        save_button.grid(row=3, column=0, sticky="w", pady=8)

        # CSV/Excel Import
        import_button = ttk.Button(input_frame, text="CSV/Excel importieren", command=self._import_users)
        import_button.grid(row=4, column=0, sticky="w", pady=5)

        # Verlauf anzeigen
        history_button = ttk.Button(input_frame, text="Verlauf anzeigen", command=self._show_history)
        history_button.grid(row=5, column=0, sticky="w", pady=5)

        ttk.Separator(main_frame, orient="horizontal").pack(fill="x", pady=10)

        # Unterer Bereich
        bottom_frame = ttk.Frame(main_frame)
        bottom_frame.pack(fill="both", expand=True)

        # Links: Suche + Liste
        left_frame = ttk.Frame(bottom_frame)
        left_frame.pack(side="left", fill="both", expand=True, padx=(0, 10))

        search_frame = ttk.LabelFrame(left_frame, text="Suche", padding=10)
        search_frame.pack(fill="x")

        ttk.Label(search_frame, text="Suche nach Name oder Kategorie:").pack(anchor="w")
        self.search_var = tk.StringVar()
        self.search_var.trace_add("write", lambda *args: self._apply_search())
        search_entry = ttk.Entry(search_frame, textvariable=self.search_var)
        search_entry.pack(fill="x", pady=3)

        list_frame = ttk.LabelFrame(left_frame, text="Einträge", padding=10)
        list_frame.pack(fill="both", expand=True, pady=(10, 0))

        self.listbox = tk.Listbox(list_frame, height=20)
        self.listbox.pack(side="left", fill="both", expand=True)

        scrollbar = ttk.Scrollbar(list_frame, orient="vertical", command=self.listbox.yview)
        scrollbar.pack(side="right", fill="y")
        self.listbox.config(yscrollcommand=scrollbar.set)

        # Rechts: Donut Chart
        right_frame = ttk.LabelFrame(bottom_frame, text="Übersicht nach Kategorie", padding=10)
        right_frame.pack(side="right", fill="both", expand=True)

        self.figure = Figure(figsize=(4, 4), dpi=100)
        self.ax = self.figure.add_subplot(111)
        self.canvas = FigureCanvasTkAgg(self.figure, master=right_frame)
        self.canvas.get_tk_widget().pack(fill="both", expand=True)

    # -----------------------------
    # Eintrag speichern
    # -----------------------------
    def _save_entry(self):
        name = self.name_var.get().strip()
        category = self.category_var.get().strip()
        gender = self.gender_var.get().strip()

        if not name:
            messagebox.showwarning("Fehlende Eingabe", "Bitte einen Namen eingeben.")
            return

        timestamp = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")

        entry = {
            "name": name,
            "category": category,
            "gender": gender,
            "timestamp": timestamp
        }

        self.entries.append(entry)
        self._save_to_file()
        self._apply_search()
        self._update_donut()

        self.name_var.set("")
        self.category_combo.current(0)
        self.gender_combo.current(0)

    # -----------------------------
    # Suche anwenden
    # -----------------------------
    def _apply_search(self):
        query = self.search_var.get().strip().lower()
        if not query:
            self.filtered_entries = list(self.entries)
        else:
            self.filtered_entries = [
                e for e in self.entries
                if query in e["name"].lower() or query in e["category"].lower()
            ]
        self._refresh_list()

    # -----------------------------
    # Liste aktualisieren
    # -----------------------------
    def _refresh_list(self):
        self.listbox.delete(0, tk.END)
        for idx, entry in enumerate(self.filtered_entries, start=1):
            text = f"{idx}. {entry['name']} – {entry['category']} ({entry['gender']})"
            self.listbox.insert(tk.END, text)

    # -----------------------------
    # Donut-Chart aktualisieren
    # -----------------------------
    def _update_donut(self):
        self.ax.clear()
        if not self.entries:
            self.ax.text(0.5, 0.5, "Keine Daten", ha="center", va="center")
            self.ax.axis("off")
            self.canvas.draw()
            return

        categories = [e["category"] for e in self.entries]
        counts = Counter(categories)

        labels = list(counts.keys())
        sizes = list(counts.values())

        wedges, texts = self.ax.pie(sizes, labels=labels, startangle=90)
        centre_circle = matplotlib.patches.Circle((0, 0), 0.70, fc="white")
        self.ax.add_artist(centre_circle)
        self.ax.axis("equal")
        self.canvas.draw()

    # -----------------------------
    # CSV/Excel Import
    # -----------------------------
    def _import_users(self):
        file_path = filedialog.askopenfilename(
            title="CSV oder Excel Datei wählen",
            filetypes=[("CSV Dateien", "*.csv"), ("Excel Dateien", "*.xlsx *.xls")]
        )

        if not file_path:
            return

        try:
            if file_path.endswith(".csv"):
                df = pd.read_csv(file_path)
            else:
                df = pd.read_excel(file_path)

            required = {"name", "category", "gender"}
            if not required.issubset(df.columns):
                messagebox.showerror("Fehler", "Die Datei muss die Spalten: name, category, gender enthalten.")
                return

            for _, row in df.iterrows():
                entry = {
                    "name": str(row["name"]).strip(),
                    "category": str(row["category"]).strip(),
                    "gender": str(row["gender"]).strip(),
                    "timestamp": datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
                }
                self.entries.append(entry)

            self._save_to_file()
            self._apply_search()
            self._update_donut()

            messagebox.showinfo("Import erfolgreich", f"{len(df)} Einträge wurden importiert.")

        except Exception as ex:
            messagebox.showerror("Fehler beim Import", f"Die Datei konnte nicht verarbeitet werden:\n{ex}")

    # -----------------------------
    # Verlauf anzeigen
    # -----------------------------
    def _show_history(self):
        history_win = tk.Toplevel(self.root)
        history_win.title("User Verlauf")
        history_win.geometry("500x400")

        frame = ttk.Frame(history_win, padding=10)
        frame.pack(fill="both", expand=True)

        listbox = tk.Listbox(frame)
        listbox.pack(fill="both", expand=True)

        for e in self.entries:
            ts = e.get("timestamp", "")
            text = f"{ts} – {e['name']} ({e['category']}, {e['gender']})"
            listbox.insert(tk.END, text)

    # -----------------------------
    # Daten speichern
    # -----------------------------
    def _save_to_file(self):
        try:
            with open(DATA_FILE, "w", encoding="utf-8") as f:
                for e in self.entries:
                    line = f"{e['name']}|{e['category']}|{e['gender']}|{e.get('timestamp','')}\n"
                    f.write(line)
        except OSError as ex:
            messagebox.showerror("Fehler beim Speichern", f"Datei konnte nicht gespeichert werden:\n{ex}")

    # -----------------------------
    # Daten laden
    # -----------------------------
    def _load_from_file(self):
        if not os.path.exists(DATA_FILE):
            return
        try:
            with open(DATA_FILE, "r", encoding="utf-8") as f:
                for line in f:
                    parts = line.strip().split("|")
                    if len(parts) == 4:
                        name, category, gender, timestamp = parts
                    else:
                        name, category, gender = parts
                        timestamp = ""
                    self.entries.append({
                        "name": name,
                        "category": category,
                        "gender": gender,
                        "timestamp": timestamp
                    })
            self.filtered_entries = list(self.entries)
        except OSError:
            self.entries = []
            self.filtered_entries = []

# -----------------------------
# Start
# -----------------------------
if __name__ == "__main__":
    root = tk.Tk()
    app = MedicalDashboardApp(root)
    root.mainloop()
