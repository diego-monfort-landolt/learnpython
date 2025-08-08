import os
import datetime
import subprocess
import time

# Lokaler Pfad zum geklonten Repo
REPO_PATH = r"C:\Users\lando\Desktop\tests\pythonCurso"  # <-- anpassen!

def git_run(args):
    """Hilfsfunktion zum Ausführen von Git-Befehlen mit Fehlerprüfung."""
    subprocess.run(["git"] + args, cwd=REPO_PATH, check=True)

def make_commit(i):
    """Erstellt eine Dummy-Datei und committed sie."""
    filename = os.path.join(REPO_PATH, f"dummy_{datetime.date.today()}_{i}.txt")
    with open(filename, "w") as f:
        f.write(f"Commit Nummer {i} am {datetime.datetime.now()}")
    git_run(["add", filename])
    commit_message = f"Automatischer Commit am {datetime.date.today()} #{i}"
    git_run(["commit", "-m", commit_message])

def push_changes():
    """Push alle Commits ins Remote."""
    git_run(["push"])

def daily_commits():
    """Erstellt 9 Commits pro Tag."""
    for i in range(1, 10):
        make_commit(i)
        time.sleep(2)  # kleine Pause zwischen Commits, wirkt natürlicher
    push_changes()

if __name__ == "__main__":
    while True:
        print(f"Starte Commits für {datetime.date.today()}")
        daily_commits()
        print("Fertig für heute, warte bis morgen...")
        # Warte bis morgen 00:01 Uhr
        tomorrow = datetime.datetime.now() + datetime.timedelta(days=1)
        next_run = datetime.datetime.combine(tomorrow.date(), datetime.time(0, 1))
        time.sleep((next_run - datetime.datetime.now()).total_seconds())
