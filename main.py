import customtkinter

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
        self.configure(state="disabled")

        # Sets up the search bar and its storage.
        self.searchtext = ""

        self.search = customtkinter.CTkEntry(master=self, height=30, width=175, corner_radius=9, state="normal", textvariable=self.searchtext, placeholder_text="Search")
        self.search.grid(pady=10,padx=10,row=0,column=15,columnspan=1,sticky="nw")

        # Sets up so the search entry prints text on enter (To be linked to a function later)
        def moviesearched(event=None):
            content = self.search.get()
            print(content)
            
        self.search.bind('<Return>', moviesearched)

# Frame that has all the watched movies
class WatchedMoviesFrame(customtkinter.CTkFrame):
    def __init__(self, master, **kwargs):
        super().__init__(master, **kwargs)
        self.label = customtkinter.CTkLabel(self)
        self.label.grid(row=0, column=0, padx=20)

        
        
# Runs the App
app = App()
app.columnconfigure(0, weight=1)
app.mainloop()
