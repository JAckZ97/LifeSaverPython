import os
import time
import speech_recognition as sr
from gtts import gTTS
import playsound
# TODO: missing pyaudio module
# https://medium.com/@wagnernoise/installing-pyaudio-on-macos-9a5557176c4d


def talk(text):
    tts = gTTS(text=text, lang="en")
    filename = "voice.mp3"
    tts.save(filename)
    playsound.playsound(filename)


def get_audio():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        audio = r.listen(source)
        said = ""

        try:
            said = r.recognize_google(audio)
            print(said)
        except Exception as e:
            print("Exception: " + str(e))

    return said


talk("hello")
get_audio()
