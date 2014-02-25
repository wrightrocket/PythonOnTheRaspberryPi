#!/usr/bin/python
''' Simple game of rock, paper and scissors 

This version is an interactive text version.
User will provide input of r,p,s, or q.
Upon accepting input, program will randomly
choose rock, paper, or scissor, and then 
calculate the winner. Score will be kept 
for the player and the program. Upon quitting,
the winner of all rounds will be printed. 
'''
import random

playerScore = 0 # scores
programScore = 0
tieScore = 0
gameD = {'r':'Rock', 'p':'Paper', 's':'Scissors'}
programChoices = tuple(gameD.keys())
userChoices = tuple(programChoices + ('q',))
''' Teaser: (list comprehension) programChoices = tuple([ x for x in userChoices if x != 'q']) '''

def didPlayerWin(player, program):
    ''' determine if player beats program '''
    if player == 'r':
        if program == 'r':
            return 'tie: rock meets rock'
        elif program == 's':
            return 'win: rock crushes scissors'
        else:
            return 'lose: paper covers rock'
    elif player == 's':
        if program == 'r':
            return 'lose: rock crushes scissors'
        elif program == 's':
            return 'tie: scissors meets scissors'
        else:
            return 'win: scissors cut paper'
    elif player == 'p':
        if program == 'r':
            return 'win: paper covers rock'
        elif program == 's':
            return 'lose: scissors cut paper'
        else:
            return 'tie: paper meets paper'
    else:
        ''' catch all for testing '''
        return 'error: for unknown reason'
      
def getProgramChoice():
    return random.choice(programChoices)
    
def getPlayerChoice():
    ''' Prompt user for input and return selection '''
    print 'What is your choice [r,p,s,q]?\n'
    choice = raw_input()
    if choice in userChoices:
        return choice
    else:
        return None

def welcome():
    ''' Initial greeting printed out by the program
    
    The one triple quoted string below replaced five print statements!
    This function doesn't explicitly return anything, so it is just a subroutine
    and will return None'''
    
    print '''Welcome to the game of rock, paper, scissors!
    First, you will be asked to make your choice
    by typing r for rock, p for paper, s for scissors
    or q to quit. Then, the program will make a 
    random choice, and determine the winner.
    
    '''

if __name__ == '__main__':
    random.seed()
    welcome()
    while True:
        userChoice = getPlayerChoice()
        if not userChoice:
            continue
        elif userChoice == 'q':
            break
        else:
            programChoice = getProgramChoice()
            result = didPlayerWin(userChoice, programChoice)
            print
            print 'You chose %s' % (gameD[userChoice])
            print 'The program chose %s' % (gameD[programChoice])
            print 'You %s' % (result)
            print 
            if result.startswith('win'):
                playerScore += 1
            elif result.startswith('lose'):
                programScore += 1
            else:
                tieScore += 1
    print
    print 'The final score after %s rounds was:' % (tieScore + playerScore + programScore)
    print 'Player: %2s Program: %2s Ties: %2s' % (playerScore, programScore, tieScore)
    if (playerScore > programScore):
        print 'You won overall!'
    elif (playerScore < programScore):
        print 'You lost overall.'
    else:
        print 'Overall it was a tie'
