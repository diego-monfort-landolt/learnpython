import os
import datetime
import subprocess
import time
import glob
import tkinter as tk
from tkinter import messagebox
import threading

REPO_PATH = r"C:\Users\lando\OneDrive\Desktop\tests\pythonCurso"

def git_run(args):
    subprocess.run(["git"] + args, cwd=REPO_PATH, check=True)

def make_commit(i):
    filename = os.path.join(REPO_PATH, f"dummy_{datetime.date.today()}_{i}.txt")
    with open(filename, "w", encoding="utf-8") as f:
        f.write(f"Commit Nummer {i} am {datetime.datetime.now()}")
    git_run(["add", filename])
    commit_message = f"Automatischer Commit am {datetime.date.today()} #{i}"
    git_run(["commit", "-m", commit_message])

def push_changes():
    git_run(["push"])

def delete_dummy_files():
    pattern = os.path.join(REPO_PATH, "dummy_*.txt")
    files = glob.glob(pattern)
    for file in files:
        os.remove(file)
    git_run(["commit", "-m", "Script wurde erfolgreich beendet"])
    push_changes()

def run_commits(num_commits, repeat_interval=None):
    for i in range(1, num_commits + 1):
        make_commit(i)
        time.sleep(2)
    push_changes()
    delete_dummy_files()
    if repeat_interval:
        threading.Timer(repeat_interval * 60, lambda: run_commits(num_commits, repeat_interval)).start()

def schedule_task(num_commits, start_time, repeat_interval):
    now = datetime.datetime.now()
    target_time = datetime.datetime.combine(now.date(), datetime.datetime.strptime(start_time, "%H:%M").time())
    if target_time < now:
        target_time += datetime.timedelta(days=1)
    delay = (target_time - now).total_seconds()
    threading.Timer(delay, lambda: run_commits(num_commits, repeat_interval)).start()
    messagebox.showinfo("Geplant", f"Task startet um {start_time}")

def start_script():
    try:
        num_commits = int(entry_commits.get())
        start_time = entry_time.get()
        repeat_interval = entry_repeat.get()
        repeat_interval = int(repeat_interval) if repeat_interval else None
        schedule_task(num_commits, start_time, repeat_interval)
    except ValueError:
        messagebox.showerror("Fehler", "Bitte gültige Werte eingeben.")

# GUI
root = tk.Tk()
root.title("Git Auto Commit Tool")

tk.Label(root, text="Anzahl der Commits:").grid(row=0, column=0)
entry_commits = tk.Entry(root)
entry_commits.grid(row=0, column=1)

tk.Label(root, text="Startzeit (HH:MM):").grid(row=1, column=0)
entry_time = tk.Entry(root)
entry_time.grid(row=1, column=1)

tk.Label(root, text="Wiederholung (Minuten, optional):").grid(row=2, column=0)
entry_repeat = tk.Entry(root)
entry_repeat.grid(row=2, column=1)

tk.Button(root, text="Starten", command=start_script).grid(row=3, columnspan=2)

root.mainloop()
