import time
import pick
import random

Cards={ 
    "suit":["\u2660", "\u2665", "\u2663", "\u2666"],
    "number":[2, 3, 4, 5, 6, 7, 8, 9, 10],
    "Special":["J", "Q", "K", "A"]
}

listofcards=[]

def deck():
    cardcolor=""
    for i in Cards["suit"]:
        for b in Cards["number"] + Cards["Special"]:
            cardcolor = "red"
            if i == "\u2663" or i == "\u2660":
                cardcolor= "black"
            listofcards.append(f'{i} {b} {cardcolor}')

def playerscard():
    deck()
    player_card1=random.choice(listofcards)
    listofcards.remove(player_card1)
    player_card2=random.choice(listofcards)
    listofcards.remove(player_card2)
    return player_card1, player_card2

def dealercard():
    deck()
    dlr_card1=random.choice(listofcards)
    listofcards.remove(dlr_card1)
    dlr_card2=random.choice(listofcards)
    listofcards.remove(dlr_card2)
    return dlr_card1, dlr_card2


def calpoint(deck):
    b=0
    val=0
    for i in deck:          #splits the deck letter by letter check 1 by 1
        if i.isalpha():
            if i == "A":
                val+=10
            if i == "J":
                val+=10
            if i == "Q":
                val+=10
            if i == "K":
                val+=10
        if i.isdigit():
            b+=int(i)
    return b+val

def playerpoint(deck):
    currentpoints=calpoint(deck)
    return currentpoints
            


def cls():
    print("\033c")

def wait(x):
    time.sleep(x)

def game():
    print("Dealer is shuffeling")
#    wait(2)
    playercurrentcard=playerscard()
    dealercurrentcard=dealercard()
    playersdeck=" "
    for i in playercurrentcard:
        i=("| ")+i+(" | ")
        playersdeck= (playersdeck + i)
    dealersdeck=("| ")+str(dealercurrentcard[0])+(" | ")
    print(f"Player cards are:", playersdeck)
 #   wait(2)
    print(f"Dealer cards are:", dealersdeck, '[         ]')
    
    print (playerpoint(playersdeck)) #players points is calculated to be stored in background
 #   wait(5)
    
    #dealerpoint() #dealer points is also calculated to be stored in the background
    
#    table = ["[HIT]", "[STAND]"]
#    table, index = pick.pick(table, "Choose between", indicator='=>', default_index=0)
#    print(table)
#    if table=="[HIT]":
        #add card
        #add points
        #check if points are above or under 21
        #print bust or ask again
        #pass




options = ["[START]", "[OPTIONS]", "[EXIT]"]
option, index = pick.pick(options, "Welcome to BlackJack", indicator='=>', default_index=0)
#main program
if __name__ == "__main__":
    cls()
    print ("Welcome to BlackJack")
    print(option)
    if option[0]:
        cls()
        countdown=3
        while countdown != 0:
            print("game starting:", countdown)
            wait(1)
            countdown -=1
            cls()
        game()
    elif option[1]:
        pass
    else:
        pass


            
