import random, sys
from art import blackjack_logo
from os import system
from modules import Players


card_list = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]


def clear():
    _ = system("clear")


def play_again():
    cmd = input("\nWould you like to play agian? >>> ")
    if cmd == "y" or cmd == "yes":
        game()
    else:
        sys.exit()


def game():

    # Create the players
    dealer = Players([], "cpu")
    user = Players([], "human")

    # Deal cards to the players
    dealer.deal_cards(card_list)
    user.deal_cards(card_list)

    while True:
        clear()
        print(blackjack_logo)

        # Display player cards, and also check if they break 21
        user.display_cards()
        dealer.display_cards()
        if user.bust == True:
            print("\nLooks like you went bust. You lose.")
            play_again()

        cmd = input("\n[hit] or [stand] [q to quit] >>> ")
        if cmd == "hit":
            user.deal_cards(card_list)
        elif cmd == "q":
            sys.exit()
        elif cmd == "stand":
            break
    
    # Tells the game to show the dealers hand now. 
    dealer.stand = True

    # Deals cards to the dealer as long as they are under 17.
    while dealer.score < 17 or dealer.score > 21 and dealer.score == 21:
        dealer.deal_cards(card_list)
        dealer.check_score()

    clear()
    print(blackjack_logo)
    user.display_cards()
    dealer.display_cards()

    if dealer.score > 21:
        print("The dealer went bust, you win!")
    elif dealer.score > user.score:
        print("The dealer had a better hand. You lost.")
    elif dealer.score == user.score:
        print("Looks like it's a draw.")
    elif user.score > dealer.score:
        print("Nice you won!")

    play_again()
game()
