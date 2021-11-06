import random, sys 
from os import system
from art import blackjack_logo

def clear():
    _ = system("clear")

def deal_card():
    cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
    card = random.choice(cards)
    return card

def calculate_score(players_cards):
    if 11 in players_cards and sum(players_cards) > 21:
        players_cards.remove(11)
        players_cards.append(1)
    player_score = sum(players_cards)
    return player_score

def play_again():
    play = input("\n[y] to play again or [n] to exit. >>> ")
    if play == "y":
        blackjack()
    elif play == "n":
        print("Ok, have a nice day.")
        sys.exit()
    else:
        print("That isn't an option.")
        play_again()
    
def compare_scores(player, dealer):
    if player == dealer:
        print("\nIt's a push.")
        return
    elif player > dealer:
        print("\nNice, you won!")
        return
    elif dealer > 21:
        print("\nThe dealer went bust. You win!")
        return
    elif player < dealer:
        print("\nLooks like the dealer beat you. Better luck next time.")
        return
    
def blackjack():
    player_cards = []
    dealer_cards = []

    for i in range(2):
        player_cards.append(deal_card())
        dealer_cards.append(deal_card())
        
    player_score = calculate_score(player_cards)
    dealer_score = calculate_score(dealer_cards)

    while True:
        clear()
        print(blackjack_logo)
        print(f"Player cards: {player_cards}      -- {player_score} -- ")
        print(f"Dealer hand:  [{dealer_cards[0]}, ?]        -- ? -- ")

        if player_score > 21: 
            print("\nYou went bust. Would you like to play again?")
            play_again()
        elif player_score == 21:
            break

        player_move = input("\n[hit] or [stand] >>> ")
        if player_move == "hit":
            player_cards.append(deal_card())
            player_score = calculate_score(player_cards)
        elif player_move == "stand":
            break
            

    while dealer_score < 17 or dealer_score > 21 and dealer_score == 21:
        dealer_cards.append(deal_card())
        dealer_score = calculate_score(dealer_cards)
    print(f"\nPlayer hand: {player_cards}   -- {player_score} -- ")
    print(f"Dealer hand: {dealer_cards}   -- {dealer_score} -- ")
    compare_scores(player_score, dealer_score)
    play_again()

blackjack()











