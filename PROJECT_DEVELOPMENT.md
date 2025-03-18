# MovieLister

## **Requirements Definition**
### **Functional Requirements**
* Users must be able to search for Movies by title (accounting for bad capitalisation)
* Users must have the ability to select watch status (Watched, Not-Watched)
* The User should have an obvious search bar to look for movie.
* The User should be able to click a Help Icon, to get a tutorial on how to use the program.
* The system should display movies in a grid form on the home page for what they have watched.
* The system should allow users to preview the movie that they are going to add, and see the rating, description, title, and genres.
* The system should allow users to preview movies that they have already watched and see the rating, description, title and genres.
* The system should offer users the TMDb link to see the movie on their page.
* The system should store the watched movies in a file, to be accessed whenever the user opens the program on their machine.

### **Non Functional Requirements**
* The Movie search process should complete within 3 seconds, if any longer it should submit an error
* The Movie search process must return verbose, easily understandable errors to the user in order to inform them of their mistake.
* The system should have an easy to use, understandable GUI.
* The system should be useable on a low-power system.

---
## **Determining Specifications**
### **Functional Specifications**
#### **User Requirements**
* The user should be able to search for any movie by name on the TMDb database and see its title, description, rating, and genres.
* The user should be able to store and access movies that they have already watched.
* The user should be able to mark movies as watched and unwatched.
#### **Inputs & Outputs**
* The system needs to accept a string input in the form of the movie title
* The system needs to accept a file input in the form of a json that will list the movies that have been previously stored.
#### **Core Features**
* The program needs to be able to take user input of a movie title and return the movies title, description, rating, and genres.
* The program also needs to be able to securely store the list of watched movies for the user, locally on their machine.;
#### **User Interaction**
* Users will interace with the system through a TKinter GUI.
* It will need to have a text box for users to input the title
* It will need to have cover images for each movie, alongside the label of each movie,
* It will need to allow for seperate pages for each movie when clicked, which would then show the title, description, rating and genres of a movie.
#### **Error Handling**
* The system needs to be able to handle incorrectly inputed strings
* The system needs to be able to handle movies that don't exist
* The system needs to be able to handle movies that have been removed from the TMDb database since stored on the local machine
* The system needs to be able to handle timeout issues from poor internet.
### **Non-Functional Specifications**
#### **Performance**
* The system should perform quickly, (within 3 seconds of a request) in order to keep user engagement.
* The system should also launch within 5 seconds on the tested system.
* The system should be scaleable at a maximum time of O(n) on loading the previously stored movies from the file in order to allow for big libraries.
#### **Useability / Accessibility**
* The application should have a light friendly tone to allow for the widest audience of users.
* The user interface should be clear and have high-contrasting colours to help people who are colourblind, and allow for obvious edges.
* The user interface should have icons over words for all pages, (information such as titles, error handling, and descriptions etc will all be done in english text) to allow for people who might not speak english to atleast navigate the basic systems.
#### **Reliability**
* Crashes should be few and far between, happening only in extreme cases.
* Data integrity is important, files should be updated on change, instead of on the closing / opening of the program to allow for more recent backups.
* Duplicate data should be handled by culling the duplicates from the stored file.
* In other crashes where the program is still open, the program should give a clear warning with a verbose report of what happened to allow users to understand what the issue could be and avoid recreating the error before an update happens.
### **Use Cases**
**Actor:** User (Avid-Movie Watcher)
**Preconditions:** Internet access; API with TMDb data is available.
**Main Flow:**
1. **Search for Movie** - User enters a movie title (e.g. Pulpfiction); system retrieves the details and displays the preview page
2. **Mark as Watched** - User marks movie as watched and stores it to their front page; system confirms storage and sends user to home page.
3. **View Watched Movies** - User looks at home page and sees all stored movies; System lists through all of their watched movies in a scrollable array of covers and titles.

**Postconditions:** Watched movie data has been received, stored, or removed successfully.

---

## **Design**
### **Gantt Chart**
![](theorystorage/Jamie%20Hanson%20-%20Software%20Engineering%20-%202025%2003%205%20-%20MovieLister%20Gantt%20Chart.png)
### **Structure Chart**
![](theorystorage/Jamie%20Hanson%20-%20Software%20Engineering%20-%202025%2003%205%20-%20MovieLister%20Structure%20Chart.png)
### **Pseudocode / Algorithms**

Main System
```{r, tidy=FALSE, eval=FALSE, highlight=FALSE }
BEGIN MovieListerSystemMain
  FOR movie = firstMovie TO lastMovie STEP watchedMovies()
    Display movie title
    Display movie cover
  NEXT movie

  IF movie clicked THEN
    movieclicked (movie)
  ENDIF

  IF movie searched THEN
    moviesearched (title)
  ENDIF

  IF helpclicked THEN
    Display Help Text
  ENDIF
END MovieListerSystemMain
```
![](theorystorage/Jamie%20Hanson%20-%20Software%20Engineering%20-%202025%2003%2010%20-%20Flowchart%20-%20MovieListerSystemMain.png)


Watched Movies
```{r, tidy=FALSE, eval=FALSE, highlight=FALSE }
BEGIN watchedMovies
  movielist = read(watchedmovies.json)
  movie = firstmovie
  REPEAT
    movietitle = read(movie, title)
    moviecover = read(move, cover)
    movieid = movie
    movie = nextmovie
    RETURN movietitle, moviecover, movieid
  UNTIL movie = lastmovie
END watchedMovies
```
![](theorystorage/Jamie%20Hanson%20-%20Software%20Engineering%20-%202025%2003%2010%20-%20Flowchart%20-%20Watched%20Movies.png)

Preview Movie
```{r, tidy=FALSE, eval=FALSE, highlight=FALSE }
BEGIN previewMovie (movieid, description, title, genreids, coverimage, rating)
  Display movieid
  Display description
  Display title
  Display coverimage
  Display rating
  FOR thisgenre = first in genreids TO last in genreids STEP next genreids
    CASEWHERE thisgenre evaluates to
      28: genre = Action
      12: genre = Adventure
      16: genre = Animation
      35: genre = Comedy
      80: genre = Crime
      99: genre = Documentary
      18: genre = Drama
      10751: genre = Family
      14: genre = Fantasy
      36: genre = History
      27: genre = Horror
      10402: genre = Music
      10749: genre = Romance
      878: genre = SciFi
      53: genre = Thriller
      10752: genre = War
      37: genre = Western
    ENDCASE
    Display genre
  NEXT thisgenre
END previewMovie (movie_id, description, title, genreids, coverimage, rating)
```
![](theorystorage/Jamie%20Hanson%20-%20Software%20Engineering%20-%202025%2003%2010%20-%20Flowchart%20-%20Preview%20Movie.png)

### **Data Dictionary**
| **Variable** | **Data Type** | **Format for Display** | **Size in Bytes** | **Size for Display** | **Description** | **Example** | **Validation** |
| --- | --- | --- | --- | --- | --- | --- | --- |
| movieid | Integer | NNNNNNN | 4 | 7 | The movie id that is used within the TMDb database | 5039482 | All characters are numbers |
| moviecoverimage | JPEG (image) | Full Image at w400xh600 resolution, 8 bit colours (256) | 240000 | 10% width of screen, 15% height per image | These are cover images stored within the file system of a users computer for all watched movies, they will also be temporarily downloaded when the user previews a movie. | ![](theorystorage/Jamie%20Hanson%20-%20Software%20Engineering%20-%202025%2003%2010%20-%20Data%20Dictionary%20-%20Cover%20Image%20Example.jpg) | N/A |
| moviecoverimagelocation | FilePath | Drive://Directory/movieid.jpg | 4 | 5-256 | The file path to locate the moviecoverimage storage location, this lets the program directly access it | C://Documents/MovieLister/coverimages/5039482.jpg | There is a jpg file at that location |
| movietitle | String | X..X | 4 | 1-1000 | The full movie title within the TMDb database | The Gentlemen | N/A | 

## Development
### Main.py
```py
import customtkinter
import tkinter as tk
import math
import PIL.Image as Images
import requests
import os
import tmdbsimple as tmdb
import threading
import pywinstyles
import json
import concurrent.futures
import sys
import platform
import apiinteractions as api # This is my python API class (module or whatever you want to call it) because it says I have to :/
import time

# Sets the theme / appearance mode, so it doesnt follow the system (Forced dark mode because yes)
customtkinter.set_default_color_theme("dark-blue")
customtkinter.set_appearance_mode("dark")

# The Window (as a class)
class App(customtkinter.CTk):
    def __init__(self):
        super().__init__()
        self.geometry("1600x900") # Creates the window, with height, width and windows actual title
        self.minsize(1600, 900)
        self.maxsize(1600, 900)
        self.title("MovieLister")
        
        # Creates the Movie Lister title.
        self.customtitle = customtkinter.CTkTextbox(master=self,height=100,text_color="#ce3b3b",font=("Bahnschrift",76), activate_scrollbars=False, width=1000, border_spacing=0, border_width=0, corner_radius=0, wrap="word")
        self.customtitle.grid(pady=10,padx=5,row=0,column=3,columnspan=11)
        self.customtitle.tag_config("center", justify="center")
        self.customtitle.insert("0.0", "MovieLister", "center")
        self.customtitle.configure(state="disabled")

        # Sets up the search bar and its storage.
        self.searchtext = ""

        self.search = customtkinter.CTkEntry(master=self, height=30, width=175, corner_radius=9, state="normal", textvariable=self.searchtext, placeholder_text="Search")
        self.search.grid(pady=10,padx=10,row=0,column=15,columnspan=1,sticky="nw")

        # Sets up so the search entry prints text on enter (To be linked to a function later)
        def moviesearched(event=None):
            string = self.search.get()
            movie = api.searchmovies(string)
            if movie == False:
                frame = ErrorWindow(self)
                timer = threading.Timer(0.2, frame.focus) # Simple Use of a threading timer so we don't impact the loading times with our focus time (For some reason ctk starts Toplevel windows... behind the window)
                timer.start()
                return
            window = SearchWindow(self, string, movie)
            timer = threading.Timer(0.2, window.focus)
            timer.start()
            #frame = MoviePreviewWindow(self, movie)
            #timer = threading.Timer(0.2, frame.focus)
            #timer.start()
            
        self.search.bind('<Return>', moviesearched)

        # Loads the WatchedMoviesFrame and sets its size and other variables
        self.watchedmoviesframe = WatchedMoviesFrame(self, width=1100, height=700, corner_radius=20, orientation="horizontal")
        self.watchedmoviesframe.grid(pady=10,padx=10,row=1,column=0,columnspan=16,sticky="nsew")  

# Frame that has all the watched movies
class WatchedMoviesFrame(customtkinter.CTkScrollableFrame):
    def __init__(self, master, **kwargs):
        super().__init__(master, **kwargs)

        # This loops through all movies and then provides a spot for the empty + movie cover.
        for movie_index in range(0, len(watchedmovies) + 1):
            movie_row = (0, 1)[(movie_index + 1) % 2 == 0] # Basic tenerary operator meaning that ensures the ordering of the movies in which rows.
            movie_column = math.floor((movie_index) / 2)
            print("Loading Movie...")
            movie_frame = MovieFrame(self, watchedmovies[movie_index] if not movie_index >= len(watchedmovies) else None, False if not movie_index >= len(watchedmovies) else True, width=200, height=300)
            movie_frame.grid(row=movie_row,column=movie_column,padx=10,pady=10)

# This here is the movies covers themselves
class MovieFrame(customtkinter.CTkFrame):
    def __init__(self, master, StoredMovie, empty, **kwargs):
        super().__init__(master, **kwargs)

        cover_master_location = 'https://image.tmdb.org/t/p/original/'

        if empty:
            self.image = Images.open(os.path.dirname(os.path.realpath(__file__)) + r"\\storage\\empty.png")
        else:
            self.image = Images.open(os.path.dirname(os.path.realpath(__file__)) + r"\\storage\\unloaded.png")
            #self.image = Images.open(requests.get(cover_master_location + StoredMovie.coverstoragelocation, stream=True).raw)
            #self.image.after_idle(lambda: self.image.configure())
        self.cover = customtkinter.CTkImage(self.image,size=(200, 300))

        if empty:
            self.label = customtkinter.CTkLabel(self, image=self.cover, text="Add a Movie By Searching!")
        else:
            self.label = customtkinter.CTkLabel(self, image=self.cover, text=StoredMovie.title)
        self.label._label.config(bd=3, relief="solid", compound="top")
        self.label._label.configure(wraplength=200)
        self.label.grid(row=0, column=0)

        if not empty:
            t1 = threading.Thread(target=MovieCover, args=(self.label, StoredMovie.coverstoragelocation))
            t1.start()
        

        if not empty:
            # Movie Preview Button
            self.button = customtkinter.CTkButton(self.label, text="👁", width=30, height=30, corner_radius=10, command=lambda: ClickToPreview(StoredMovie.TMDbID))
            self.button.place(relx=0.06,rely=0.04)

            self.remove = customtkinter.CTkButton(self.label, text="X", width=30, height=30, corner_radius=10, command=lambda: RemoveMovie(StoredMovie.TMDbID, True, None, master), fg_color="#a43c3c", hover_color="#912424")
            self.remove.place(relx=0.79,rely=0.04)
            
        # This is to parse a clicked eye icon into the preview window
        def ClickToPreview(id):
            movie = api.getmovie(id)
            if movie == False:
                error("#02")
                return
            frame = MoviePreviewWindow(master, movie)
            timer = threading.Timer(0.2, frame.focus)
            timer.start()
        
# This function is here so we can seperate the threading for getting the cover of the movie, as the web requests can take time on slow internet connections or when you have alot of images. By default it will set the movie the horrific + icon cover and then back to its image. (Hopefully)
def MovieCover(label, coverstoragelocation):
    cover_master_location = 'https://image.tmdb.org/t/p/original/'
    image = Images.open(requests.get(cover_master_location + coverstoragelocation, stream=True).raw)
    cover = customtkinter.CTkImage(image, size=(200,300))
    label.after_idle(lambda: label.configure(image=cover))
        
# The Movie Preview Claim
class MoviePreviewWindow(customtkinter.CTkToplevel):
    def __init__(self, master, movie,  **kwargs):
        super().__init__(master, **kwargs)

        cover_master_location = 'https://image.tmdb.org/t/p/original/'

        # Sets up the window
        self.geometry("1280x720")
        self.minsize(1280, 720)
        self.maxsize(1280, 720)
        self.title(movie['title'])

        self.image = Images.open(os.path.dirname(os.path.realpath(__file__)) + r"\\storage\\emptybackground.png")
        self.backgroundimage = customtkinter.CTkImage(self.image, size=(1280, 720))
        self.backgroundlabel = customtkinter.CTkLabel(self, text="", image=self.backgroundimage)
        self.backgroundlabel.place(x=0,y=0) # The image will be added with mutlitrheading later.

        # Now Sets up the title display etc.
        self.titlelabel = customtkinter.CTkTextbox(self.backgroundlabel, font=("Bahnschrift", 55), width=700, height=50, fg_color="#282828", wrap="none")
        self.titlelabel.insert("0.0", text=movie['title'])
        self.titlelabel.configure(state="disabled")
        self.titlelabel.place(relx=0.025,rely=0.1)

        self.titlescrollbar = customtkinter.CTkScrollbar(self.backgroundlabel, command=self.titlelabel.xview, orientation="horizontal", width=700) # This makes a scrollbar to force the textbox to scroll horizontally not vertically,
        self.titlescrollbar.place(relx=0.025,rely=0.19)
        self.titlelabel.configure(xscrollcommand=self.titlescrollbar.set)

        # Setting up the description
        self.overview = customtkinter.CTkTextbox(self.backgroundlabel, font=("Bahnschrift", 30), width=700, wrap="word", fg_color="#282828")
        self.overview.insert("0.0", text=movie['overview'])
        self.overview.configure(state="disabled")
        self.overview.place(relx=0.025,rely=0.21)

        # Setting up the cover image
        self.cover = Images.open(os.path.dirname(os.path.realpath(__file__)) + r"\\storage\\unloaded.png")
        self.coverctk = customtkinter.CTkImage(self.cover, size=(200, 300))
        self.coverlabel = customtkinter.CTkLabel(self.backgroundlabel, text="", image=self.coverctk)
        self.coverlabel.place(relx=0.8,rely=0.1)

        if not isinstance(movie['backdrop_path'], type(None)):
            t2 = threading.Thread(target=BackgroundImage, args=(self.backgroundlabel, movie['backdrop_path']))
            t3 = threading.Thread(target=MovieCover, args=(self.coverlabel, movie['poster_path']))
            t2.start()
            t3.start()

        # Setting up the vote score (rating)
        self.votinglabel = customtkinter.CTkLabel(self.backgroundlabel, font=("Bahnschrift", 40), text="Rating: " + str(round(movie['vote_average'], 1)) + "/10", fg_color="#282828")
        self.votinglabel.place(relx=0.025,rely=0.485)

        # Setting up the Genres (pain)
        genres = movie['genre_ids']
        self.genrelabel = customtkinter.CTkTextbox(self.backgroundlabel, font=("Bahnschrift", 40), width=500, height=50, fg_color="#282828")
        genrestrings = []
        for genre in genres: # Getting the ID's and turning them into a list of strings.
            match genre: 
                case 28:
                    genrestrings.append("Action")
                case 12:
                    genrestrings.append("Adventure")
                case 16:
                    genrestrings.append("Animation")
                case 35:
                    genrestrings.append("Comedy")
                case 80:
                    genrestrings.append("Crime")
                case 99:
                    genrestrings.append("Documentary")
                case 18:
                    genrestrings.append("Drama")
                case 10751:
                    genrestrings.append("Family")
                case 14:
                    genrestrings.append("Fantasy")
                case 36:
                    genrestrings.append("History")
                case 27:
                    genrestrings.append("Horror")
                case 10402:
                    genrestrings.append("Music")
                case 9648:
                    genrestrings.append("Mystery")
                case 10749:
                    genrestrings.append("Romance")
                case 878:
                    genrestrings.append("SciFi")
                case 53:
                    genrestrings.append("Thriller")
                case 10752:
                    genrestrings.append("War")
                case 37:
                    genrestrings.append("Western")
        genres = ""
        for i, genre in enumerate(genrestrings, start=1):
            if i == len(genrestrings):
                genres = genres + f"{genre}"
            else:
                genres = genres + f"{genre}, "
        self.genrelabel.insert("0.0", text=genres)
        self.genrelabel.configure(state="disabled")
        self.genrelabel.place(relx=0.025, rely=0.55)

        # Sets up the Release Date Display
        self.releaselabel = customtkinter.CTkTextbox(self.backgroundlabel, font=("Bahnschrift", 40), width=250, height=50, fg_color="#282828")
        self.releaselabel.insert("0.0", movie["release_date"])
        self.releaselabel.configure(state="disabled")
        self.releaselabel.place(relx=0.025,rely=0.625)

        # Sets up the TMDb ID display
        self.tmdbidlabel = customtkinter.CTkTextbox(self.backgroundlabel, font=("Bahnschrift", 30), width=250, height=50, fg_color="#282828")
        self.tmdbidlabel.insert("0.0", "TMDbID: " + str(movie["id"]))
        self.tmdbidlabel.configure(state="disabled")
        self.tmdbidlabel.place(relx=0.025,rely=0.7)

        # Sets up the button that will let us add this to the watched movies list
        if not HasMovie(movie["id"]):
            self.addmoviebutton = customtkinter.CTkButton(self.backgroundlabel, font=("Bahnscrhift", 18), text="Add to WatchList!", width=200, corner_radius=0, command=lambda: AddMovie(StoredMovie(movie["title"], movie["id"], movie["poster_path"]), self, master))
            self.addmoviebutton.place(relx=0.8, rely=0.52)
        else:
            self.removemoviebutton = customtkinter.CTkButton(self.backgroundlabel, font=("Bahnschrift", 18), text="Remove from Watchlist!", width=200, corner_radius=0, command=lambda: RemoveMovie(movie["id"], False, self, master), fg_color="#a43c3c", hover_color="#912424")
            self.removemoviebutton.place(relx=0.8, rely=0.52)

        # This means that the objects parsed will be opaque, we have to use this as CustomTkinter and Tkinter itself dont have support for opaque / transparent windows, nor do they have antialiasing.
        pywinstyles.set_opacity(self.titlelabel, value=0.8)
        pywinstyles.set_opacity(self.overview, value=0.8)
        pywinstyles.set_opacity(self.votinglabel, value=0.8)
        pywinstyles.set_opacity(self.genrelabel, value=0.8)
        pywinstyles.set_opacity(self.releaselabel, value=0.8)
        pywinstyles.set_opacity(self.tmdbidlabel, value=0.8)

# Another function dedicated to manipulating stuff on threads.
def BackgroundImage(backgroundlabel, backdrop_path):
    cover_master_location = 'https://image.tmdb.org/t/p/original/'
    image = Images.open(requests.get(cover_master_location + backdrop_path, stream=True).raw)
        
    source = image.split() #Here i'm going through an making the background image darker, so it's less standout.
    R, G, B = 0, 1, 2
    constant = 1.5
    Red = source[R].point(lambda i: i/constant)
    Green = source[G].point(lambda i: i/constant)
    Blue = source[B].point(lambda i: i/constant)
    image = Images.merge(image.mode, (Red, Green, Blue))

    # Now sets the darkend image as the background (CustomTkinter and Tkinter require images to be put as labels for whater stupid reason.
    backgroundimage = customtkinter.CTkImage(image, size=(1280, 720))
    backgroundlabel.after_idle(lambda: backgroundlabel.configure(image=backgroundimage)) # This is so we are threadsafe

# This is so we can see multiple search results
class SearchWindow(customtkinter.CTkToplevel):
    def __init__(self, master, searchcontent, search, **kwargs):
        super().__init__(**kwargs)
        self.geometry("600x720")
        self.minsize(600, 720)
        self.maxsize(600, 720)
        self.title(f"Search results for: {searchcontent}")

        self.grid_rowconfigure(0, weight=1) # We do this so that when we put the scrollable frame on the grid, it covers the whole window!
        self.grid_columnconfigure(0, weight=1)

        self.scrollableframe = SearchFrame(master=self, mm=master, search=search, width=600, height=720,corner_radius=0, fg_color="transparent")
        self.scrollableframe.grid(row=0, column=0, sticky="nsew")

class SearchFrame(customtkinter.CTkScrollableFrame):
    def __init__(self, master, mm, search, **kwargs):
        super().__init__(master, **kwargs)
        
        for i, movie in enumerate(search):
            if movie["poster_path"] is None:
                continue
            frame = SearchMovieFrame(self, mm, movie, width=580, height=300, corner_radius=20)
            frame.grid(row=i, padx=10, pady=10)

class SearchMovieFrame(customtkinter.CTkFrame):
    def __init__(self, master, mmm, movie, **kwargs):
        super().__init__(master, **kwargs)
        
        self.title = customtkinter.CTkTextbox(self, font=("Bahnschrift", 25), width=350, height=20, wrap="none", fg_color="transparent")
        self.title.insert("0.0", movie["title"])
        self.title.configure(state="disabled")
        self.title.place(relx=0.025,rely=0.05)
        
        
        self.releasedate = customtkinter.CTkLabel(self, text=movie["release_date"], font=("Arial", 18))
        self.releasedate.place(relx=0.05,rely=0.25)
        
        self.rating = customtkinter.CTkLabel(self, text=str(round(movie["vote_average"], 1)) + "/10", font=("Arial", 18))
        self.rating.place(relx=0.25, rely=0.25)
        
        self.image = Images.open(os.path.dirname(os.path.realpath(__file__)) + r"\\storage\\unloaded.png")
        self.ctkimage = customtkinter.CTkImage(self.image, size=(200, 300))
        self.imagelabel = customtkinter.CTkLabel(self, text="", image=self.ctkimage)
        self.imagelabel.place(relx=0.64, rely=0)

        
        self.preview = customtkinter.CTkButton(self, text="👁", font=("Arial", 40), width=100, height=100, corner_radius=30, command=lambda: ClickToPreview(movie["id"]))
        self.preview.place(relx=0.025,rely=0.6)

        t1 = threading.Thread(target=MovieCover, args=(self.imagelabel, movie["poster_path"]))
        t1.start()

        def ClickToPreview(id):
            movie = api.getmovie(id)
            if movie == False:
                error("#02")
                return
            frame = MoviePreviewWindow(mmm, movie)
            timer = threading.Timer(0.2, frame.focus)
            timer.start()

            
# This window is so the user knows that a search is happening.
class SearchProgressWindow(customtkinter.CTkToplevel):
    def __init__(self, master,  **kwargs):
        super().__init__(master, **kwargs)
        self.geometry("600x200")
        self.title("Searching...")
        self.label = customtkinter.CTkLabel(self, font=("Bahnschrift", 40), text="Searching!")
        self.label.pack(padx=40,pady=20)

class ErrorWindow(customtkinter.CTkToplevel):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.geometry("600x200")
        self.title("Uh Oh!")
        self.label = customtkinter.CTkLabel(self, font=("Bahnschrift", 30), text="We couldn't find that movie!")
        self.label.pack(padx=20,pady=20)
        self.button = customtkinter.CTkButton(self, font=("Bahnschrift", 30), text="Ok", fg_color="#a43c3c", hover_color="#912424", command=self.destroy)
        self.button.pack(padx=20,pady=20)

""" This is the main code sections where we will connect the GUI into the modules and storage
    First we have a class for the movies to be stored
    and then the rest of the code
"""
# Movie Storage Class
class StoredMovie():
    def __init__(self, title: str, TMDbID: int, coverstoragelocation: str):
        self.title = "" # Sets up the values within the class
        self.TMDbID = 0
        self.coverstoragelocation = ""
        if isinstance(title, str):
            self.title = title
        else:
            print("Title is not a string... converting")
            self.title = str(title)
        if isinstance(TMDbID, int):
            self.TMDbID = TMDbID
        else:
            print("TMDbID is not a number... attempting conversion")
            try:
                self.TMDbID = int(TMDbID)
            except:
                print("Could not convert TMDbID to a number! Returning")
                return
        if isinstance(coverstoragelocation, str):
            self.coverstoragelocation = coverstoragelocation
        else:
            print("Cover Storage Location is not a string... converting")
            self.coverstoragelocation = str(coverstoragelocation)
    def get_dict(self):
        dict_obj = {
            "title": self.title,
            "TMDbID": self.TMDbID,
            "coverstoragelocation": self.coverstoragelocation
            }
        return dict_obj

# Loading from json
watchedmovies = []

savefile = "watchedmovies.json"
try:
    with open(savefile, 'r') as f:
        watchedmovies_json = f.read()
        opened_json = json.loads(watchedmovies_json)
        for i in opened_json:
            watchedmovies.append(StoredMovie(i["title"], i["TMDbID"], i["coverstoragelocation"]))
except:
    watchedmovies = []

def AddMovie(movie: StoredMovie, window, master):
    watchedmovies.append(movie)
    window.destroy() # Destorys that window
    for widget in master.watchedmoviesframe.winfo_children():
        widget.destroy()
    try:
        unserializedwatchedmovies = [] # This is all because JSON won't save a class because why would it.
        for movie in watchedmovies:
            unserializedwatchedmovies.append(movie.get_dict())
        with open(savefile, 'x') as f:
            f.write(json.dumps(unserializedwatchedmovies))
        print("Saved Movies!")
    except:
        try:
            unserializedwatchedmovies = []
            for movie in watchedmovies:
                unserializedwatchedmovies.append(movie.get_dict())
            with open(savefile, 'w') as f:
                f.write(json.dumps(unserializedwatchedmovies))
            print("Saved Movies!")
        except:
            error("#01")

    # This here re-runs the code that is used in the WatchedMoviesFrame from here to make sure it relists everything.
    for movie_index in range(0, len(watchedmovies) + 1):
        movie_row = (0, 1)[(movie_index + 1) % 2 == 0] # Basic tenerary operator meaning that ensures the ordering of the movies in which rows.
        movie_column = math.floor(movie_index / 2)
        print("Loading Movie...")
        movie_frame = MovieFrame(master.watchedmoviesframe, watchedmovies[movie_index] if not movie_index >= len(watchedmovies) else None, False if not movie_index >= len(watchedmovies) else True, width=200, height=300)
        movie_frame.grid(row=movie_row,column=movie_column,padx=10,pady=10)

def HasMovie(TMDbID: int) -> bool:
    for movie in watchedmovies:
        if movie.TMDbID == TMDbID:
            return True
    return False

def RemoveMovie(TMDbID: int, main: bool, window, master): # Removes the movie, main bool is to just tell if its coming from the main window or a top level.
    for movie in watchedmovies:
        if movie.TMDbID == TMDbID:
            watchedmovies.remove(movie)
            break
    if not main:
        window.destroy()
    for widget in master.winfo_children():
        widget.destroy()
    try:
        unserializedwatchedmovies = [] # This is all because JSON won't save a class because why would it.
        for movie in watchedmovies:
            unserializedwatchedmovies.append(movie.get_dict())
        with open(savefile, 'x') as f:
            f.write(json.dumps(unserializedwatchedmovies))
        print("Saved Movies!")
    except:
        try:
            unserializedwatchedmovies = []
            for movie in watchedmovies:
                unserializedwatchedmovies.append(movie.get_dict())
            with open(savefile, 'w') as f:
                f.write(json.dumps(unserializedwatchedmovies))
            print("Saved Movies!")
        except:
            error("#01")

    # This here re-runs the code that is used in the WatchedMoviesFrame from here to make sure it relists everything.
    for movie_index in range(0, len(watchedmovies) + 1):
        movie_row = (0, 1)[(movie_index + 1) % 2 == 0] # Basic tenerary operator meaning that ensures the ordering of the movies in which rows.
        movie_column = math.floor(movie_index / 2)
        print("Loading Movie...")
        movie_frame = MovieFrame(master, watchedmovies[movie_index] if not movie_index >= len(watchedmovies) else None, False if not movie_index >= len(watchedmovies) else True, width=200, height=300)
        movie_frame.grid(row=movie_row,column=movie_column,padx=10,pady=10)

def error(code):
    print(f"An Error has occured, please report the following\nErrorCode: {code}\nPyVer: {sys.version}\nPlatform: {platform.platform()}")

""" Back to running the GUI """        
# Runs the App
app = App()
app.columnconfigure(0, weight=1)
app.mainloop()
```

### apiinteractions.py
```py
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
```

## Testing and debugging
Done alongside development within commits.

## Maintenance
### Maintenance Questions
1. The Movie Databases (TMDb) API doesn't change old movies as a part of their own maintenance system, they have a great focus on backwards compatability and there will be no need to adapt to change. Older movies lack certifications (age ratings) and the database has stayed the same, TMDb Simple is also the interface we use to manage the database, and they focus on keeping a 1 to 1 relation to TMDb's api calls. As a result, MovieLister should need no maintenance to do with TMDb's api changing, allowing for a long-term usage of the API.

2. MovieLister database uses very simple core libraries, that are the foundation of alot of 
python programs (except TMDbSimple but see the first question for that) meaning we should not have to do any maintenance here. They have teams or are open source in a way that allows for us to be secure in their updates not breaking our program. In the unrealistic case of one of these modules making an overhaul that does effect our program, it would be pretty big news, allowing us to quickly find a method to patch and replace the depreciated code. Simply put, these big python modules are made to not effect functionality of older programs, but in the case that they do we'd be able to patch it quickly.

3. When a Bug is found a reported in the program, there should already be catch statements and prints within the program which should report the specific error (in which case it makes it easier to figure out what went wrong). If we can not find the bug through this method, we will look at pythons error case and quickly patch it out after a user has contacted me through email or another contact method.

4. To maintain clear documentation, I'd go through to flowchats, algorithms, structure charts etc.. and update them to fit new changes in the code, aswell as keeping code comments and storing logs of all changes through version control applications such as GitHub.

### Final Evaluation
