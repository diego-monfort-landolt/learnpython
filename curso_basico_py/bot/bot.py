import smtplib
from bs4 import BeautifulSoup
from dotenv import load_dotenv
import requests
from time import sleep
import os

URL = "https://www.binance.com/es/price/bitcoin"
OBERGRENZE = 98000
UNTERGRENZE = 80000
load_dotenv()
EMAIL = os.getenv("ALERT_EMAIL")
PASSWORT = os.getenv("ALERT_PASS")
SMTP_SERVER = os.getenv("SMTP_SERVER")
def preis_abfragen():
    headers = {'User-Agent': 'Mozilla/5.0'}
    try:
        seite = requests.get(URL, headers=headers, timeout=10)
        soup = BeautifulSoup(seite.text, 'html.parser')  
        # HINWEIS: Dies ist ein Platzhalter! Im Browser den aktuellen CSS-Selektor prüfen.
        preis_element = soup.find('div', {'class': 'css-12ujz79'})  
        if preis_element:
            text = preis_element.text.strip()
            # Punkt entfernen, falls es Tausendertrennzeichen sind (z. B. „98.000,00“)
            text = text.replace('.', '').replace(',', '.').replace("€", "")
            return float(text)
    except Exception as e:
        print(f"Fehler bei Preisabfrage: {e}")
    return None
def benachrichtigen(preis, richtung):
    nachricht = f"🚨 BTC ist {richtung} {preis:.2f} EUR"
    try:
        with smtplib.SMTP(SMTP_SERVER, 587) as server:
            server.starttls()
            server.login(EMAIL, PASSWORT)
            server.sendmail(EMAIL, EMAIL, f"Subject: Bitcoin Alert\n\n{nachricht}")
        print(nachricht)
    except Exception as e:
        print(f"Fehler beim Senden: {e}")
while True:
    preis = preis_abfragen()
    if preis:
        if preis >= OBERGRENZE:
            benachrichtigen(preis, "gestiegen über 98.000")
        elif preis <= UNTERGRENZE:
            benachrichtigen(preis, "gefallen unter 80.000")
    sleep(5)