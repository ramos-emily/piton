import sys
import time

lyrics= [
    ("pode me dizer como é o seu nome? ", 2),
    ("alexandre", 2.5),
    ("hmmm", 0.5),
    ("você ainda fala!", 1.7),
    ("falo sim sinhô...", 1),
    ("eu quero ir pra casa da minha mamãe", 10),
]

def print_lyrics():
    for line, display_time in lyrics:
        print(line)
        time.sleep(display_time)
        print('')

print_lyrics()