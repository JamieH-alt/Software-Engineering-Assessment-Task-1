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
from playsound import playsound
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

        def helpwindow():
            self.helpwindow = HelpWindow(master=self)
            timer = threading.Timer(0.2, self.helpwindow.focus)
            timer.start()

        def reportwindow():
            self.reportwindow = ReportWindow(master=self)
            timer = threading.Timer(0.2, self.reportwindow.focus)
            timer.start()
            
        self.search.bind('<Return>', moviesearched)

        # Loads the WatchedMoviesFrame and sets its size and other variables
        self.watchedmoviesframe = WatchedMoviesFrame(self, width=1100, height=700, corner_radius=20, orientation="horizontal")
        self.watchedmoviesframe.grid(pady=10,padx=10,row=1,column=0,columnspan=16,sticky="nsew")

        # Help Button
        self.helpbutton = customtkinter.CTkButton(master=self, font=("Bahnschrift", 72), text="help", width=200, height=100, corner_radius=15, command=helpwindow)
        self.helpbutton.grid(pady=10,padx=10,row=0,column=0,sticky="nw")

        # Report Button
        self.reportbutton = customtkinter.CTkButton(master=self, font=("Bahnschrift", 72), text="!", command=reportwindow, width=100, height=100, corner_radius=15, fg_color="#a43c3c", hover_color="#912424")
        self.reportbutton.grid(pady=10,padx=10,row=0,column=1,sticky="ne")

# Report Window
class ReportWindow(customtkinter.CTkToplevel):
    def __init__(self, master, **kwargs):
        super().__init__(master, **kwargs)
        self.geometry("600x720")
        self.minsize(600, 720)
        self.maxsize(600, 720)
        self.title("Report A Problem! (I care sooo much)")

        self.textbox = customtkinter.CTkTextbox(self, width=600, height=620)
        self.textbox.pack()
        self.textbox.insert("0.0", "Fill in only the revelant fields\nMovie Title: \nTMDb ID: \nError Code: (If none leave blank) \n\nDescribe the issue and how we could fix it below: ")

        def reportFiled():
            T = threading.Thread(target=playShreddingSoundFx)
            T.start()
            reportFiledWindow = ReportFiledWindow(master=master)
            T1 = threading.Thread(target=lambda: shredprogram(720, self))
            T1.start()
        self.submit = customtkinter.CTkButton(self, width=600, height=75, font=("Bahnschrift", 60), text="Submit", command=reportFiled)
        self.submit.pack()

def playShreddingSoundFx(): # This function is outside of the class so we can use multithreading to have it run without blocking the program.
    print("Shredding Report")
    playsound(os.path.dirname(os.path.realpath(__file__)) + r"\\storage\\papershredder.mp3")
    print('Finished Shredding Report !!!')

# Report Filed Window alerts the user report is filed
class ReportFiledWindow(customtkinter.CTkToplevel):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.geometry("600x200")
        self.minsize(600, 200)
        self.maxsize(600, 200)
        self.title("Report Filed Window!")
        self.label = customtkinter.CTkLabel(self, font=("Bahnschrift", 30), text="Report Filed!")
        self.label.pack(padx=20,pady=20)
        self.label2 = customtkinter.CTkLabel(self, font=("Bahnschrift", 24), text="You're feedback is valuable")
        self.label2.pack(padx=20,pady=5)
        self.button = customtkinter.CTkButton(self, font=("Bahnschrift", 30), text="Ok", command=self.destroy)
        self.button.pack(padx=20,pady=20)

# Shredder
def shredprogram(startvalue: int, window):
    for i in range(0, math.floor(startvalue / 10)):
        value = startvalue - (i * 10)
        window.minsize(600, value)
        window.maxsize(600, value)
        window.geometry(f"600x{value}")
        time.sleep(0.08)
    window.destroy()
        
# Help window
class HelpWindow(customtkinter.CTkToplevel):
    def __init__(self, master, **kwargs):
        super().__init__(master, **kwargs)
        self.geometry("1280x720")
        self.minsize(1280, 720)
        self.maxsize(1280, 720)
        self.title("I need somebody (Help) not just anybody (Help) you know I need someone, help So much younger than today (I never need) I never needed anybodys help in any way (Now) but now these days are gone (these days are gone) Im not so self assured(And now I find) now I find Ive changed my mindAnd opened up the doors")

        self.grid_rowconfigure(0, weight=1)
        self.grid_columnconfigure(0, weight=1) # This allows us to have a full window of scrollable frame

        self.scrollableframe = HelpFrame(master=self, width=1280, height=720)
        self.scrollableframe.grid(row=0, column=0, sticky="nsew")

# Help Frame (Scollable frame just to chuck the images on)
class HelpFrame(customtkinter.CTkScrollableFrame):
    def __init__(self, master, **kwargs):
        super().__init__(master, **kwargs)

        image1 = Images.open(os.path.dirname(os.path.realpath(__file__)) + r"\\storage\\MainWindowHelp.png")
        ctkimage1 = customtkinter.CTkImage(image1, size=(994, 576))
        ctklabel1 = customtkinter.CTkLabel(image=ctkimage1, text="", master=self)
        ctklabel1.pack(padx=10,pady=10)

        image2 = Images.open(os.path.dirname(os.path.realpath(__file__)) + r"\\storage\\SearchWindowHelp.png")
        ctkimage2 = customtkinter.CTkImage(image2, size=(590, 745))
        ctklabel2 = customtkinter.CTkLabel(image=ctkimage2, text="", master=self)
        ctklabel2.pack(padx=10,pady=10)

        image3 = Images.open(os.path.dirname(os.path.realpath(__file__)) + r"\\storage\\PreviewWindowHelpAdd.png")
        ctkimage3 = customtkinter.CTkImage(image3, size=(994, 576))
        ctklabel3 = customtkinter.CTkLabel(image=ctkimage3, text="", master=self)
        ctklabel3.pack(padx=10,pady=10)

        image4 = Images.open(os.path.dirname(os.path.realpath(__file__)) + r"\\storage\\PreviewWindowHelp.png")
        ctkimage4 = customtkinter.CTkImage(image4, size=(994, 576))
        ctklabel4 = customtkinter.CTkLabel(image=ctkimage4, text="", master=self)
        ctklabel4.pack(padx=10,pady=10)
        
        

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

        # Sets up the watch location display
        self.wdframe = customtkinter.CTkScrollableFrame(self.backgroundlabel, orientation="horizontal", width=500, height=125, fg_color="#282828")
        self.wdframe.place(relx=0.025,rely=0.775)
        moviewatchproviders = api.watchproviders(movie["id"])
        try:
            buy = moviewatchproviders["buy"]
            self.buylabel = customtkinter.CTkLabel(master=self.wdframe, text="Buy: ", font=("Bahnschrift", 25))
            for e, i in enumerate(buy, start=1):
                image = Images.open(os.path.dirname(os.path.realpath(__file__)) + r"\\storage\\empty_icon.png")
                ctkimage = customtkinter.CTkImage(image, size=(50,50))
                ctklabel = customtkinter.CTkLabel(master=self.wdframe, image=ctkimage,text="")
                ctklabel.grid(row=0,column=e,padx=5)
                T = threading.Thread(target=lambda: streamingIcon(ctklabel, i["logo_path"]))
                T.start()
        except:
            self.buylabel = customtkinter.CTkLabel(master=self.wdframe, text="Buy: Not Available", font=("Bahnschrift", 25))
        try:
            rent = moviewatchproviders["flatrate"]
            self.rentlabel = customtkinter.CTkLabel(master=self.wdframe, text="Stream: ", font=("Bahnschrift", 25))
            for e, i in enumerate(rent, start=1):
                rimage = Images.open(os.path.dirname(os.path.realpath(__file__)) + r"\\storage\\empty_icon.png")
                rctkimage = customtkinter.CTkImage(rimage, size=(50,50))
                rctklabel = customtkinter.CTkLabel(master=self.wdframe, image=rctkimage,text="")
                rctklabel.grid(row=1,column=e,padx=5,pady=10)
                T = threading.Thread(target=lambda: streamingIcon(rctklabel, i["logo_path"]))
                T.start()
        except:
            self.rentlabel = customtkinter.CTkLabel(master=self.wdframe, text="Stream: Not Available", font=("Bahnschrift", 25))
        self.buylabel.grid(row=0,column=0,padx=5,sticky="w")
        self.rentlabel.grid(row=1,column=0,padx=5,pady=10,sticky="w")
        
        

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

# Another function again dedicated to manipulating stuff on threads
def streamingIcon(iconlabel, icon_path):
    location = 'https://image.tmdb.org/t/p/original/'
    image = Images.open(requests.get(location + icon_path, stream=True).raw)
    ctkimage = customtkinter.CTkImage(image, size=(50,50))
    iconlabel.after_idle(lambda: iconlabel.configure(image=ctkimage))

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

class ErrorWindow(customtkinter.CTkToplevel): # This window just alerts of an error in the case of an unfound search
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
