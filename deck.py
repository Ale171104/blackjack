from card_deck import Card 



class DeckCards:
    cards = []

    def __init__(self):
        suits = ["S","D","H","C"]
        ranks = ["A","2","3","4","5","6","7","8","9","10","J","Q","K"]

        for suit in suits:
            for rank in ranks:
                card = Card(suit,rank)
                self.cards.append(card)



