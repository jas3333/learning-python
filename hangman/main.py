from brain import WordGame
from os import system
from data import game_data
import random


def clear():
    _ = system("clear")

def main():

    word_list = ["computer", "apple", "couch", "chair", "kitty", "monitor", "toaster", "microwave"]
    chosen_word = random.choice(word_list)
    guessed_letters = ""
    tries = 7
    game = WordGame(chosen_word, guessed_letters)
    clear()


    while tries > 0:
        game = WordGame(chosen_word, guessed_letters)
        game.display_hang(game_data, tries)
        game.present_word()
        if game.game_on == False:
            break
        guess = input(f"\nGuess a letter -- [{guessed_letters}] -- Tries left -- {tries} -- >>> ")
        if guess not in chosen_word and guess not in guessed_letters:
            tries -= 1
        clear() 
        if guess in guessed_letters:
            print("You already tried that one.")
        else:
            guessed_letters += guess

    
    if tries == 0:
        game.display_hang(game_data, tries)
        game.present_word()
        print("\nLooks like you lost. Better luck next time.")

    play_again = input("Would you like to play again? >>> ")
    if play_again == "y" or play_again == "yes":
        main()
    else:
        print("Ok, have a nice day.")

main()



