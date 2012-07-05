#!/usr/bin/env python
''' Module provides a simple function to test whether a year is a leap year'''

def isLeapYear(year):
    ''' Returns True if a year is a leap year, otherwise False 

    This function first checks the passed value of year to ensure to that is an Integer.
    It then tests the year to see if it is a Leap Year according to the algorithm 
    expressed in the pseudo-code found at http://en.wikipedia.org/wiki/Leap_year'''

    if type(year) is not int:  #  verifying year is an int (Integer) object
        # if year is not an Integer then return False
        # print year, "is a not an Integer, so unable to check if it a leap year"
        return False
    else:  # This is where the pseudo-code of the function begins
        if not (year % 400):  
            # zero is considered False
            return True 
            #  if year / 400.0 has zero remainder then is a leap year
        elif not (year % 100):
            return False  
            # if year / 100.0 has zero remainder than is not leap year
        elif not (year % 4):
            return True  
            # if year / 4 has zero remainder and both above are not true
        else:
            return False  # otherwise it is not a leap year

def test_isLeapYear():
    ''' Display the full range of leap years from 1752 to 2012 '''
    print "\nPrinting the the list of all leap years up to 2012:"
    years = 0
    for year in range(1752, 2013):
        # start the year at 1752, when they began and go to 2013 - 1
        if isLeapYear(year):
            print year, 
            # don't add a new line by using trailing comma
            years += 1
            # add one to the years variable
            if not (years % 10):
                # every 10 leap years print a new line
                print 
        else:
            pass
            # do nothing instead of printing years that are not leap years
            # print "%s IS NOT a leap year" % year
    else:
        # when through with the loop finish the line of print
        print


def test_logic_isLeapYear():
    ''' This function tests every branch of isLeapYear() to verify logic 

    If this function raises an AssertionError then the logic of isLeapYear() 
    is not working correctly according to pseudo-code for calculating 
    Leap Years found at http://en.wikipedia.org/wiki/Leap_year'''

    print "\nTesting each branch of isLeapYear for accurate results:"
    print "Is the year 2000 a leap year? Why, or why not?", isLeapYear(2000)
    # 2000 modulus 400 is 0, so it is a leap year
    assert isLeapYear(2000)
    # if isLeapYear returns False, then this assertion will halt execution
    print "Is the year 1800 a year year? Why, or why not?", isLeapYear(1800)
    # 1800 modulus 400 != 0, and 1800 % 100 == 0, so it is not a leap year
    assert not isLeapYear(1800)
    # if isLeapYear returns True, then this assertion will halt execution
    print "Is the year 2012 a leap year? Why, or why not?", isLeapYear(2012)
    # 2012 % 400 != 0, 2012 % 100 != 0, but 2012 % 4 == 0, so it is a leap year
    assert isLeapYear(2012)
    # if isLeapYear returns False, then this assertion will halt execution
    print "Is the year 2013 a leap year? Why, or why not?", isLeapYear(2013)
    # 2013 % 400 != 0, 2013 % 100 != 0, and 2013 % 4 != 0, so not a leap year
    assert not isLeapYear(2013)
    # if isLeapYear returns True, then this assertion will halt execution

if __name__ == '__main__':
    # when run directly, and not being imported execute the following block of code
    test_isLeapYear()
    test_logic_isLeapYear()
