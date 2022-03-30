import os
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

def openSoftware(term):
    try:
        if term == "chrome":
            os.startfile("C:\\Program Files\\Google\\Chrome\\Application\\chrome.exe")
            speak("Opening chrome")
        else:
            query = str(term)
            dirPath = os.path.dirname(__file__)
            os.startfile(os.path.realpath(os.path.join(dirPath, '..', '..', 'Database', 'SoftwareShortcuts', query + '.lnk')))
            speak("Opening " + query)
    except:
        speak("Pardon, I can't understand")
