#!/usr/bin/python
'''
This module just does some simple calculations to help determine sectors to
use when updating a Debian image for Raspberry Pi.

Use these calculations at your own risk! Beware that modifying partitions on 
a device may result in a loss of data.
'''
DEFAULT_SWAP_SIZE = 383
BYTES_PER_SECTOR = 512
MIBI_BYTE = 1048576

def makeRecommendation(lastSector, swapMiBiSize=DEFAULT_SWAP_SIZE):
    lastSector -= 1
    swapSectors = swapMiBiSize * MIBI_BYTE / BYTES_PER_SECTOR
    firstSwapSector = lastSector - swapSectors
    lastRootSector = firstSwapSector - 1
    print "\nYou should have made note of the starting sector for partition 2.\n"
    print "The ending sector for partition 2 is: %s\n" % lastRootSector
    print "The starting sector for partition 3 is %s\n" % firstSwapSector
    print "The ending sector for partition 3 is: %s\n" % lastSector
    
def calcCardSize(lastSector):
    cardSize = lastSector * BYTES_PER_SECTOR / MIBI_BYTE
    if cardSize < 2000:
        print "\nYour card appears to be %s MiB which is less than 2000MB" % cardSize
        print "Check the value you entered, as this size cannot be expanded\n" 
        return None
    else:
        print "\nYour card appears to be %s MiB in size\n" % cardSize
        return cardSize
    
def getLastSector():
    print "From the output of fdisk -l enter the ending sector of your SD card"
    lastCardSector = raw_input("Last sector: ")
    if lastCardSector.isdigit():
        lastCardSector = long(lastCardSector)
        if calcCardSize(lastCardSector):
            print "How many MiB for the swap partition, or Enter for default (%s): " % DEFAULT_SWAP_SIZE
            mibiSwap = raw_input("Swap size: ")
            if mibiSwap.isdigit():
                makeRecommendation(lastCardSector, long(mibiSwap))
            elif mibiSwap == '':
                makeRecommendation(lastCardSector)
            else:
                print "The swap size must be entered as a number without commas"
    else:
        print "The last sector must be entered as a number without commas"
        print "From the output of fdisk -l enter the ending sector of your SD card"
            

if __name__ == "__main__":
    print "This program will calculate the sector numbers to use when"
    print "expanding the default Debian image for the Raspberry Pi.\n"
    getLastSector()
            
            
        