from sys import platform
import sounddevice as sd
from scipy.io.wavfile import write
from Basic.google_search import search_google
from Basic.open_google_chrome import chrome
from playsound import playsound

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
    platform_os = platform
    for i in range(2):
        listener(count_recording)
        speaker(count_recording)
        count_recording = count_recording + 1
    #chrome(platform_os) #To open chrome
    #search_google("Search what you want to search") #this command will search and open in chrome
    
