
# -*- coding: utf-8 -*-
import os
import time
import subprocess

# ==== Konfiguration ====
APP_NAME = "NeonShell"  # <— hier einfach ändern
SHOW_MATRIX_INTRO = True  # Intro mit „Matrix“-Effekt (abschaltbar)

# ANSI-Farben
RESET = "\033[0m"
GREEN = "\033[92m"
BRIGHT_GREEN = "\033[38;5;46m"
BLACK_BG = "\033[40m"
CYAN = "\033[96m"
MAGENTA = "\033[95m"
YELLOW = "\033[93m"
RED = "\033[91m"
DIM = "\033[2m"
BOLD = "\033[1m"

BANNER = (
    BLACK_BG + BRIGHT_GREEN + BOLD +
    f"\n   _   _                        ____  _          _ _ "
    f"\n  | \\ | | ___  ___  _ __  _   _/ ___|| |__   ___| | |"
    f"\n  |  \\| |/ _ \\/ _ \\| '_ \\| | | \\___ \\| '_ \\ / _ \\ | |"
    f"\n  | |\\  |  __/ (_) | | | | |_| |___) | | | |  __/ | |"
    f"\n  |_| \\_|\\___|\\___/|_| |_|\\__,_|____/|_| |_|\\___|_|_|"
    f"\n                {APP_NAME}"
    + RESET
)

MENU = (
    f"\n{DIM}────────────────────────────────────────────────────────────{RESET}\n"
    f"{BOLD}{CYAN} [1]{RESET} Startmenü/Apps öffnen\n"
    f"{BOLD}{CYAN} [2]{RESET} Windows-Standardprogramme\n"
    f"{BOLD}{CYAN} [3]{RESET} Cache & Wartung\n"
    f"{BOLD}{CYAN} [4]{RESET} Neues CMD-Fenster\n"
    f"{BOLD}{CYAN} [0]{RESET} Beenden\n"
    f"{DIM}────────────────────────────────────────────────────────────{RESET}\n"
)

PROGRAM_MENU = (
    f"\n{DIM}──────── Windows-Programme ────────{RESET}\n"
    f"{BOLD}{CYAN} [1]{RESET} Editor (notepad)\n"
    f"{BOLD}{CYAN} [2]{RESET} Rechner (calc)\n"
    f"{BOLD}{CYAN} [3]{RESET} Paint (mspaint)\n"
    f"{BOLD}{CYAN} [4]{RESET} Explorer (explorer)\n"
    f"{BOLD}{CYAN} [5]{RESET} Systemsteuerung (control)\n"
    f"{BOLD}{CYAN} [6]{RESET} Task-Manager (taskmgr)\n"
    f"{BOLD}{CYAN} [7]{RESET} Eingabeaufforderung (cmd)\n"
    f"{BOLD}{CYAN} [0]{RESET} Zurück\n"
)

CACHE_MENU = (
    f"\n{DIM}──────── Cache & Wartung ────────{RESET}\n"
    f"{BOLD}{YELLOW} [1]{RESET} Temporäre Dateien (%TEMP%) bereinigen\n"
    f"{BOLD}{YELLOW} [2]{RESET} DNS-Cache leeren (ipconfig /flushdns)\n"
    f"{BOLD}{YELLOW} [3]{RESET} Microsoft Store Cache (wsreset)\n"
    f"{BOLD}{YELLOW} [0]{RESET} Zurück\n"
)

def slow_print(text, delay=0.01):
    for ch in text:
        print(ch, end='', flush=True)
        time.sleep(delay)
    print()

def progress_bar(task_name, seconds=2):
    length = 26
    slow_print(f"{DIM}>> {task_name}...{RESET}", 0.02)
    for i in range(length + 1):
        bar = "#" * i + "-" * (length - i)
        print(f"{GREEN}[{bar}] {int((i/length)*100)}%{RESET}", end='\r', flush=True)
        time.sleep(seconds/length)
    print()

def matrix_intro(lines=10, width=44, cycles=80, delay=0.02):
    import random, string
    charset = string.ascii_uppercase + string.digits
    slow_print(f"{DIM}Booting {APP_NAME}…{RESET}", 0.02)
    for _ in range(cycles):
        row = ''.join(random.choice(charset) for _ in range(width))
        print(BRIGHT_GREEN + row + RESET)
        time.sleep(delay)
    print()

def open_start_menu():
    try:
        progress_bar("Öffne Apps-Übersicht")
        subprocess.Popen(["explorer", "shell:AppsFolder"], shell=True)
    except Exception as e:
        print(f"{RED}Fehler: {e}{RESET}")
    try:
        time.sleep(0.5)
        progress_bar("Öffne Startmenü-Ordner")
        subprocess.Popen(["explorer", "shell:StartMenu"], shell=True)
    except Exception as e:
        print(f"{RED}Fehler: {e}{RESET}")

def launch_program(choice: str):
    mapping = {
        '1': 'notepad',
        '2': 'calc',
        '3': 'mspaint',
        '4': 'explorer',
        '5': 'control',
        '6': 'taskmgr',
        '7': 'cmd'
    }
    exe = mapping.get(choice)
    if not exe:
        return
    try:
        progress_bar(f"Starte {exe}")
        subprocess.Popen(exe, shell=True)
    except Exception as e:
        print(f"{RED}Fehler: {e}{RESET}")

def clear_temp():
    temp = os.environ.get('TEMP') or os.environ.get('TMP')
    if not temp:
        print(f"{RED}TEMP-Ordner nicht gefunden.{RESET}")
        return
    slow_print(f"{DIM}Ziel: {temp}{RESET}", 0.01)
    cmd = (
        f'cmd /c "'
        f'del /q /f /s "{temp}\\*" 2>nul & '
        f'for /d %i in ("{temp}\\*") do rd /s /q "%i" 2>nul'
        f'"'
    )
    progress_bar("Lösche temporäre Dateien", seconds=3)
    os.system(cmd)
    print(f"{GREEN}Bereinigung abgeschlossen.{RESET}")

def flush_dns():
    progress_bar("Leere DNS-Cache")
    os.system("ipconfig /flushdns >nul 2>&1")
    print(f"{GREEN}DNS-Cache geleert.{RESET}")

def wsreset():
    progress_bar("Setze Microsoft Store Cache zurück")
    os.system("wsreset.exe >nul 2>&1")
    print(f"{GREEN}wsreset ausgeführt.{RESET}")

def new_cmd_window():
    progress_bar("Öffne neues CMD-Fenster")
    os.system("start cmd")

def clear_screen():
    os.system("cls")

def main():
    clear_screen()
    print(BANNER)
    if SHOW_MATRIX_INTRO:
        matrix_intro()
    slow_print(f"{DIM}Initialisiere Konsole...{RESET}", 0.02)
    time.sleep(0.5)

    while True:
        print(MENU)
        choice = input(f"{BRIGHT_GREEN}{BOLD}> Auswahl: {RESET}")

        if choice == '1':
            open_start_menu()
        elif choice == '2':
            print(PROGRAM_MENU)
            sub = input(f"{BRIGHT_GREEN}{BOLD}> Programm: {RESET}")
            if sub == '0':
                continue
            launch_program(sub)
        elif choice == '3':
            print(CACHE_MENU)
            sub = input(f"{BRIGHT_GREEN}{BOLD}> Aktion: {RESET}")
            if sub == '1':
                print(f"{YELLOW}{BOLD}Warnung:{RESET} Es werden nur temporäre Dateien im %TEMP%-Ordner gelöscht.")
                confirm = input(f"{CYAN}Bestätigen (j/n): {RESET}").strip().lower()
                if confirm == 'j':
                    clear_temp()
                else:
                    print(f"{RED}Abgebrochen.{RESET}")
            elif sub == '2':
                flush_dns()
            elif sub == '3':
                wsreset()
            else:
                continue
        elif choice == '4':
            new_cmd_window()
        elif choice == '0':
            print(f"{MAGENTA}{DIM}Bye.{RESET}")
            break
        else:
            print(f"{RED}Ungültige Auswahl.{RESET}")
        time.sleep(0.4)

if __name__ == '__main__':
    try:
        main()
    except KeyboardInterrupt:
        print(f"\n{RED}Beendet durch Benutzer.{RESET}")

