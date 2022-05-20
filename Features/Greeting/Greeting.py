import datetime
from Functions.Speak import speak

def greeting():
    currentTime = datetime.datetime.now()
    currentTime.hour

    if currentTime.hour < 12:
        speak('Hello, Good morning')
    elif 12 <= currentTime.hour < 18:
        speak('Hello, Good afternoon')
    else:
        speak('Hello, Good evening')
