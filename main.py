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
storedAvalue= 0

def deck():
    cardcolor=""
    for i in Cards["suit"]:
        for b in Cards["number"] + Cards["Special"]:
            cardcolor = "red"
            if i == "\u2663" or i == "\u2660":
                cardcolor= "black"
            listofcards.append(f'{i} {b} {cardcolor}')

def playerscard():
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
    skip="\n"
    global storedAvalue
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
        storedAvalue=0
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
        if len(stored_letter) == 2:
            if stored_letter[0] == "A" and stored_letter[1] == "A":
                val+=12
        elif len(stored_letter) >= 3:
            if stored_letter[0] == "A" and stored_letter[1] == "A" and stored_letter[2] == "A":
                val+=13
        elif len(stored_letter) >= 4:
            if stored_letter[0] == "A" and stored_letter[1] == "A" and stored_letter[2] == "A" and stored_letter[3] == "A":
                val+=14
        for i in stored_letter:
            if i == "K" or i == "Q" or i == "J":
                val+=10
            if i == "A" and len(deck) == 2:
                while True:
                    printdeck=str(deck)
                    title="current deck= "+printdeck+skip+"do u want your A to be a 11 or 1?: "
                    table = ["[ 1 ]", "[ 11 ]"]
                    table, index = pick.pick(table, title, indicator='=>', default_index=0)
                    print (table)
                    if table == "[ 11 ]":
                        val+=11
                        storedAvalue=11
                        break
                    elif table == "[ 1 ]":
                        val+=1
                        storedAvalue=1
                        break
                    else:
                        print ("Invalid")
            if i == "A" and len(deck) > 2:
                types.append(i)
                if storedAvalue > 0:
                    val+=(storedAvalue+1)
            a = dict(Counter(types))
            if "A" in a:
                if a["A"]== 2:
                    val+=(storedAvalue+1)
                if a["A"]== 1:
                    val+=1
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
    deck()
    skip="\n"
    title="Dealer is Shufling"+skip+"Player cards are:"+'[ *HIDDEN* ]'+'[ *HIDDEN* ]'+skip+"Dealer cards are: "+'[ *HIDDEN* ]'+'[ *HIDDEN* ]'
    print(title)
    wait(2)
    playercurrentcard=playerscard()
    dealercurrentcard=dealerscard()
    playersdeck=" "
    for i in playercurrentcard:
        i=("[ ")+i+(" ] ")
        playersdeck= (playersdeck + i)
    dealersdeck=("[ ")+str(dealercurrentcard[0])+(" ] ")
    playercurrent_points=(playerpoint(playercurrentcard))
    dealercurrent_points=(dealerpoint(dealercurrentcard))
    playerprintpoints=str(playercurrent_points)
    bust=False
    while not bust:
        title="Player's turn"+skip+"Player cards are:" + playersdeck + playerprintpoints + skip + "Dealer cards are: " + dealersdeck + '[ *HIDDEN* ]'
        table = ["[HIT]", "[STAND]"]
        table, index = pick.pick(table, title, indicator='=>', default_index=0)
        print(table)
        if table=="[HIT]":
            hit1=hit()
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
        if table=="[STAND]":
            cls()
            title="Player choose stand"+skip+"Player cards are:" + playersdeck + skip + "Dealer cards are: " + dealersdeck + '[ *HIDDEN* ]'
            print(title)
            wait(2)
            playercurrentcard=playercurrentcard
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
            if table == "[HIT]":
                table = ["[HIT]", "[STAND]"]
                table, index = pick.pick(table, title, indicator='=>', default_index=0)
            print(title)
            cls()
            title="Player cards are:" + playersdeck + skip + "Dealer cards are: " + dealersdeck + '[ *HIDDEN* ]' + skip + "Dealers turn"
            print(title)
            cls()
            wait(2)
            title="Player cards are:" + playersdeck + skip + "Dealer cards are: " + dealers_deck + skip + "Dealers turn"
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

            

