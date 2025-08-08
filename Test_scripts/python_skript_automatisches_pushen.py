import os
import datetime
import subprocess

REPO_PATH = "http://github.com/diego-monfort-landolt/learnpython"  # Lokaler Pfad zum Git-Repo
COMMIT_MESSAGE = "Automatischer Commit am " + datetime.datetime.now().strftime("%Y-%m-%d")

def make_commit(i):
    filename = os.path.join(REPO_PATH, f"dummy_{i}.txt")
    with open(filename, "w") as f:
        f.write(f"Commit Nummer {i} am {datetime.datetime.now()}")
    subprocess.run(["git", "add", filename], cwd=REPO_PATH)
    subprocess.run(["git", "commit", "-m", f"{COMMIT_MESSAGE} #{i}"], cwd=REPO_PATH)

def push_changes():
    subprocess.run(["git", "push"], cwd=REPO_PATH)

def main():
    for i in range(1, 10):  # 9 Commits
        make_commit(i)
    push_changes()

if __name__ == "__main__":
    main()
