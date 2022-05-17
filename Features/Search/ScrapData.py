import requests
import webbrowser
import bs4
from Functions.Speak import speak
from Functions.TakeCommand import takeCommand


def scrapData():
    # try:
        speak("Tell me, what type of data you want to extract")
        term = takeCommand()
        res = requests.get('https://google.com/search?q='+term)
        res.raise_for_status()
        speak(f"Extracting the {term} data")
        soup = bs4.BeautifulSoup(res.text, "html.parser")
        linkElements = soup.select('div#main > div > div > div > a')
        linkToOpen = min(5, len(linkElements))
        for i in range(linkToOpen):
            webbrowser.open('https://google.com'+linkElements[i].get('href'))
    # except:
        # speak("Sorry, I am unable to extract the data")

