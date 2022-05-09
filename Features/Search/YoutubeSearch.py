import pywhatkit
import webbrowser as web
from Functions.Speak import speak
from Functions.TakeCommand import takeCommand

# Voice assistant youtube search function
def youTubeSearch():
    speak("Tell me, what would you like to search on youtube")
    term = takeCommand()
    result = "https://www.youtube.com/results?search_query=" + term
    web.open(result)
    speak("Can I play first video for you")

    query = takeCommand()
    if "yes" in query:
        pywhatkit.playonyt(term)
        speak("Okey")
    elif "no" in query:
        speak("Okey")

