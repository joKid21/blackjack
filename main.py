import time
import pick
import random
from collections import Counter

Cards={ 
    "suit":["\u2660", "\u2665", "\u2663", "\u2666"],
    "number":[2, 3, 4, 5, 6, 7, 8, 9, 10],
    "Special":["J", "Q", "K", "A"]
}

list_of_cards=[]
Stored_A_value= 0

def Create_deck():
    cardcolor=""
    for i in Cards["suit"]:
        for b in Cards["number"] + Cards["Special"]:
            cardcolor = "red"
            if i == "\u2663" or i == "\u2660":
                cardcolor= "black"
            list_of_cards.append(f'{i} {b} {cardcolor}')

def Starter_players_cards():
    player_card1=random.choice(list_of_cards)
    list_of_cards.remove(player_card1)
    player_card2=random.choice(list_of_cards)
    list_of_cards.remove(player_card2)
    return player_card1, player_card2

def Starter_dealers_card():
    dlr_card1=random.choice(list_of_cards)
    list_of_cards.remove(dlr_card1)
    dlr_card2=random.choice(list_of_cards)
    list_of_cards.remove(dlr_card2)
    return dlr_card1, dlr_card2

def hit():
    hit_card1=random.choice(list_of_cards)
    list_of_cards.remove(hit_card1)
    return hit_card1

def calculate_point(deck, who):
    skip="\n"
    global Stored_A_value
    print_deck=str(deck)
    cards_split=print_deck.split(" ")
    Stored_digit=0
    Total_sum=0
    stored_letter=[]
    for i in cards_split:               #splits the deck letter by letter check 1 by 1
        if i.isalpha():
            if i == "K" or i == "Q" or i == "J" or i == "A":
                stored_letter.append(i)
        if i.isdigit():
            Stored_digit+=int(i)
        Stored_sum=Stored_digit+Total_sum
    if len(deck) <= 2:
        Stored_A_value=0
        if "A" in stored_letter and "K" in stored_letter:
            return 21
        if "A" in stored_letter and "Q" in stored_letter:
            return 21
        if "A" in stored_letter and "J" in stored_letter:
            return 21
        if "A" in stored_letter and Stored_digit==10:
            return 21
    if who == "player":
        types=[]
        if len(stored_letter) == 2:
            if stored_letter[0] == "A" and stored_letter[1] == "A":
                Total_sum+=12
        elif len(stored_letter) >= 3:
            if stored_letter[0] == "A" and stored_letter[1] == "A" and stored_letter[2] == "A":
                Total_sum+=13
        elif len(stored_letter) >= 4:
            if stored_letter[0] == "A" and stored_letter[1] == "A" and stored_letter[2] == "A" and stored_letter[3] == "A":
                Total_sum+=14
        for i in stored_letter:
            if i == "K" or i == "Q" or i == "J":
                Total_sum+=10
            if i == "A" and len(deck) == 2:
                while True:
                    printdeck=str(deck)
                    title="current deck= "+printdeck+skip+"do u want your A to be a 11 or 1?: "
                    table = ["[ 1 ]", "[ 11 ]"]
                    table, index = pick.pick(table, title, indicator='=>', default_index=0)
                    print (table)
                    if table == "[ 11 ]":
                        Total_sum+=11
                        Stored_A_value=11
                        break
                    elif table == "[ 1 ]":
                        Total_sum+=1
                        Stored_A_value=1
                        break
                    else:
                        print ("Invalid")
            if i == "A" and len(deck) > 2:
                types.append(i)
                if Stored_A_value > 0:
                    Total_sum+=(Stored_A_value+1)
            Total_A_calculation = dict(Counter(types))
            if "A" in Total_A_calculation:
                if Total_A_calculation["A"]== 2:
                    Total_sum+=(Stored_A_value+1)
                if Total_A_calculation["A"]== 1:
                    Total_sum+=1
    if who == "dealer":
        if stored_letter == "AA":
            Total_sum+=12
        else:
            for i in stored_letter:
                if i == "K" or i == "Q" or i == "J":
                    Total_sum+=10
                if i == "A":
                    Total_sum+=11   
    Total_points=Total_sum+Stored_sum
    return Total_points

def player_points(deck):
    who="player"
    currentpoints=calculate_point(deck,who)
    return currentpoints

def dealer_points(deck):
    who="dealer"
    currentpoints=calculate_point(deck,who)
    return currentpoints
            
def cls():
    print("\033c")

def wait(x):
    time.sleep(x)

def game():
    Create_deck
    Skip="\n"
    title="Dealer is Shufling"+Skip+"Player cards are:"+'[ *HIDDEN* ]'+'[ *HIDDEN* ]'+Skip+"Dealer cards are: "+'[ *HIDDEN* ]'+'[ *HIDDEN* ]'
    print(title)
    wait(2)
    player_current_card=Starter_players_cards()
    dealer_current_card=Starter_dealers_card()
    players_deck=" "
    for i in player_current_card:
        i=("[ ")+i+(" ] ")
        players_deck= (players_deck + i)
    dealers_deck=("[ ")+str(dealer_current_card[0])+(" ] ")
    player_current_points=(player_points(player_current_card))
    dealer_current_points=(dealer_points(dealer_current_card))
    playerprintpoints=str(player_current_points)
    bust=False
    while not bust:
        title="Player's turn"+Skip+"Player cards are:" + players_deck + playerprintpoints + Skip + "Dealer cards are: " + dealers_deck + '[ *HIDDEN* ]'
        table = ["[HIT]", "[STAND]"]
        table, index = pick.pick(table, title, indicator='=>', default_index=0)
        print(table)
        if table=="[HIT]":
            print_added_card=hit()
            player_current_card=player_current_card+(print_added_card,)
            players_deck=""
            for b in player_current_card:
                b=(" [ ")+(b)+(" ]")
                players_deck= (players_deck + b)
                cls()
            player_current_points=(player_points(player_current_card))
            dealers_deck=""
            for m in dealer_current_card:
                m=("[ ")+m+(" ] ")
                dealers_deck= (dealers_deck + m)
        if table=="[STAND]":
            cls()
            title="Player choose stand"+Skip+"Player cards are:" + players_deck + Skip + "Dealer cards are: " + dealers_deck + '[ *HIDDEN* ]'
            print(title)
            wait(2)
            player_current_card=player_current_card
            players_deck=""
            for b in player_current_card:
                b=(" [ ")+(b)+(" ]")
                players_deck= (players_deck + b)
                cls()
            player_current_points=(player_points(player_current_card))
            dealers_deck=""
            for m in dealer_current_card:
                m=("[ ")+m+(" ] ")
                dealers_deck= (dealers_deck + m)


        if player_current_points >=22:
            title="Player cards are:" + players_deck + Skip + "Dealer cards are: " + dealers_deck  + Skip + "Player BUST"    #add card   #add points
            print(title)
            bust=True
            break

        elif player_current_points <= 21:
            title="Player cards are:" + players_deck + Skip + "Dealer cards are: " + dealers_deck + '[ *HIDDEN* ]'
            if table == "[HIT]":
                table = ["[HIT]", "[STAND]"]
                table, index = pick.pick(table, title, indicator='=>', default_index=0)
            print(title)
            cls()
            title="Player cards are:" + players_deck + Skip + "Dealer cards are: " + dealers_deck + '[ *HIDDEN* ]' + Skip + "Dealers turn"
            print(title)
            cls()
            wait(2)
            title="Player cards are:" + players_deck + Skip + "Dealer cards are: " + dealers_deck + Skip + "Dealers turn"
            print(title)
            break
        
        elif player_current_points == 21:
            title="Player cards are:" + players_deck + Skip + "Dealer cards are: " + dealers_deck + '[ *HIDDEN* ]' + Skip + "You have BlackJack"
            wait(2)
            title="Player cards are:" + players_deck + Skip + "Dealer cards are: " + dealers_deck + '[ *HIDDEN* ]' + Skip + "You have BlackJack" + Skip + "Dealers turn"
            wait(2)
            title="Player cards are:" + players_deck + Skip + "Dealer cards are: " + dealers_deck + Skip + "You have BlackJack" + Skip + "Dealers turn"
            if dealer_current_points <= 17:
                newcard=hit()
                dealer_current_card=dealer_current_card+(newcard,) 
            elif dealer_current_card == 21:
                title="Player cards are:" + players_deck + Skip + "Dealer cards are: " + dealers_deck + Skip + "PUSH"
#                table = ["[NEW GAME]", "[EXIT]"]
#                table, index = pick.pick(table, title, indicator='=>', default_index=0)
            print(f"You have BlackJack")
            break
        if dealer_current_points == player_current_points:
            title="Player cards are:" + players_deck + Skip + "Dealer cards are: " + dealers_deck + Skip + "PUSH"
    print(player_current_points)
                 
                
        #check if points are above or under 21
        #print bust or ask again
        #pass


#main program
if __name__ == "__main__":
    playing=True
    while playing:
        Title="Welcome to BlackJack"
        skip_line="\n"
        options = ["[START]", "[OPTIONS]", "[EXIT]"]
        option, index = pick.pick(options, Title, indicator='=>', default_index=0)
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

            

