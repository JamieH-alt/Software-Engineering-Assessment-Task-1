import tmdbsimple as tmdb
import customtkinter

tmdb.API_KEY = '#'
tmdb.REQUESTS_TIMEOUT = 5

def searchmovie(content: str):
    search = tmdb.Search()
    response = search.movie(query=content)
    if len(search.results) < 1:
        return False
    return search.results[0]

def getmovie(id: int):
    try:
        movie = tmdb.Movies(id).info()
        content = movie['title']
        search = tmdb.Search()
        response = search.movie(query=content)
        return search.results[0]
    except:
        print("Error has occured!")
        return False