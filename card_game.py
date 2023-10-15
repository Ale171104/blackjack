from Player import Player
from DeckCards import DeckCards
import random
from deck_database import deck
#deck = DeckCards()
#for card in deck.cards:
#    card.printcard()

random.shuffle(deck.cards)

for card in deck.cards:
    card.printcard()


player1 = Player()

player1.add_card()

print("-------")

for card in player1.hand:
    card.printcard()

print("-------")

for card in deck.cards:
    card.printcard()







