import pywhatkit
import wikipedia
from Functions.Speak import speak
from Functions.TakeCommand import takeCommand

def searchWiki():
    try:
        speak("Tell me, what would you like to search on wikipedia")
        term = takeCommand()
        speak(f"Searching on wikipedia {term}")
        Query = str(term)
        pywhatkit.search(Query)
        search = wikipedia.summary(Query, 2)
        speak(f": According to wikipedia : {search}")
    except:
        speak("Sorry, I'm unable to search on wikipedia")
        return

