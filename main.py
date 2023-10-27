import time
import pick
import random
from collections import Counter

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

def dealerscard():
    dlr_card1=random.choice(listofcards)
    listofcards.remove(dlr_card1)
    dlr_card2=random.choice(listofcards)
    listofcards.remove(dlr_card2)
    return dlr_card1, dlr_card2

def hit():
    hit_card1=random.choice(listofcards)
    listofcards.remove(hit_card1)
    return hit_card1

def calpoint(deck, who):
    pdeck=str(deck)
    cards_split=pdeck.split(" ")
    b=0
    val=0
    stored_letter=[]
    for i in cards_split:               #splits the deck letter by letter check 1 by 1
        if i.isalpha():
            if i == "K" or i == "Q" or i == "J" or i == "A":
                stored_letter.append(i)
        if i.isdigit():
            b+=int(i)
        storedval=b+val
    if len(deck) <= 2:
        if "A" in stored_letter and "K" in stored_letter:
            return 21
        if "A" in stored_letter and "Q" in stored_letter:
            return 21
        if "A" in stored_letter and "J" in stored_letter:
            return 21
        if "A" in stored_letter and b==10:
            return 21
    if who == "player":
        types=[]
        if "AA" in stored_letter:
            val+=12
        else:
            global storedAvalue
            storedAvalue= -1
            if storedAvalue < 1:
                storedAvalue = 0
            for i in stored_letter:
                if i == "K" or i == "Q" or i == "J":
                    val+=10
                if i == "A" and len(deck) <= 2:
                    while True:
                        A=input("do u want your A to be a 11 or 1?: ")
                        if A == "11":
                            val+=11
                            storedAvalue=11
                            break
                        elif A == "1":
                            val+=1
                            storedAvalue=1
                            break
                        else:
                            print ("Invalid")
                elif i == "A" and len(deck) >= 2:
                    types.append(i)
                    if storedAvalue > 0:
                        val+=(storedAvalue+1)
            a = dict(Counter(types))
            if "A" in a:
                if a["A"]== 2:
                    val+=(storedAvalue+2)


    if who == "dealer":
        if stored_letter == "AA":
            val+=12
        else:
            for i in stored_letter:
                if i == "K" or i == "Q" or i == "J":
                    val+=10
                if i == "A":
                    val+=11   
    points=val+storedval
    return points

def playerpoint(deck):
    who="player"
    currentpoints=calpoint(deck,who)
    return currentpoints

def dealerpoint(deck):
    who="dealer"
    currentpoints=calpoint(deck,who)
    return currentpoints
            
def cls():
    print("\033c")

def wait(x):
    time.sleep(x)

def game():
    print("Dealer is shuffeling")
#    wait(2)
    BlackJack=False
    playercurrentcard=playerscard()
    dealercurrentcard=dealerscard()
    playersdeck=" "
    for i in playercurrentcard:
        i=("[ ")+i+(" ] ")
        playersdeck= (playersdeck + i)
    dealersdeck=("[ ")+str(dealercurrentcard[0])+(" ] ")
    print(f"Player cards are:", playersdeck)
    #wait(2)
    print(f"Dealer cards are:", dealersdeck, '[ *HIDDEN* ]')

    playercurrent_points=(playerpoint(playercurrentcard))
    dealercurrent_points=(dealerpoint(dealercurrentcard))

    if playercurrent_points == 21: #players points is calculated to be stored in background
        BlackJack=True
    if BlackJack:
        print(f"You have BlackJack")
    #wait(5)
    if dealercurrent_points == 21:
        pass
    #dealerpoint() #dealer points is also calculated to be stored in the background
    skip="\n"
    playerprintpoints=str(playercurrent_points)
    title="Player cards are:" + playersdeck + playerprintpoints + skip + "Dealer cards are: " + dealersdeck + '[ *HIDDEN* ]'
    table = ["[HIT]", "[STAND]"]
    table, index = pick.pick(table, title, indicator='=>', default_index=0)
    print(table)
    hit1=hit()
    bust=False
    while not bust:
        if table=="[HIT]":
            playercurrentcard=playercurrentcard+(hit1,)
            playersdeck=""
            for b in playercurrentcard:
                b=(" [ ")+(b)+(" ]")
                playersdeck= (playersdeck + b)
                cls()
            playercurrent_points=(playerpoint(playercurrentcard))
            
            dealers_deck=""
            for m in dealercurrentcard:
                m=("[ ")+m+(" ] ")
                dealers_deck= (dealers_deck + m)

            if playercurrent_points >=22:
                title="Player cards are:" + playersdeck + skip + "Dealer cards are: " + dealers_deck  + skip + "Player BUST"    #add card   #add points
                print(title)
                bust=True
                break

            elif playercurrent_points <= 21:
                title="Player cards are:" + playersdeck + skip + "Dealer cards are: " + dealersdeck + '[ *HIDDEN* ]'
                table = ["[HIT]", "[STAND]"]
                table, index = pick.pick(table, title, indicator='=>', default_index=0)
                print(title)
                break
            
            elif playercurrent_points == 21:
                title="Player cards are:" + playersdeck + skip + "Dealer cards are: " + dealersdeck + '[ *HIDDEN* ]' + skip + "You have BlackJack"
                wait(2)
                title="Player cards are:" + playersdeck + skip + "Dealer cards are: " + dealersdeck + '[ *HIDDEN* ]' + skip + "You have BlackJack" + skip + "Dealers turn"
                wait(2)
                title="Player cards are:" + playersdeck + skip + "Dealer cards are: " + dealers_deck + skip + "You have BlackJack" + skip + "Dealers turn"
                if dealercurrent_points <= 17:
                    newcard=hit()
                    dealercurrentcard=dealercurrentcard+(newcard,)
                    
                elif dealercurrentcard == 21:
                    title="Player cards are:" + playersdeck + skip + "Dealer cards are: " + dealers_deck + skip + "PUSH"
#                table = ["[NEW GAME]", "[EXIT]"]
#                table, index = pick.pick(table, title, indicator='=>', default_index=0)
                print(f"You have BlackJack")
                break
            if dealercurrent_points == playercurrent_points:
                title="Player cards are:" + playersdeck + skip + "Dealer cards are: " + dealers_deck + skip + "PUSH"

    print(playercurrent_points)
                 
                
        #check if points are above or under 21
        #print bust or ask again
        #pass

playering=True
while playering:
    Title="Welcome to BlackJack"
    skipline="\n"
    options = ["[START]", "[OPTIONS]", "[EXIT]"]
    option, index = pick.pick(options, Title, indicator='=>', default_index=0)
    #main program
    if __name__ == "__main__":
        cls()
        print ("Welcome to BlackJack")
        print(option)
        if option=="[START]":
            cls()
            countdown=3
            while countdown != 0:
                print("game starting:", countdown)
                wait(1)
                countdown -=1
                cls()
            game()
            break
        elif option=="[OPTIONS]":
            cls()
            Title="Welcome to BlackJack/OPTIONS"
            options = ["[DECK SIZE]", "[option2]", "[option3]", "[BACK]"]
            option, index = pick.pick(options, Title, indicator='=>', default_index=0)
            print("this where the game options are")
            wait(2)
        elif option=="[EXIT]":
            cls()
            print("GoodBye!")
            break

            

