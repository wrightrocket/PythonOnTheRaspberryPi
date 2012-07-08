#!/usr/bin/python
''' Simple game of rock, paper and scissors 

This version is like the interactive text version
except is uses instances of a class called rps 
to encapsulate the information about 
Rock, Paper, Scissors like the types,
names, and actions. 

It uses a dictionary object to map the types of
rps objects to their names, and the action they
perform when they win.

User will provide input of r,p,s, or q.
Upon accepting input, program will randomly
choose rock, paper, or scissor, and then 
calculate the winner. Score will be kept 
for the player and the program. Upon quitting,
the winner of all rounds will be printed. 
'''

class rps(object):
    ''' A simple class for a rock, paper, or scissor 


    Special feature is ability to compare itself
    to other rps objects for greater than, less than,
    or equal
    '''
    rpsTypes = ('r','p','s')
    rpsNames = ('Rock','Paper','Scissors')
    rpsActions = ('breaks', 'covers', 'cuts')
    rpsTypeDict = dict(zip(rpsTypes, rpsNames))
    rpsActionDict = dict(zip(rpsTypes, rpsActions))
    
    def __init__(self, rpsType):
        ''' requires a rpstype to create object '''
        if rpsType not in self.rpsTypes:
            raise TypeError
        else:
            self.rpsType = rpsType

    def __cmp__(self, other):
        ''' if self loses return -1, if self wins return 1, otherwise return 0 if equal '''
        if self.rpsType == other.rpsType:
            return 0
        elif self.rpsType == 'r':
            if other.rpsType == 's':
                return 1
            elif other.rpsType == 'p':
                return -1
        elif self.rpsType == 's':
            if other.rpsType == 'r':
                return -1
            elif other.rpsType == 'p':
                return 1
        elif self.rpsType == 'p':
            if other.rpsType == 'r':
                return 1
            elif other.rpsType == 's':
                return -1

    def __repr__(self):
        return self.rpsType

    def __str__(self):
        return self.rpsTypeDict[self.rpsType]

    def action(self):
        return self.rpsActionDict[self.rpsType]

    def meets(self, other):
        if self == other:
            return 'You tie: %s meets %s' % (self, other)
        elif self > other:
            return 'You win: %s %s %s' % (self, self.action(), other)
        else:
            return 'You lose %s %s %s' % (other, other.action(), self)


import random

      
def getProgramChoice():
    return random.choice(programChoices)
    
def getPlayerChoice():
    ''' Prompt user for input and return selection '''
    print 'What is your choice [r,p,s,q]?\n'
    choice = raw_input().lower()
    if choice in userChoices:
        return choice
    else:
        return None

def welcome():
    ''' Initial greeting printed out by the program '''
    print 
    print 'Welcome to the game of rock, paper, scissors!'
    print 'First, you will be asked to make your choice'
    print 'by typing r for rock, p for paper, s for scissors'
    print 'or q to quit. Then, the program will make a '
    print 'random choice, and determine the winner.'
    print 

if __name__ == '__main__':
    playerScore = 0 # scores
    programScore = 0
    tieScore = 0
    programChoices = tuple(rps.rpsTypes)
    userChoices = programChoices + ('q',)
    random.seed()
    welcome()
    while True:
        userChoice = getPlayerChoice()
        if not userChoice:
            continue
        elif userChoice == 'q':
            break
        else:
            userObject = rps(userChoice)
            programChoice = getProgramChoice()
            programObject = rps(programChoice)
            result = userObject.meets(programObject)
            print
            print 'You chose %s' % (userObject)
            print 'The program chose %s' % (programObject)
            print result
            print 
            if userObject > programObject:
                playerScore += 1
            elif userObject < programObject:
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
