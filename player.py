from deck_database import deck

class Player:
    
    
    

    def __init__(self):
        self.hand = []
        self.total_value = 0

    def add_card(self):
        
        cardhand = deck.cards[-1] 
        self.hand.append(cardhand)
        deck.cards.pop(-1) 
        self.total_value = self.total_value + cardhand.get_value()
        #cardhand.printcard_hand()

    def print_total_value(self):
        print(self.total_value)
    
        