from Player import Player
from deck_database import deck
import random

class Blackjack:

    players = []

    gaming = True
    
    def __init__(self):
        numbers_of_players = int(input("how many players will join?(1-4): "))
        for current_player in range(numbers_of_players):
            current_player = Player()
            current_player.get_name()
            self.players.append(current_player)

        for player in self.players:
            player.print_name()    


    def start(self):
        def victory_condition():
            for player in self.players:            
                if player.total_value > house.total_value and player.total_value < 22 and house.total_value < 22:
                    player.wins = player.wins + 1
                    print(player.print_name()," won")

                elif player.total_value < house.total_value and player.total_value < 22 and house.total_value < 22:
                    player.loses = player.loses + 1
                    print(player.print_name()," lose")

                elif player.total_value == house.total_value and player.total_value < 22 and house.total_value < 22:
                    player.draws = player.draws + 1
                    print(player.print_name()," drawn")


        
        

        print(len(deck.cards))



        


        while self.gaming == True:
            
            for player in self.players:
                player.limit_exceed = False

            #player1.limit_exceed = False
            random.shuffle(deck.cards)



            for player in self.players:
                player.add_card()
                player.add_card()

            #player1.add_card()
            #player1.add_card()

            house.add_card()
            house.add_card()


            for player in self.players:
                print(player.print_name(),"hand")
                
                player.print_hand()
                player.print_total_value()
                print("--------")



            #print("your hand")
            #for card in player1.hand:
            #    card.printcard_hand()

            #player1.print_total_value()
            #print("--------")


            print("house hand")
            for card in house.hand:
                card.printcard_hand()


            house.print_total_value()
            print("--------")

            for player in self.players:
                while True:

                    print(player.print_name())
                    more1 = input("1 more?(Y/N): ")
                    
                    if more1.lower() == "y" or more1.lower() == "yes":
                        player.add_card()

                        print(player.print_name()," hand")
                        for card in player.hand:
                            card.printcard_hand()

                        player.print_total_value()
                        print("--------")

                    if player.total_value == 21:
                                break

                    elif player.total_value > 21:
                        player.loses = player1.loses + 1
                        player.limit_exceed = True

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
                    
                    print(player.print_name()," hand")
                    for card in player.hand:
                        card.printcard_hand()
                    player.print_total_value()

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
                    for player in self.players:
                        if player.limit_exceed == False:
                            player.wins = player.wins + 1

                    for player in self.players:
                        print(player.print_name()," hand")
                        for card in player.hand:
                            card.printcard_hand()
                            player.print_total_value()    

                    print("house hand")
                    for card in house.hand:
                        card.printcard_hand()

                    house.print_total_value()


                    #print("your hand")
                    #for card in player1.hand:
                    #    card.printcard_hand()

                    #player1.print_total_value()
                    

                    break
                
                else:
                    break

            victory_condition()

            for player in self.players:
                player.ratio()
                player.print_record()

                player.return_cards()

            house.return_cards()  

            print(len(deck.cards))

            game_running = input("stop playing?(Y/N): ")
            if game_running.lower() == "y" or game_running.lower() == "yes":
                break
        

    '''
    #def victory_condition():
        if player1.total_value > house.total_value and player1.total_value < 22 and house.total_value < 22:
            player1.wins = player1.wins + 1

        elif player1.total_value < house.total_value and player1.total_value < 22 and house.total_value < 22:
            player1.loses = player1.loses + 1

       elif player1.total_value == house.total_value and player1.total_value < 22 and house.total_value < 22:
            player1.draws = player1.draws + 1 


                   
    '''    
   

