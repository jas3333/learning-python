import random


class Players:

    # Blueprint for the players
    def __init__(self, hand, player_type):
        self.hand = hand
        self.player_type = player_type
        self.bust = False
        self.score = 0
        self.stand = False

    # Deal cards based on hand size.
    def deal_cards(self, cards):
        if len(self.hand) > 1:
            self.hand.append(random.choice(cards))
        else:
            for _ in range(2):
                self.hand.append(random.choice(cards))

    # Display player hands based on player type
    def display_cards(self):
        self.check_score()
        if self.player_type == "cpu" and self.stand == False:
            print(f"Dealers hand: [{self.hand[0]} ?] >")
        elif self.player_type == "cpu" and self.stand == True:
            print(f"Dealers hand: {self.hand} -- {self.score} -- ")
        else:
            print(f"Player hand: {self.hand} -- {self.score} -- ")


    def check_score(self):
        self.score = sum(self.hand)
        if self.score > 21 and self.player_type == "human" and 11 in self.hand:
            self.hand.remove(11)
            self.hand.append(1)
            self.score = sum(self.hand)
        if self.score > 21:
            self.bust = True


                

        

        

