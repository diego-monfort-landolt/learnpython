import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
import os
from dotenv import load_dotenv

# -----------------------
# .env laden (enthält E-Mail & Passwort)
# -----------------------
load_dotenv()
smtp_user = os.getenv("SMTP_USER")
smtp_pass = os.getenv("SMTP_PASS")

# Empfängeradresse (Demo)
recipient = "empfaenger@beispiel.de"

# SMTP-Server von Ethereal (für Tests)
smtp_server = "smtp.ethereal.email"
smtp_port = 587

# -----------------------
# E-MAIL-INHALT (gestylt)
# -----------------------

msg = MIMEMultipart("alternative")
msg['Subject'] = "🚨 Dringende Mitteilung: Bitte sofort prüfen!"
msg['From'] = f"Testsender <{smtp_user}>"
msg['To'] = recipient

# HTML-Inhalt
html_content = """
<html>
  <body style="font-family: Arial, sans-serif; background-color: #f9f9f9; padding: 20px;">
    <h2 style="color: #d32f2f;">🚨 Wichtige Benachrichtigung</h2>
    <p style="font-size: 16px;">
      Dies ist eine <b style="color: #d32f2f;">automatisierte Testnachricht</b>, gesendet über ein Python-Script.<br><br>
      <span style="background-color: #fff3cd; padding: 10px; border: 1px solid #ffeeba; display: block; margin-top: 10px;">
        👉 <b>Bitte ignorieren Sie diese E-Mail nicht!</b><br>
        Sie dient zu Testzwecken und demonstriert HTML-E-Mails mit Stil.
      </span>
    </p>
    <hr>
    <p style="font-size: 12px; color: #888;">Gesendet von einem automatisierten Script • Kein echtes Anliegen</p>
  </body>
</html>
"""

# Nur-Text-Version (Backup)
text_content = "Wichtige Testnachricht über Python-Script.\nBitte prüfen Sie diese Nachricht umgehend."

# Inhalte anhängen
msg.attach(MIMEText(text_content, "plain"))
msg.attach(MIMEText(html_content, "html"))

# -----------------------
# Senden der E-Mail
# -----------------------

try:
    with smtplib.SMTP(smtp_server, smtp_port) as server:
        server.starttls()
        server.login(smtp_user, smtp_pass)
        server.send_message(msg)
        print("✅ Test-E-Mail erfolgreich gesendet!")
except Exception as e:
    print(f"❌ Fehler beim Senden: {e}")
