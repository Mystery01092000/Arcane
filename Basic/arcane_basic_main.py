from sys import platform
import os
import sounddevice as sd
from scipy.io.wavfile import write

from Basic.email_work import send_plain_text_mail
from Basic.google_search import search_google
from Basic.open_google_chrome import chrome
from playsound import playsound

from Basic.seach_wikipedia import wiki_search
from Basic.text_to_audio import talk


def listener(count):
    fs = 44100  # Sample rate
    seconds = 10  # Duration of recording
    myrecording = sd.rec(int(seconds * fs), samplerate=fs, channels=2)
    sd.wait()  # Wait until recording is finished
    write('recording/output{}.wav'.format(count), fs, myrecording)


def speaker(count):
    playsound("recording/output{}.wav".format(count))


if __name__ == "__main__":
    print("WELCOME TO COMMAND LINE OF ARCANE BOT")
    count_recording = 0
    print("THERE ARE A LOTS OF DIFFERENT FUNCTIONALITY I CAN PERFORM FOR YOU")
    print("PLEASE GUIDE ME, AND I WILL HELP YOU!")
    #parent_dir = "C:/Users/prana/PycharmProjects/Arcane/Basic"
    #directory = "recording"

    #path = os.path.join(parent_dir, directory)

    #os.mkdir(path)
    #os.chmod(path, 777)
    platform_os = platform
    #for i in range(2):
    #    listener(count_recording)
    #    speaker(count_recording)
    #    count_recording = count_recording + 1
    # chrome(platform_os) #To open chrome
    # search_google("Search what you want to search") #this command will search and open in chrome
    #search_google("Open YouTube")
    talk("Hello arcane! How are you")
    #send_plain_text_mail()
    wiki_search("KILL")
    #os.remove(path)