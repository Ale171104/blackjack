import random 
card = 0 
wins = 0
loses = 0

cardrandom = 0
cardset = []
cardbot = 0
cardsetbot = []
cardeck = [
    ["1","S"],
    ["2","S"],
    ["3","S"],
    ["4","S"],
    ["5","S"],
    ["6","S"],
    ["7","S"],
    ["8","S"],
    ["9","S"],
    ["10","S"],
    ["J","S"],
    ["Q","S"],
    ["K","S"],

    ["1","$"],
    ["2","$"],
    ["3","$"],
    ["4","$"],
    ["5","$"],
    ["6","$"],
    ["7","$"],
    ["8","$"],
    ["9","$"],
    ["10","$"],
    ["J","$"],
    ["Q","$"],
    ["K","$"],

    ["1","<3"],
    ["2","<3"],
    ["3","<3"],
    ["4","<3"],
    ["5","<3"],
    ["6","<3"],
    ["7","<3"],
    ["8","<3"],
    ["9","<3"],
    ["10","<3"],
    ["J","<3"],
    ["Q","<3"],
    ["K","<3"],

    ["1","*"],
    ["2","*"],
    ["3","*"],
    ["4","*"],
    ["5","*"],
    ["6","*"],
    ["7","*"],
    ["8","*"],
    ["9","*"],
    ["10","*"],
    ["J","*"],
    ["Q","*"],
    ["K","*"],
]

#def pluscard():
#    global card
#    card = random.randint(1,10)
#    global cardset 
#    cardset.append(card)

def addcard():
    global cardrandom
    global cardeck
    cardrandom = random.randint(0,len(cardeck))
    cardset.append(cardeck[cardrandom])
    cardeck.pop(cardrandom)
   

def addcardbot():
    global cardrandom
    global cardeck
    cardrandom = random.randint(0,len(cardeck))
    cardsetbot.append(cardeck[cardrandom])
    cardeck.pop(cardrandom)
    

def game():
    while True:
        global cardset
        global cardsetbot
        global wins 
        global loses
        cardset = []
        cardsetbot = []
        addcard()
        addcard()
        addcardbot()
        addcardbot()
        print("your cards", cardset, sum(cardset))
        print("house cards", "[x]" ,cardsetbot[1], )
        player()
        bot()
        if sum(cardset) > sum(cardsetbot) and sum(cardset) < 22 and sum(cardsetbot) < 22:
            wins = wins + 1
        elif sum(cardset) < sum(cardsetbot) and sum(cardset) < 22 and sum(cardsetbot) < 22:
            loses = loses + 1    

        print("wins", wins)
        print("loses", loses)

        if input("another round?") == "n":
            break    


def player():
    global loses
    loop = True
    while loop ==  True:
        morecard = input("1 more?(y/n)")

        if morecard == "y":
            addcard()
            print(cardset, sum(cardset))
            if sum(cardset) > 21:
                print("limit exeded")
                loses = loses + 1
                break
        elif morecard == "n":
            loop = False    

def bot():
    global wins
    global cardsetbot
    loop2 = True
    while loop2 == True:
        if sum(cardsetbot) < 17:
            addcardbot
            print(cardsetbot, sum(cardsetbot))
        elif sum(cardsetbot) > 21:
            wins = wins + 1
            loop2 = False
        else:
            loop2 = False          
    

game()
