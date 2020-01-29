import speech_recognition as sr
import webbrowser
import time
import playsound
import os
import random
from gtts import gTTS
from time import ctime

recognizer = sr.Recognizer()


def record_audio(ask=False):
    with sr.Microphone() as mic:
        if ask:
            thornton_response(ask)
        # # Get what is said into the microphone
        audio = recognizer.listen(mic)
        voice_data = ''
        try:
            # # What is said is put into a var and pass the audio into it
            voice_data = recognizer.recognize_google(audio)
        except sr.UnknownValueError:
            thornton_response("Huh? What you say?")
        except sr.RequestError:
            thornton_response("Not now, I am sleepy and can't work right now")
        return voice_data


def thornton_response(audio_string):
    text_to_speak = gTTS(text=audio_string, lang='en')
    random_string = random.randint(1, 10000000)
    audio_file = 'audio-' + str(random_string) + '.mp3'
    text_to_speak.save(audio_file)
    playsound.playsound(audio_file)
    print(audio_string)
    os.remove(audio_file)


def thornton_ask(voice_data):
    # Gives the systems moniker
    if 'reveal yourself' in voice_data:
        thornton_response("I love it when they call me Big Mama Thornton")
    # Gives the date and time
    if 'what time is it' in voice_data:
        thornton_response(ctime())
    # Retrieves what is asked for
    if 'enhance' in voice_data:
        search = record_audio('What should I search for?')
        url = "https://duckduckgo.com/?q=" + search
        webbrowser.get().open(url)
        thornton_response('Here you go boss ' + search)
    # Retrieves specifically a certain location
    if 'locate' in voice_data:
        location = record_audio('Where are you thinking about?')
        url = "https://google.nl/maps/place/" + location + '/&amp;'
        webbrowser.get().open(url)
        thornton_response('Here you go boss ' + location)
    # Exit the system
    if 'now go to sleep' in voice_data:
        thornton_response('Signing off')
        exit()


time.sleep(1)
thornton_response('What needs to be done boss?')
while 1:
    voice_data = record_audio()
    thornton_ask(voice_data)
