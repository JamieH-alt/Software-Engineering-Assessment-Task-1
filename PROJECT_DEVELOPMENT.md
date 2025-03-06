# MovieLister

## **Requirements Definition**
### **Functional Requirements**
* Users must be able to search for Movies by title (accounting for bad capitalisation)
* Users must have the ability to select watch status (Watched, Not-Watched)
* The User should have an obvious search bar to look for movies
* The User should be able to click an icon at any time to access the home page.
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



Watched Movies
```{r, tidy=FALSE, eval=FALSE, highlight=FALSE }
BEGIN watchedMovies
  movielist = read(watchedmovies.json)
  FOR movie = firstmovie in movielist TO lastmovie in movielist STEP 1
    movietitle = read(movie, title)
    moviecover = read(movie, cover)
    movieid = movie
    RETURN movietitle, moviecover, movieid
  NEXT movie 
END watchedMovies
```

Preview Movie
```{r, tidy=FALSE, eval=FALSE, highlight=FALSE }
BEGIN previewMovie (movie_id, description, title, genreids, coverimage, rating)
  Display movie_id
  Display description
  Display title
  Display coverimage
  Display rating
  CASEWHERE genreid exvalues to
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
    9648: genre = Mystery
    10749: genre = Romance
    878: genre = SciFi
    53: genre = Thriller
    10752: genre = war
    37: genre = western
  ENDCASE
  Display genre
END previewMovie (movie_id, description, title, genreids, coverimage, rating)