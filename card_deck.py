import random
import math

class card:
    suit = ""
    rank = ""
    value = ""


    def __init__(self,suit,rank,value):
        self.suit = suit
        self.rank = rank
        self.value = value 