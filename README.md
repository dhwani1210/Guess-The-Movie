Hangman.py
Purpose:
This Python script implements a basic hangman game where the player needs to guess a movie title. 
The game randomly selects a movie from a combination of two movie lists: top 50 movies from IMDb and movies from the Marvel Cinematic Universe (MCU).

How to Use:
Run the Hangman.py script.
The game will display a menu with options to start or exit.
If the player chooses to start:
A random movie title is chosen from the combined list of IMDb top 50 movies and MCU movies.
The player has to guess the movie title by entering one character at a time.
The player has limited chances to guess the correct movie title.
If the player guesses the movie correctly within the given chances, they win; otherwise, they lose.
After each game, the player can choose to play again or exit.

Files Used:
imdbTop50.py: Retrieves the top 50 movie titles from IMDb.
MCU_movies.py: Retrieves the movie titles from the Marvel Cinematic Universe.


imdbTop50.py
Purpose:
This Python script scrapes IMDb's website to obtain the top 50 movie titles from a specific list.

MCU_movies.py
This Python script scrapes Wikipedia to obtain the list of movie titles from the Marvel Cinematic Universe.
