import random
deck = []
players = []
def generateDeck():
    AS = 0
    CA = 0
    DU = 0
    AM = 0
    CO = 0
    i = 0
    while(i<15):
        #print(i)

        number = random.randint(1,5)
        #print("Number " + str(number))
        if(number == 1):
            if(AS == 3):
                i = i-1
            else:
                deck.append("AS")
                AS = AS + 1

        elif(number == 2):
            if(CA == 3):
                i = i-1
            else:
                deck.append("CA")
                CA = CA + 1
        elif(number == 3):
            if(DU == 3):
                i = i-1
            else:
                deck.append("DU")
                DU = DU + 1
        elif(number == 4):
            if(AM == 3):
                i = i-1
            else:
                deck.append("AM")
                AM = AM + 1
        else:
            if(CO == 3):
                i = i-1
            else:
                deck.append("CO")
                CO = CO + 1
        i = i+1
    print("Generated Deck:\t" + str(deck))
    #Integer.parseInt()
def dealCards(p):
    i = 0
    while(i < p):
        add = []
        add.append(deck.pop(0))
        add.append(deck.pop(0))
        #print(add)
        players.append(add)
        #print(deck.pop(0))
        #players.append(list(deck.pop(0)).append(deck.pop(0)))
        i = i + 1

    print(players)

def createGame(numPlay):
    generateDeck()
    dealCards(numPlay)


print("Starting Coup")
play = input("How many players?\r\n")
createGame(int(play))
