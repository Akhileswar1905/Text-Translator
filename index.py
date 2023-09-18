# Translator Demo Code



import speech_recognition as sr
from googletrans import Translator
from gtts import gTTS
import pygame
from time import sleep

recognizer = sr.Recognizer()

def say(text, lang="en"):
    tts = gTTS(text=text, lang=lang, slow=False)
    filename = "voice.mp3"
    tts.save(filename)
    pygame.mixer.init()
    pygame.mixer.music.load(filename)
    pygame.mixer.music.play()
    while pygame.mixer.music.get_busy():
        pygame.time.Clock().tick(10)
    pygame.mixer.quit()

say("Hi there, how can I help you?")

while True:
    try:
        with sr.Microphone() as microphone:
            recognizer.pause_threshold = 1
            recognizer.adjust_for_ambient_noise(microphone, duration=0.2)
            print("Listening.....")
            audio = recognizer.listen(microphone)
            query = recognizer.recognize_google(audio, language="en-in")
            print("Res is: " + query)
            res = Translator().translate(query, dest='hi')  
            print("In Hindi: " + res.text)
            say(res.text, lang="hi")
    except:
        print("Can't hear you")
