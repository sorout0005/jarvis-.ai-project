import speech_recognition as sr
import pyttsx3 as pyt
import webbrowser as wb

speaker = pyt.init("sapi5")
voices = speaker.getProperty("voices")
speaker.setProperty('voices',voices[0].id)
speaker.setProperty('rate', 120)



def say (text):
    pyt.speak(f"{text}")


def takeCommand():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        r.pause_threshold = 0.6
        audio = r.listen(source)
        try:
            print("Recognizing....")
            query = r.recognize_google(audio, language='en-in')
            print(f"You said: {query}")
            return query
        except Exception as e:
            print("some error occured while listening please try again")
if __name__ == '__main__':
    print('started')
    say("Hello I am JArvis AI")
    while True:
        print('I am listening...')
        text = takeCommand()
        sites = [["youtube","https://www.youtube.com"],["wikipedia","https://www.wikipedia.com"],
                 ["Google","https://www.google.com"],["instagram","https://www.instagram.com"],
                 ["facebook","https://www.facebook.com"],["spotify","https://www.spotify.com"]]
        for site in sites:
            if f"Open {site[0]}".lower() in text.lower():
                say(f"Opening{site[0]} Sir")
                wb.open(site[1])
        #say(text)
    
speaker.runAndWait()


