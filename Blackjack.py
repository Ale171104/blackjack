from player_database import player1
from deck_database import deck
import random

class Blackjack:

    #def __init__(self):
        
    def start():
        random.shuffle(deck.cards)
        player1.add_card()
        player1.add_card()
        for card in player1.hand:
            card.printcard_hand()

