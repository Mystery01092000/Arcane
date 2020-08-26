from gtts import gTTS
import speech_recognition as sr
from pygame import mixer
import my_commands
import speech_reco
import random


def arcane(command):
    errors = [
        "I don\'t know what you mean!",
        "Excuse me?",
        "Can you please repeat that?"
    ]

