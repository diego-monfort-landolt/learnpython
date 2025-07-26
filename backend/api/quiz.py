import requests
import html

def get_question():
    url = "https://opentdb.com/api.php?amount=1&type=multiple"
    response = requests.get(url)
    data = response.json()

    if data['response_code'] == 0:
        frage_daten = data['results'][0]
        frage = html.unescape(frage_daten['question'])
        richtige_antwort = html.unescape(frage_daten['correct_answer'])
        falsche_antworten = [html.unescape(ans) for ans in frage_daten['incorrect_answers']]
        alle_antworten = falsche_antworten + [richtige_antwort]
        import random
        random.shuffle(alle_antworten)

        return frage, richtige_antwort, alle_antworten
    else:
        return None, None, None

def spiel():
    punkte = 0
    print("🎮 Willkommen zum Trivia-Quiz!")
    print("Drücke Strg+C zum Beenden.\n")

    try:
        while True:
            frage, richtig, antworten = get_question()
            if frage is None:
                print("Fehler beim Abrufen der Frage.")
                break
            print("Frage:")
            print(frage)
            for i, ans in enumerate(antworten):
                print(f"{i+1}. {ans}")

            wahl = input("Deine Antwort (1-4): ").strip()
            if not wahl.isdigit() or not (1 <= int(wahl) <= 4):
                print("Ungültige Eingabe. Bitte 1-4 eingeben.\n")
                continue

            if antworten[int(wahl)-1] == richtig:
                print("✅ Richtig!\n")
                punkte += 1
            else:
                print(f"❌ Falsch! Die richtige Antwort war: {richtig}\n")

            print(f"🔢 Punktestand: {punkte}\n")

    except KeyboardInterrupt:
        print("\n🛑 Spiel beendet. Dein Punktestand: ", punkte)

if __name__ == "__main__":
    spiel()