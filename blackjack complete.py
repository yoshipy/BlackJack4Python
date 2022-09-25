import random
from playsound import playsound
import re




wager2 = 0
playerpoints = 0
playerpoints2 = 0
dealerpoints = 0
playercard1 = 0
dealercard1 = 0
acep = 0
acep2 = 0
aced = 0
split = 'no'
hitstand2 = ''

bankroll = 3000
player1list = []
player2list = []
dealerlist = []
playerpointlist = []
playerpointlist2 = []
splitcheck = []


cardlist = [2, 2, 2, 2, 3, 3, 3, 3, 4, 4, 4, 4, 5, 5, 5, 5, 6, 6, 6, 6, 7, 7, 7, 7, 8, 8, 8, 8, 9, 9, 9, 9, 10, 10, 10, 10, 10, 'j', 'j', 'j', 'j', 'q', 'q', 'q', 'q', 'k', 'k', 'k', 'k', 'a', 'a', 'a', 'a']

print('hello, this is a game of blackjack, your starting balance is $3000, please tell me your name')
name = input('')
print('would you like to start the game?')
play = input('yes/no ')
print('how much do you want to wager?')

while True:
    try:
        wager = int(input(''))
        if wager > bankroll:
            print('you cannot bet more money than you have...')
            print('how much do you want to wager?')
            continue
        else:
            break
    except ValueError:
        print("Numbers only, please!")
        continue




def playerdrawcard():
    global playerpoints
    global playercard1
    print('{} draws the following card: '.format(name)) #chooses the player's second card, adds it to the player's card list and removes it from the list of cards in the deck.
    playercard1 = random.choice(cardlist)
    splitcheck.append(playercard1)
    player1list.append(playercard1)
    cardlist.remove(playercard1)
    acep = 0
    print(playercard1)
    print(name + " is currently holding the following cards: " + str(player1list))
    if playercard1 == 'j':
        playercard1 = (playercard1)=10
    if playercard1 == 'k':
        playercard1 = (playercard1)=10
    if playercard1 == 'q':
        playercard1 = (playercard1)=10
    if playercard1 == 'a':
        print('you drew an ace, please decide whether you want it to count for 1 or 11 points...')
        acevalue = input('type 1 or 11... ')
        playercard1 = int(acevalue)
    playerpoints = (playerpoints + playercard1)
    playerpointlist.append(playercard1)
        
    print(name + "'s current point total is: " + str(playerpoints))

    if playerpoints > 21:
        if 11 in playerpointlist:
            print('your score went over 21, but you have an ace worth 11 in your hand, changing it to be worth 1...')
            for n, i in enumerate(playerpointlist):
                if i == 11:
                    playerpointlist[n] = 1
                    playerpoints = sum(playerpointlist)
                    print('your new point total is ' + str(playerpoints))
                    
def playersplitdraw():    
    global playerpoints2
    print('{} draws the following card: '.format(name)) #chooses the player's second card, adds it to the player's card list and removes it from the list of cards in the deck.
    playercard2 = random.choice(cardlist)
    if len(player2list) == 0:
        player2list.append(playercard1)
    player2list.append(playercard2)
    
    cardlist.remove(playercard2)
    acep = 0
    print(playercard2)
    print(name + " is currently holding the following cards in their second hand: " + str(player2list))
    if playercard2 == 'j':
        playercard2 = (playercard2)=10
    if playercard2 == 'k':
        playercard2 = (playercard2)=10
    if playercard2 == 'q':
        playercard2 = (playercard2)=10
    if playercard2 == 'a':
        print('you drew an ace, please decide whether you want it to count for 1 or 11 points...')
        acevalue = input('type 1 or 11... ')
        playercard2 = int(acevalue)
    playerpoints2 = (playerpoints2 + playercard2)
    playerpointlist2.append(playercard2)
        
    print(name + "'s current point total in their second hand is: " + str(playerpoints2))

    if playerpoints2 > 21:
        if 11 in playerpointlist2:
            print('your score went over 21, but you have an ace worth 11 in your hand, changing it to be worth 1...')
            for n, i in enumerate(playerpointlist2):
                if i == 11:
                    playerpointlist2[n] = 1
                    playerpoints2 = sum(playerpointlist2)
                    print('your new point total is ' + str(playerpoints2))          
    

def dealerdrawcard():
    global dealerpoints
    print('the dealer draws the following card: ') #chooses the dealer's second card, adds it to the dealer's card list and removes it from the list of cards in the deck
    dealercard1 = random.choice(cardlist)
    cardlist.remove(dealercard1)
    dealerlist.append(dealercard1)
    aced = 0
    print(dealercard1)
    print("the dealer is currently holding the following cards: " + str(dealerlist))

    if dealercard1 == 'j':
        dealercard1 = (dealercard1)=10
    if dealercard1 == 'k':
        dealercard1 = (dealercard1)=10
    if dealercard1 == 'q':
        dealercard1 = (dealercard1)=10
    if dealercard1 == 'a':
        while dealerpoints + 11 <= 21:
            aced = (dealercard1)=11
            dealercard1 = dealercard1=0
            break
        while dealerpoints + 11 > 21:
            aced = (dealercard1)=1
            dealercard1 = dealercard1=0
            break
    
            
    dealerpoints = dealerpoints + dealercard1 + aced
    print("the dealer's current point total is " + str(dealerpoints))


def hitstandfunction():
    global bankroll
    hitstand = input('hit or stand?' )
    hitstandpossibleanswer = ['hit', 'stand']
    while hitstand not in hitstandpossibleanswer:
        print('please only enter "hit" or "stand" into the box...')
        hitstand = input('')

    while hitstand == 'hit':
        playerdrawcard()
        if playerpoints > 21:
            if dealerpoints <= 21:
                print('you went over 21 and have lost...')
                break
        if dealerpoints < 16:
            dealerdrawcard()
            if dealerpoints > 21:
                    if playerpoints <= 21:
                        print('dealer went over 21')
                        break
        else:
            print('the dealer chooses to stand at their {} point total'.format(dealerpoints))
            
        hitstand = input('hit or stand?')
    while hitstand == 'stand':
        print('you chose to stand at a total of {} points.'.format(playerpoints))
        if dealerpoints >= 16:
            break
        if dealerpoints < 16:
            if playerpoints <= 21:
                dealerdrawcard()
            if playerpoints > 21:
                break
            if dealerpoints >= 16:
                break
            
    if playerpoints <= 21:
            print('')
            if playerpoints > dealerpoints:
                if dealerpoints <= 21:
                    print('you win!')
                    bankroll = bankroll + wager
                
            if playerpoints < dealerpoints:
                if dealerpoints <= 21:
                    print('you lose')
                    bankroll = bankroll - wager
            if dealerpoints > 21:
                print('you win!')
                bankroll = bankroll + wager
                
    if playerpoints > 21:        
        if dealerpoints <= 21:
            print('you lose')
            bankroll = bankroll - wager
def hitstandfunction2():
    global bankroll
    hitstand2 = input('hit or stand your second hand?' )

    while hitstand2 == 'hit':
        playersplitdraw()
        if playerpoints2 > 21:
            if dealerpoints <= 21:
                print('you went over 21 and have lost this hand...')
                break
        if dealerpoints < 16:
            
            if dealerpoints > 21:
                    if playerpoints2 <= 21:
                        print('dealer went over 21')
                        break
        else:
            print('the dealer chooses to stand at their {} point total'.format(dealerpoints))
            
        hitstand2 = input('hit or stand?')
        if hitstand2 == 'stand':
            print('you chose to stand at a total of {} points.'.format(playerpoints))
        while dealerpoints < 16:
            if playerpoints2 > 21:
                break
            
            
    if playerpoints2 <= 21:
            print('')
            if playerpoints2 > dealerpoints:
                if dealerpoints <= 21:
                    print('you win!')
                    bankroll = bankroll + wager2
                
            if playerpoints2 < dealerpoints:
                if dealerpoints <= 21:
                    print('you lose')
                    bankroll = bankroll - wager2
            if dealerpoints > 21:
                print('you win!')
                bankroll = bankroll + wager2
                
    if playerpoints2 > 21:        
        if dealerpoints <= 21:
            print('you lose')
            bankroll = bankroll - wager2




while play == 'yes':

    playerdrawcard()
    playerdrawcard()
    for elem in player1list:
        if player1list.count(elem) > 1:
            print('you drew a pair, do you want to split?')
            split = input('yes or no?')
            if split == 'yes':
                player1list.remove(playercard1)
                playerpoints = playerpoints - playercard1
                wager2 = int(input('how much do you want to wager on your second hand?'))
                playerpoints2 = playerpoints
                playersplitdraw()
                playerdrawcard()
                
    
    dealerdrawcard()
    dealerdrawcard()
    hitstandfunction()
    if split == 'yes':
        hitstandfunction2()

    
    
            
    print('new bankroll is {}'.format(bankroll))
    play = input('play again?')
    if play == 'yes':
        print('how much do you want to wager?')
        wager = int(input(''))

        wager2 = 0
        playerpoints = 0
        playerpoints2 = 0
        dealerpoints = 0
        playercard1 = 0
        dealercard1 = 0
        acep = 0
        acep2 = 0
        aced = 0
        split = 'no'
        hitstand2 = ''

        
        player1list = []
        player2list = []
        dealerlist = []
        playerpointlist = []
        playerpointlist2 = []
        splitcheck = []

        cardlist = [2, 2, 2, 2, 3, 3, 3, 3, 4, 4, 4, 4, 5, 5, 5, 5, 6, 6, 6, 6, 7, 7, 7, 7, 8, 8, 8, 8, 9, 9, 9, 9, 10, 10, 10, 10, 10, 'j', 'j', 'j', 'j', 'q', 'q', 'q', 'q', 'k', 'k', 'k', 'k', 'a', 'a', 'a', 'a']
            
