import numpy as np
import os
import cv2
import pyautogui
from Functions.Speak import speak
from Functions.TakeCommand import takeCommand


def takeScreenShot():
    speak("Tell me the file name for this screenshot")
    filename = takeCommand()

    # take screenshot using pyautogui
    image = pyautogui.screenshot()
    image = cv2.cvtColor(np.array(image), cv2.COLOR_RGB2BGR)

    desktopLocation = os.path.join(os.path.join(os.environ['USERPROFILE']), 'Desktop', filename+'.png')

    cv2.imwrite(desktopLocation, image)
    speak("I'm sending this screenshot to Desktop")
