import os
from pyautogui import click
from keyboard import write
from time import sleep
from Functions.Speak import speak
from Functions.TakeCommand import takeCommand


def voiceCall():
    os.startfile("C:\\Users\\raman\\AppData\\Local\\WhatsApp\\WhatsApp.exe")
    speak("Please wait, I am opening whatsapp")
    sleep(7)

    click(x=259, y=145)
    speak('To Whom you want to voice call on whatsapp')
    name = takeCommand()

    write(name)

    sleep(1)
    click(x=287, y=301)

    speak('would you like to voice call this person')
    choice = takeCommand()
    if('yes' in choice):
        speak('okay')
        sleep(0.5)

        click(x=1725, y=65)
    elif('no' in choice):
        speak('okay')
    else:
        speak("Pardon, I can't understand")
