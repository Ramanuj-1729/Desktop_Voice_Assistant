import speech_recognition as sr
import Main

# Voice assistant take command function
def takeCommand():
    recognize = sr.Recognizer()

    with sr.Microphone() as source:
        print(": Listening ...")
        recognize.pause_threshold = 1
        audio = recognize.listen(source, None, 6)

    try:
        print(": Recognizing...")
        query = recognize.recognize_google(audio, language='en-in')
        print(f": Your Command : {query}\n")
    except:
        return ""

    return query.lower()

while True:
        query = takeCommand()
        if 'start assistant' in query:
            Main.main()
            exit()


