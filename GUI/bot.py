import random
import nltk
from nltk.chat.util import Chat, reflections

pairs = [
    [r"Hallo|Hi|Hey", ["Hallo! Wie kann ich helfen?", "Hey! Schön, dich zu sehen!"]],
    [r"Wie geht es dir?", ["Mir geht es gut, danke!", "Ich bin ein Programm, aber danke der Nachfrage!"]],
    [r"(.*) Wetter (.*)", ["Ich kann das Wetter nicht checken, aber es gibt Wetter-APIs!"]],
]

chatbot = Chat(pairs, reflections)
while True:
    user_input = input("Du: ")
    response = chatbot.respond(user_input)
    print("Bot:", response)
