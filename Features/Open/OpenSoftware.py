import os
from Functions.Speak import speak
from Functions.TakeCommand import takeCommand

def openSoftware():
    try:
        speak("Tell me the name of the software")
        term = takeCommand()

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
