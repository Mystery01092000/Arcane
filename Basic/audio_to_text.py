import speech_recognition as sr

def audio_to_text(aud):
    au = sr.AudioFile("../recording/output0.wav")
    sr.recognize_api(au)


audio_to_text("Hello")