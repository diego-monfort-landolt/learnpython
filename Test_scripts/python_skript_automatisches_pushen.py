import os
import datetime
import subprocess
import time
import glob
import schedule

REPO_PATH = r"C:\Users\lando\Desktop\tests\pythonCurso"

def git_run(args):
    """Git-Befehle mit Fehlerprüfung ausführen."""
    subprocess.run(["git"] + args, cwd=REPO_PATH, check=True)

def make_commit(i):
    """Dummy-Datei erstellen und committen."""
    filename = os.path.join(REPO_PATH, f"dummy_{datetime.date.today()}_{i}.txt")
    with open(filename, "w", encoding="utf-8") as f:
        f.write(f"Commit Nummer {i} am {datetime.datetime.now()}")
    git_run(["add", filename])
    commit_message = f"Automatischer Commit am {datetime.date.today()} #{i}"
    git_run(["commit", "-m", commit_message])

def push_changes():
    """Änderungen ins Remote-Repo pushen."""
    git_run(["push"])

def delete_dummy_files():
    """Alle Dummy-Dateien löschen und committen."""
    pattern = os.path.join(REPO_PATH, "dummy_*.txt")
    files = glob.glob(pattern)
    if not files:
        print("Keine Dummy-Dateien zum Löschen gefunden.")
        return
    for file in files:
        os.remove(file)
    git_run(["commit", "-m", "Script wurde nun erfolgreich beendet"])
    push_changes()

def main():
    print(f"Starte Commit-Prozess um {datetime.datetime.now()}")
    for i in range(1, 13):  # 12 Commits
        make_commit(i)
        time.sleep(2)
    push_changes()
    delete_dummy_files()
    print(f"Prozess beendet um {datetime.datetime.now()}")

# Zeitplan festlegen
schedule.every().day.at("09:00").do(main)
schedule.every().day.at("16:00").do(main)

if __name__ == "__main__":
    print("Script läuft und wartet auf 09:00 und 16:00 Uhr...")
    while True:
        schedule.run_pending()
        time.sleep(1)
