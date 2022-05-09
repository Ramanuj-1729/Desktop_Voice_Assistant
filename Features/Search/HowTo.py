import pywhatkit
from pywikihow import search_wikihow
from Functions.Speak import speak

def howTo(term):
    try:
        Query = str(term)
        pywhatkit.search(Query)
        max_result = 1
        how_to_func = search_wikihow(query=Query, max_results=max_result)
        assert len(how_to_func) == 1
        how_to_func[0].print
        speak(how_to_func[0].summary)
    except:
        speak("Sorry, I'm unable to search on google")
        return

