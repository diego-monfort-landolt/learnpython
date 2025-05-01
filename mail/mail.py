import smtplib
from email.mime.text import MIMEText

# Text der Email - hier kannst du den Inhalt der Email anpassen
text = 'Hy there! This is a test email. \n\nThis is a test email sent from Python.'

# SMTP-Server und Port - hier kannst du den SMTP-Server und den Port deines Email-Anbieters anpassen
mail= MIMEText(text)
mail['Subject'] = 'Email versendet via Script in python'
mail['from'] = 'Diego <youre-mail@gmail.com>'
mail['to'] = 'empfänger@example.com'

sender = smtplib.SMTP('smtp.gmail.com', 587)
sender.ehlo()
sender.starttls()
sender.ehlo()

# Hier kannst du deine Email-Adresse und dein Passwort eingeben
sender.login('youremailgmail.com, "TEST-PWD"')
sender.send_message(mail);
sender.close()

print("Email sent successfully!") 
  