from TakeCommand import takeCommand
import Features.Search.YoutubeSearch as ys
import Features.Search.GoogleSearch as gs
import Features.Search.ScrapData as sd
import Features.Search.HowTo as ht
import Features.Search.SearchWiki as sw
import Features.Open.OpenSoftware as os

#Task execution function
def taskExe():
    while True:
        query = takeCommand()
        Query = query.replace("david ","")

        if 'google search' in query:
            query = Query.replace("google search ","")
            gs.googleSearch(query)

        elif 'youtube search' in query:
            query = Query.replace("youtube search ","")
            ys.youTubeSearch(query)
        
        elif 'extract data' in query:
            query = Query.replace("extract data ","")
            sd.scrapData(query)
        
        elif 'how to' in query:
            ht.howTo(Query)

        elif 'wikipedia' in query:
            query = Query.replace("wikipedia ","")
            sw.searchWiki(query)

        elif 'open' in query:
            query = Query.replace("open ", "")
            print(query)
            os.openSoftware(query)




