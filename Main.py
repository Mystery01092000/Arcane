from gtts import gTTS
import speech_recognition as sr
from pygame import mixer
from my_commands import *
from speech_reco import *
import random


def arcane(command):
    errors = [
        "I don\'t know what you mean!",
        "Excuse me?",
        "Can you please repeat that?"
    ]

    if 'Hello' in command:
        talk("Hello! I am Arcane. How can I help you?")

    else:
        error = random.choice(errors)
        talk(error)

talk("Arcane here!")

while(True):
    arcane(myCommand())

