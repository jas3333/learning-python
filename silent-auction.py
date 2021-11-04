from os import system

def clear():
    _ = system("clear")

auction_bidders = {}

def bidders(bidder_name, bid_amount):
    auction_bidders[bidder_name] = bid_amount

def highest_bidder(bidder_list):
    high_bid = 0
    bidder_key = ""
    for bidder in bidder_list:
        bid_amount = bidder_list[bidder]
        if bid_amount > high_bid:
            high_bid = bid_amount
            winner = bidder
    print(f"The winner is {winner} with a bid of ${high_bid}.")

print("Welcome to the silent auction.")

while True:
    name = input("What is your name?\n>>> ")
    bid = int(input("How much would you like to bid?\n>>> $"))
    bidders(name, bid)
    any_additional_bidders = input("Are there any additional bidders?('yes' or 'no')\n>>> ")
    if any_additional_bidders == "yes":
        clear()
    elif any_additional_bidders == "no":
        print("Ok, the winner is.....")
        break

highest_bidder(auction_bidders)

