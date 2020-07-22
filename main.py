import speech_recognition as sr
from playsound import playsound
from time import ctime
from gtts import gTTS
import random
import webbrowser
import time
import os

recognize = sr.Recognizer()


def mic_Audio(ask=False):
    with sr.Microphone() as mic:
        if(ask):
            JEXI_speak(ask)
        audio = recognize.listen(mic)
        voice_data=''
        try:
            voice_data = recognize.recognize_google(audio)

        except sr.UnknownValueError:
            JEXI_speak("Sorry cannot understand that")
        except sr.RequestError:
            JEXI_speak("Unavailable")
        return voice_data


def JEXI_speak(audio_str):
    tts = gTTS(text=audio_str,lang='en')
    rand = random.randint(1,10000000)
    audio_file= 'audio-' + str(rand) + '.mp3'
    tts.save(audio_file)
    playsound(audio_file)
    print(audio_str)
    os.remove(audio_file)

def response(voice_data):
    if "name" in voice_data:
        JEXI_speak("My name is Jexi")
    if "time" in voice_data:
        JEXI_speak(ctime())
    if "search" in voice_data:
        search = mic_Audio("What do you want to search?")
        url = 'https://google.com/search?q=' + search
        webbrowser.get().open(url)
        JEXI_speak("Here is what i found.")
    if "find location" in voice_data:
        location = mic_Audio("What is the location?")
        url = 'https://google.nl/maps/place/' + location + '/&amp;'
        webbrowser.get().open(url)
        JEXI_speak("Here is the location of " + location)
    if "exit" in voice_data:
        exit()


time.sleep(1)
JEXI_speak("How can i be of assistance.")
while(1):
    voice_data = mic_Audio()
    response(voice_data)
