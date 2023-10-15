

class Card:

    

    def __init__(self,suit,rank):
        self.suit = suit
        self.rank = rank
 
        

    def get_value(self):
        try:
            value = int(self.rank)
            return value
        except ValueError:
            if self.rank == "A":
                return 1
            
            if self.rank == "J":
                return 10
            
            if self.rank == "Q":
                return 10

            if self.rank == "K":
                return 10  



    def printcard(self):
       print(self.suit,self.rank,self.get_value())

     