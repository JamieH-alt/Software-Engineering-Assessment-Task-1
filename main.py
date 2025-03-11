import customtkinter
import math
import PIL.Image as Images
import requests
import os

# Sets the theme / appearance mode, so it doesnt follow the system (Forced dark mode because yes)
customtkinter.set_default_color_theme("dark-blue")
customtkinter.set_appearance_mode("dark")

# The Window (as a class)
class App(customtkinter.CTk):
    def __init__(self):
        super().__init__()
        self.geometry("1280x720") # Creates the window, with height, width and windows actual title
        self.title("MovieLister")
        self.minsize(1280, 720)
        self.maxsize(1280, 720)
        
        # Creates the Movie Lister title.
        self.customtitle = customtkinter.CTkTextbox(master=self,height=100,text_color="#ce3b3b",font=("Times New Roman",76), activate_scrollbars=False, width=1000, border_spacing=0, border_width=0, corner_radius=0, wrap="word")
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
            content = self.search.get()
            print(content)
            
        self.search.bind('<Return>', moviesearched)

        # Loads the WatchedMoviesFrame and sets its size and other variables
        self.watchedmoviesframe = WatchedMoviesFrame(self, width=1100, height=500, corner_radius=20)
        self.watchedmoviesframe.grid(pady=10,padx=10,row=1,column=0,columnspan=16,sticky="nsew")
            

# Frame that has all the watched movies
class WatchedMoviesFrame(customtkinter.CTkScrollableFrame):
    def __init__(self, master, **kwargs):
        super().__init__(master, **kwargs)

        # This loops through all movies and then provides a spot for the empty + movie cover.
        for movie_index in range(0, len(watchedmovies) + 1):
            movie_row = (1, 0)[movie_index % 2 == 0] # Basic tenerary operator meaning that ensures the ordering of the movies in which rows.
            if movie_row == 0:
                movie_column = math.floor((movie_index) / 2)
            else:
                movie_column = math.floor((movie_index) + 1 / 2) # Some tenerary operators in the following line, basically just validates the movie
            movie_frame = MovieFrame(self, watchedmovies[movie_index] if not movie_index >= len(watchedmovies) else None, False if not movie_index >= len(watchedmovies) else True, width=400, height=600)
            movie_frame.grid(row=movie_row,column=movie_column,padx=10,pady=10)

class MovieFrame(customtkinter.CTkFrame):
    def __init__(self, master, StoredMovie, empty, **kwargs):
        super().__init__(master, **kwargs)

        if empty:
            self.image = Images.open(os.path.dirname(os.path.realpath(__file__)) + r"\\storage\\empty.png")
        else:
            self.image = Images.open(requests.get(self.StoredMovie.coverstoragelocation, stream=True).raw)
        self.cover = customtkinter.CTkImage(light_image=self.image,size=(400, 600))

        self.label = customtkinter.CTkLabel(self, image=self.cover)
        self.label.pack()
        

""" This is the main code sections where we will connect the GUI into the modules and storage
    First we have a class for the movies to be stored
    and then the rest of the code
"""
# Movie Storage Class
class StoredMovie():
    def __init__(self):
        self.title = "" # Sets up the values within the class
        self.TMDbID = 0
        self.coverstoragelocation = ""
        
    def setvalues(title, TMDbID, coverstoragelocation): # Validates all the values to ensure they aren't wrongly typed.
        if isinstance(title, (str, unicode)):
            self.title = title
        else:
            print("Title is not a string... converting")
            self.title = str(title)
        if isinstance(TMdbID, int):
            self.TMDbID = TMDbID
        else:
            print("TMDbID is not a number... attempting conversion")
            try:
                self.TMDbID = int(TMDbID)
            except:
                print("Could not convert TMDbID to a number! Returning")
                return
        if isinstance(coverstoragelocation, (str, unicode)):
            self.coverstoragelocation = ""
        else:
            print("Cover Storage Location is not a string... converting")
            self.coverstoragelocation = str(coverstoragelocation)

watchedmovies = [] # Temporary, this should be read from a file.

""" Back to running the GUI """        
# Runs the App
app = App()
app.columnconfigure(0, weight=1)
app.mainloop()

