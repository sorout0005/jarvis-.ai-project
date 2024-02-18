import speech_recognition as sr
import os
import pyttsx3 as pyt



speaker = pyt.init("sapi5")



def speak (text):
    pyt.say("dfgh")


def takeCommand():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        r.pause_threshold = 1
        audio = r.listen(source)
        query = r.recognize_google(audio, language='en-in')
        print(f"You said: {query}")
if __name__ == '__main__':
    print('PyCharm')
    speak("Hello I am JArvis A.I")
    print('I am listening...')
    text = takeCommand()
    speak(text)
    
speaker.runAndWait()


