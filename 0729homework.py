
#define the game function

def gm():
    import random
    sn=random.randint(1,101)
    count=0
    while True:
        guess=int(input('please pick a number between 1 and 100:  '))
        count+=1
        if guess>sn:
            print('it\'s too big.  guess again!')
        elif guess<sn:
            print('it\'s too small. guess again!')
        else:
            print('You get it right after %d guesses.  The scret number is %d.'%(count,guess))
            return count
            break


# main process

while True:
    player=input('please input your name: ')    
    playgm='y'
    gmnumber=0
    countdic={}
    ttlcount=0
    avecount=0
    while playgm=='y' or playgm=='Y':
        gmnumber+=1
        eachcount=gm()
        countdic[gmnumber]=eachcount
        mincount=min(countdic.values())
        ttlcount+=eachcount
        avecount=ttlcount/gmnumber
        print(f'{player}, you\'ve played the game {gmnumber} round(s).\
\nthe minimun is {mincount} guesses. On average, you tried {round(avecount,1)} guesses to get the answer.')
        playgm=input('Wanna play again? (please press "y" to continue or anything else to quit.)  ')
    print('End game. See you again!')


