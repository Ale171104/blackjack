from Player import Player
from DeckCards import DeckCards
import random
from deck_database import deck


#deck = DeckCards()
#for card in deck.cards:
#    card.printcard()

loop = True

random.shuffle(deck.cards)

player1 = Player()

 
player1.add_card()
player1.add_card()

for card in player1.hand:
    card.printcard_hand()

player1.print_total_value()

while loop == True:
    more1 = input("1 more?(Y/N): ")
    if more1 == "Y" or more1 == "y":
        player1.add_card()

        for card in player1.hand:
            card.printcard_hand()

        player1.print_total_value()

        if player1.total_value == 21:
            loop = False

        elif player1.total_value > 21:
            print("limit exceeded")  
            loop = False        


    elif more1 == "N" or more1 == "n":
        loop = False


#for card in player1.hand:
    #card.printcard()





#player1.print_total_value()  
#player1.print_hand()  







