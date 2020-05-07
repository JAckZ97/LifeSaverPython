import os
import time
import speech_recognition as sr
from gtts import gTTS
import playsound


def talk(text):
    tts = gTTS(text=text, lang="en")
    filename = "voice.mp3"
    tts.save(filename)
    playsound.playsound(filename)


def get_audio():
    r = sr.Recognizer()
    mic = sr.Microphone(device_index=0)

    with mic as source:
        r.adjust_for_ambient_noise(source)
        print("listening...")

        audio = r.listen(source)
        saying = ""

        try:
            saying = r.recognize_google(audio)
            print(saying)

        except Exception as e:
            print("Exception: " + str(e))

    return saying


talk("hello")
get_audio()

