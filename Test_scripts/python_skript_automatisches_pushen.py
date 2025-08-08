import os
import datetime
import subprocess
import time

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

def main():
    for i in range(1, 13):  # 12 Commits
        make_commit(i)
        time.sleep(2)  # kleine Pause zwischen den Commits
    push_changes()
    print(f"Fertig: {datetime.date.today()} – 12 Commits + Push ausgeführt.")

if __name__ == "__main__":
    main()
