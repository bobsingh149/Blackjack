import random
from art import logo


cards=[1,2,3,4,5,6,7,8,9,10,10,10,10]

def getrandomCard(curScore):
    
    idx=random.randint(0, len(cards)-1)
    
    card=cards[idx]
    
    if card==1 and curScore+11<=21:
        card=11
        
    return card
        
    
        
def check(score):
    
    return score<=21

def initPlayer(curScore):
    cards=[]
    
    cards.append(getrandomCard(curScore))
    curScore+=cards[0]
    cards.append(getrandomCard(curScore))
    curScore+=cards[1]
    
    return cards,curScore

def initComputer(curScore):
    cards=[]
    
    cards.append(getrandomCard(curScore))
    curScore+=cards[0]
    
    
    return cards,curScore
    


def whoWon(player,computer):
    
    if computer>21 or player>computer :
        print('You win 😃')
        
    else:
        print('Sorry You lose')
           
            
        
    
    
def showScores(myCards,myScore,computerCards,computerScore):
    
    print('Your hand:',end=' ')
    print(myCards,myScore)
    print("Computer's hand:",end=' ')
    print(computerCards,computerScore)
    

def game():
    
    
    
    while True:
        
        myScore=0
        computerScore=0
        myCards=[]
        computerCards=[]
        
        
        
        
        option=int(input('Do you want to play a game of Blackjack? Type 1 or 0: '))
        
        if option==0:
            break
        
        print(logo)
        
        myCards,myScore=initPlayer(myScore)
        computerCards,computerScore=initComputer(computerScore)
        
        showScores(myCards, myScore, computerCards, computerScore)
        
        while myScore<=21:
            
            ch=str(input("Type 'y' to get another card, type 'n' to pass: "))
            
            if ch=='n':
                
                while computerScore<17:
                    card=getrandomCard(computerScore)
                    computerCards.append(card)
                    computerScore+=card
                    
                    
                showScores(myCards, myScore, computerCards, computerScore)
                whoWon(myScore, computerScore)
                break
                
                
            else:
                card=getrandomCard(myScore)
                myCards.append(card)
                myScore+=card
                
                showScores(myCards, myScore, computerCards, computerScore)
                
                if myScore>21:
                    print('You lose')
                    break
        
        
        
        
        
    
game()        
        
        
        
        
        
        
        
    
    
    
    
