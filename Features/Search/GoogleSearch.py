import webbrowser
import pyttsx3

# Voice assistant engine
engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voices', voices[0].id)

# Voice assistant speak Function
def speak(audio):
    print(" ")
    print(f": {audio}")
    engine.say(audio)
    engine.runAndWait()
    print(" ")

# Voice assistant google search function
def googleSearch(term):
    speak("Searching on google")
    Query = str(term)
    webbrowser.open('https://google.com/search?q='+Query)

