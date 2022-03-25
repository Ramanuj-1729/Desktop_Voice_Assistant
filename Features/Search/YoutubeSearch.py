import pywhatkit
import webbrowser as web
from Speak import speak
from TakeCommand import takeCommand

# Voice assistant youtube search function
def youTubeSearch(term):
    result = "https://www.youtube.com/results?search_query=" + term
    web.open(result)
    speak("Can I play first video for you")

    query = takeCommand()
    if "yes" in query:
        pywhatkit.playonyt(term)
        speak("ok sir")
    elif "no" in query:
        speak("ok sir")

