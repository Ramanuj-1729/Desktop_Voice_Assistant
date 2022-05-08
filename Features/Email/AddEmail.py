from openpyxl import load_workbook
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


def addEmail():
    try:
        speak("Enter receiver name: ")
        userName = input("Enter user name: ")
        speak("Enter receiver mail id: ")
        emailId = input("Enter email id: ")

        data = [userName, emailId]
        file_name = os.path.realpath(os.path.join(os.path.dirname(__file__), '..', '..', 'Database', 'EmailDB', 'emailDB.xlsx'))
        wb = load_workbook(file_name)
        page = wb.active

        page.append(data)

        wb.save(filename=file_name)
        speak("Data added successfully")

    except:
        speak("Sorry, I am unable to add the data")
