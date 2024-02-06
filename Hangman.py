import random
from imdbTop50 import movies as imdbTop50
from MCU_Movies import movies as MCU_Movies

print("Welcome to the Hangman Game! Let's see if you can guess this Movie!")
while(True):
    userInput= (int(input("1. Start\n2. Exit\n--> ")))
    if userInput == 1:
        random_movie = random.choice(MCU_Movies + imdbTop50).upper() #generates a random Movie from the list
        guessed_letters = list()
        display = " "
        chance = 5
        while(True):
            display = " "
            for i in random_movie:
                if i in guessed_letters:
                    display += i + " "
                elif i.isalpha():
                    display += "_ "
                else:
                    display += i + " "
            print(display + "\n")

            if "_" not in display:
                print("Congratulations! You've guessed the movie: " +  random_movie)
                print("\nWould you like to play again?")
                break
            elif chance >= 1 and chance <= 5:
                guess = input("Enter a Character: ")
                
                while (True):
                    if guess.isalpha() != True:
                        guess = input("Enter a valid Character: ")
                    elif guess.upper() in guessed_letters:
                        guess = input("You've Already guessed the letter!\nEnter a valid Character: ")
                    elif len(guess) != 1:
                        guess = input("Enter only one Character: ")
                    else:
                        break
                
                if guess.upper() not in random_movie:
                    chance-=1
                    print("You've only " + str(chance) + " chance left!")

                guessed_letters.append(guess.upper())
            else:
                print("Correct Answer: ",random_movie)
                print("Better Luck Next Time!!!")
                print("\nWould you like to play again?")
                break
    elif userInput == 2:
        print("Exit")
        break
    else:
        print("Enter a valid Number: ")