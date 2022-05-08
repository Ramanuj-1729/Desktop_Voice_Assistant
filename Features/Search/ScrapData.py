import requests
import webbrowser
import bs4
from Speak import speak


def scrapData(term):
    try:
        res = requests.get('https://google.com/search?q='+term)
        res.raise_for_status()
        speak("Extracting the data.")
        soup = bs4.BeautifulSoup(res.text, "html.parser")
        linkElements = soup.select('div#main > div > div > div > a')
        linkToOpen = min(5, len(linkElements))
        for i in range(linkToOpen):
            webbrowser.open('https://google.com'+linkElements[i].get('href'))
    except:
        speak("Sorry i can't extract the data")

