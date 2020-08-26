from gtts import gTTS
import speech_recognition as sr
from pygame import mixer

def myCommand():

    r = sr.Recognizer()

    with sr.Microphone() as source:

        print("ARCANE is ready.......")

        r.adjust_for_ambient_noise(source, duration=1)

        audio = r.listen(source)

    try:
        command = r.recognize_google(audio).lower()
        print('You said: ' + command + '\n')

    except sr.UnknownValueError:

        print("Your last command couldn't be heard")

        command = myCommand()

    return command