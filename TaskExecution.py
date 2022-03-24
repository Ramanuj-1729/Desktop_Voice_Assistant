from TakeCommand import takeCommand
import Features.GoogleSearch as gs
import Features.YoutubeSearch as ys

#Task execution function
def taskExe():
    while True:
        query = takeCommand()

        if 'google search' in query:
            Query = query.replace("david","")
            query = Query.replace("google search","")
            gs.googleSearch(query)

        elif 'youtube search' in query:
            Query = query.replace("david","")
            query = Query.replace("youtube search","")
            ys.youTubeSearch(query)


