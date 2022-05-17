import os
from pyautogui import click
from keyboard import press
from keyboard import write
from time import sleep
from Functions.Speak import speak
from Functions.TakeCommand import takeCommand


def message():
    os.startfile("C:\\Users\\raman\\AppData\\Local\\WhatsApp\\WhatsApp.exe")
    speak("Please wait, I am opening whatsapp")
    sleep(7)

    click(x=259, y=145)
    speak('To Whom you want to send whatsapp message')
    name = takeCommand()

    write(name)

    sleep(1)
    click(x=287, y=301)

    speak('would you like to message this person')
    choice = takeCommand()
    if('yes' in choice):
        speak('okay')
        sleep(1)
        click(x=1007, y=1041)

        speak('tell me what message you want to send')
        message = takeCommand()

        sleep(0.5)
        write(message)
        press('enter')
        speak('message send')
    elif('no' in choice):
        speak('okay')
    else:
        speak("Pardon, I can't understand")
