import tmdbsimple as tmdb
import customtkinter

tmdb.API_KEY = '8295c16817d7dbb5f94ba36baa7c04cf'
tmdb.REQUESTS_TIMEOUT = 5

def searchmovie(content: str):
    search = tmdb.Search()
    response = search.movie(query=content)
    if len(search.results) < 1:
        return False
    return search.results[0]

def getmovie(id: int):
    movie = tmdb.Movies(id).info()
    movie["genre_ids"] = [genre["id"] for genre in movie["genres"]]
    return movie

def searchmovies(content: str):
    search = tmdb.Search()
    response = search.movie(query=content)
    if len(search.results) < 1:
        return False
    results = search.results
    for movies in search.results:
        movie = tmdb.Movies(movies["id"])
        response = movie.releases()
        test = False
        for c in movie.countries:
            if c['iso_3166_1'] == 'AU' and c['certification'] != '':
                match c['certification']:
                    case "R 18+":
                        results.remove(movies)
                        break
                    case "X 18+":
                        results.remove(movies)
                        break
                    case "RC":
                        results.remove(movies)
                        break
            elif c['iso_3166_1'] == 'US' and c['certification'] != '':
                match c['certification']:
                    case "R":
                        results.remove(movies)
                        break
                    case "NC-17":
                        results.remove(movies)
                        break
                    case "NR":
                        results.remove(movies)
                        break
            else:
                results.remove(movies)
                break
        if test:
            results.remove(movies)
    return results
