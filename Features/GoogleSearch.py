import pywhatkit
import wikipedia
from pywikihow import search_wikihow
import pyttsx3

# Voice assistant engine
engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voices', voices[1].id)

# Voice assistant speak Function
def speak(audio):
    print(" ")
    print(f": {audio}")
    engine.say(audio)
    engine.runAndWait()
    print(" ")

# Voice assistant google search function
def googleSearch(term):
    Query = str(term)
    pywhatkit.search(Query)

    if 'how to' in Query:
        max_result = 1
        how_to_func = search_wikihow(query=Query, max_results=max_result)
        assert len(how_to_func) == 1
        how_to_func[0].print
        speak(how_to_func[0].summary)
    else:
        search = wikipedia.summary(Query, 2)
        speak(f": According to my search : {search}")

