from deck_database import deck

class Player:
    
    wins = 0
    loses = 0
    draws = 0
    win_ratio = 0
    limit_exceed = False 

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

    def return_cards(self):
        for card in self.hand:
            deck.cards.append(card)
        self.hand.clear()
        self.total_value = 0


    def ratio(self):
        if self.loses > 0:
            self.win_ratio = self.wins / self.loses


    def print_record(self):    
        print("wins",self.wins,"|","loses",self.loses,"|","draws",self.draws,"|","win ratio",self.win_ratio)

        