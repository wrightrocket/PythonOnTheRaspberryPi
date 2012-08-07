#!/usr/bin/python
''' Simple game of rock, paper and scissors 

This version is an interactive text version.
User will provide input of r,p,c,l,s, or q.
Upon accepting input, program will randomly
choose rock, paper, scissor, lizard or spock and  
calculate the winner. Score will be kept 
for the player and the program. Upon quitting,
the winner of all rounds will be printed. 
'''

import random

class game(object):
    ''' A simple class for a rock, paper, scissor, lizard, spock 


    Special feature is ability to compare itself
    to other game objects for greater than, less than,
    or equal

    '''

    rules = '''
            Scissors cut paper
            Paper covers rock
            Rock crushes lizard
            Lizard poisons Spock
            Spock smashes scissors
            Scissors decapitate lizard
            Lizard eats paper
            Paper disproves Spock
            Spock vaporizes rock
            Rock crushes scissors'''
    gameTypes = ('r','p','c','l','s')
    gameNames = ('Rock','Paper','Scissors','Lizard','Spock')
    rMeets = ('l', 'c')
    rActions = ('crushes', 'crushes')
    rDict = dict(zip(rMeets, rActions))
    pMeets = ('r', 's')
    pActions = ('covers','disproves')
    pDict = dict(zip(pMeets, pActions))
    cMeets = ('p', 'l')
    cActions = ('cuts', 'decapitates')
    cDict = dict(zip(cMeets, cActions))
    lMeets = ('s','p')
    lActions = ('poisons', 'eats')
    lDict = dict(zip(lMeets, lActions))
    sMeets = ('c', 'r')
    sActions = ('smashes', 'vaporizes')
    sDict = dict(zip(sMeets, sActions))
    meetActions = (rDict, pDict, cDict, lDict, sDict)
    gameTypeDict = dict(zip(gameTypes, gameNames))
    gameActionDict = dict(zip(gameTypes, meetActions))
    
    def __init__(self, gameType):
        ''' requires a gametype to create object '''
        if gameType not in self.gameTypes:
            raise TypeError
        else:
            self.gameType = gameType

    def __cmp__(self, other):
        ''' if self loses return -1, if self wins return 1, otherwise return 0 if equal '''
        if self.gameType == other.gameType:
            return 0
        elif self.gameType == 'r':
            if other.gameType == 's':
                return -1
            elif other.gameType == 'p':
                return -1
            elif other.gameType == 'l':
                return 1
            elif other.gameType == 'c':
                return 1
        elif self.gameType == 'c':
            if other.gameType == 'r':
                return -1
            elif other.gameType == 'p':
                return 1
            elif other.gameType == 'l':
                return 1
            elif other.gameType == 's':
                return -1
        elif self.gameType == 'p':
            if other.gameType == 'r':
                return 1
            elif other.gameType == 's':
                return 1
            elif other.gameType == 'c':
                return -1
            elif other.gameType == 'l':
                return -1
        elif self.gameType == 's':
            if other.gameType == 'c':
                return 1
            elif other.gameType == 'l':
                return -1
            elif other.gameType == 'p':
                return -1
            elif other.gameType == 'r':
                return 1
        elif self.gameType == 'l':
            if other.gameType == 'c':
                return -1
            elif other.gameType == 'p':
                return 1
            elif other.gameType == 's':
                return 1
            elif other.gameType == 'r':
                return -1

    def __repr__(self):
        ''' define how an instance looks in the interpreter or repr() '''
        return self.gameType

    def __str__(self):
        ''' define how an instance looks from print or str() '''
        return self.gameTypeDict[self.gameType]

    def action(self, other):
        ''' uses the dictionary inside the dictionary 

        Method would have been more explicit like:
        typeDict = self.gameActionDict[self.gameType]
        return typeDict[other.gameType]
        '''
        return self.gameActionDict[self.gameType][other.gameType]

    def meets(self, other):
        ''' display results when self is compared to other '''
        if self == other:
            return 'You tie: %s meets %s' % (self, other)
        elif self > other:
            return 'You win: %s %s %s' % (self, self.action(other), other)
        else:
            return 'You lose %s %s %s' % (other, other.action(self), self)

def getProgramChoice():
    return random.choice(programChoices)
    
def getPlayerChoice():
    ''' Prompt user for input and return selection '''
    print
    print 'To play automatically enter a number, or to play yourself enter your own choice.'
    print 'Choices: r for rock, p for paper, c for scissor, l for lizard, s for spock, and q to quit\n'
    choice = raw_input('How many times to play automatically or your choice [#,r,p,c,l,s,q]? ')
    if choice in userChoices:
        return choice
    elif choice.isdigit():
        return choice
    else:
        return None

def welcome():
    ''' Initial greeting printed out by the program '''
    print 
    print 'Welcome to the game of Rock, Paper, Scissor, Lizard, Spock!'
    print 'All Hail Sam Kass! He is the inventor of the game.'
    print 'Visit http://www.samkass.com/theories/RPSSL.html to learn more.'
    print 
    print 'Here are the rules:'
    print game.rules


if __name__ == '__main__':
    playerScore = 0 # scores
    programScore = 0
    tieScore = 0
    programChoices = tuple(game.gameTypes)
    userChoices = programChoices + ('q',)
    weaponDict = {}
    allTimes = {}
    for weapon in programChoices:
        weaponDict[weapon] = 0
    for weapon in programChoices:
        allTimes[weapon] = weaponDict.copy()
    '''
    This kind of code is better because it is dynamic
    if the number of weapons changes, so does the dictionary
    weaponDict = { 'r':0, 'p':0, 'c':0, 'l':0, 's':0 }
    rTimes = weaponDict.copy()
    pTimes = weaponDict.copy()
    cTimes = weaponDict.copy()
    lTimes = weaponDict.copy()
    sTimes = weaponDict.copy()
    allTimes = {'r':rTimes, 'p':pTimes, 'c':cTimes, 'l':lTimes, 's':sTimes}
    '''
    userTimes = weaponDict.copy()
    programTimes = weaponDict.copy()
    random.seed()
    welcome()
    automatic = False
    automaticTimes = 0
    userChoice = getPlayerChoice()
    while True:
        if not userChoice:
            continue
        elif userChoice == 'q':
            break
        else:
            if userChoice.isdigit() or automatic:
                if userChoice.isdigit():
                    automaticTimes = int(userChoice)
                userChoice = getProgramChoice()
                automatic = True
            userTimes[userChoice] += 1
            userObject = game(userChoice)
            programChoice = getProgramChoice()
            programTimes[programChoice] += 1
            allTimes[userChoice][programChoice] +=1            
            programObject = game(programChoice)
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
            print 'After %s rounds the score is:' % (tieScore + playerScore + programScore)
            print 'Player: %2s\tProgram: %2s\tTies: %2s' % (playerScore, programScore, tieScore)
            print 'This is the current distribution of choices:'
            ''' Challenge: make the following "print" lines be dynamic to print the header, user, and program choices '''
            print '\t\tRock\tPaper\tScissor\tLizard\tSpock'
            print '%7s\t\t%2s\t%2s\t%2s\t%2s\t%2s' % ('Player', userTimes['r'], userTimes['p'],userTimes['c'],userTimes['l'],userTimes['s'])
            print '%7s\t\t%2s\t%2s\t%2s\t%2s\t%2s' % ('Program',programTimes['r'], programTimes['p'],programTimes['c'],programTimes['l'],programTimes['s'])
            print
            print 'This is how many times each weapon met another weapon:'
            ''' Challenge: make the following "print" lines use a dynamic loop to print all the items '''
            print 'Weapon:\t\tRock\tPaper\tScissor\tLizard\tSpock'
            print '%7s\t\t%2s\t%2s\t%2s\t%2s\t%2s' % ('Rock', allTimes['r']['r'], allTimes['r']['p'],allTimes['r']['c'],allTimes['r']['l'],allTimes['r']['s'])
            print '%7s\t\t%2s\t%2s\t%2s\t%2s\t%2s' % ('Paper',allTimes['p']['r'], allTimes['p']['p'],allTimes['p']['c'],allTimes['p']['l'],allTimes['p']['s'])
            print '%7s\t\t%2s\t%2s\t%2s\t%2s\t%2s' % ('Scissor', allTimes['c']['r'], allTimes['c']['p'],allTimes['c']['c'],allTimes['c']['l'],allTimes['c']['s'])
            print '%7s\t\t%2s\t%2s\t%2s\t%2s\t%2s' % ('Lizard',allTimes['l']['r'], allTimes['l']['p'],allTimes['l']['c'],allTimes['l']['l'],allTimes['l']['s'])
            print '%7s\t\t%2s\t%2s\t%2s\t%2s\t%2s' % ('Spock',allTimes['s']['r'], allTimes['s']['p'],allTimes['s']['c'],allTimes['s']['l'],allTimes['s']['s'])
            if automatic:
                automaticTimes -= 1
                if automaticTimes == 0:
                    automatic = False 
            if not automatic:
                userChoice = getPlayerChoice()
                       
    print
    print 'The final score after %s rounds was:' % (tieScore + playerScore + programScore)
    print 'Player: %2s\tProgram: %2s\tTies: %2s' % (playerScore, programScore, tieScore)
    if (playerScore > programScore):
        print 'You won overall!'
    elif (playerScore < programScore):
        print 'You lost overall.'
    else:
        print 'Overall it was a tie'
    print 'Thanks for playing Rock, Paper, Scissors, Lizard, Spock!'
         
