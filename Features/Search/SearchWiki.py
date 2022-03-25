import pywhatkit
import wikipedia
from Speak import speak

def searchWiki(term):
    speak("Searching on wikipedia.")
    Query = str(term)
    pywhatkit.search(Query)
    search = wikipedia.summary(Query, 2)
    speak(f": According to wikipedia : {search}")

