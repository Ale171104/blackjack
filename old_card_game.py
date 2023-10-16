from Player import Player
from DeckCards import DeckCards
import random
from deck_database import deck
from player_database import player1,house


#deck = DeckCards()
#for card in deck.cards:
#    card.printcard()

player1.get_name()
player1.print_name()


def victory_condition():
    if player1.total_value > house.total_value and player1.total_value < 22 and house.total_value < 22:
        player1.wins = player1.wins + 1

    elif player1.total_value < house.total_value and player1.total_value < 22 and house.total_value < 22:
        player1.loses = player1.loses + 1

    elif player1.total_value == house.total_value and player1.total_value < 22 and house.total_value < 22:
        player1.draws = player1.draws + 1        



gaming = True
loop = True

print(len(deck.cards))



 


while gaming == True:
    
    player1.limit_exceed = False
    random.shuffle(deck.cards)

    player1.add_card()
    player1.add_card()

    house.add_card()
    house.add_card()

    print("your hand")
    for card in player1.hand:
        card.printcard_hand()

    player1.print_total_value()
    print("--------")


    print("house hand")
    for card in house.hand:
        card.printcard_hand()


    house.print_total_value()
    print("--------")


    while True:
        more1 = input("1 more?(Y/N): ")
        
        if more1.lower() == "y" or more1.lower() == "yes":
            player1.add_card()

            print("your card")
            for card in player1.hand:
                card.printcard_hand()

            player1.print_total_value()
            print("--------")

            if player1.total_value == 21:
                break

            elif player1.total_value > 21:
                player1.loses = player1.loses + 1
                player1.limit_exceed = True

                print("limit exceeded")  
                break        


        else:
            break

    while True:
        if house.total_value < 17:
            house.add_card()

            for card in house.hand:
                card.printcard_hand()

            house.print_total_value()
            print("--------")


        elif house.total_value >= 17 and house.total_value < 22:
            print("house hand")
            for card in house.hand:
                card.printcard_hand()

            house.print_total_value()


            print("your hand")
            for card in player1.hand:
                card.printcard_hand()

            player1.print_total_value()

            break

        elif house.total_value > 22: 
            if player1.limit_exceed == False:
                player1.wins = player1.wins + 1

            print("house hand")
            for card in house.hand:
                card.printcard_hand()

            house.print_total_value()


            print("your hand")
            for card in player1.hand:
                card.printcard_hand()

            player1.print_total_value()
            print("you won")

            break
        
        else:
            break

    victory_condition()
    player1.ratio()
    player1.print_record()

    player1.return_cards()
    house.return_cards()  

    print(len(deck.cards))

    game_running = input("stop playing?(Y/N): ")
    if game_running.lower() == "y" or game_running.lower() == "yes":
        break
  

        








