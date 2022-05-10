import webbrowser
from Functions.Speak import speak

# Voice assistant google search function
def googleSearch(term):
    try:
        speak(f"Searching on google, {term}")
        Query = str(term)
        webbrowser.open('https://google.com/search?q='+Query)
    except:
        speak("Sorry, I'm unable to search on google")

