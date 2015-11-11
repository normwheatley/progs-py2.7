# Program by Mitchell Aikens 2012
# No copyright.
import math
 
def main():
    try:
        epact()
    except ValueError:
        print "Error. Please enter an integer value."
        year = 0
        epact()
    except NameError:
        print "Error. Please enter an integer value."
        year = 0
        epact()
    except SyntaxError:
        print "Error. Please enter an integer value."
        year = 0
        epact()
    finally:
        print "Program Complete"
 
def epact():
 
    year = int(input("What year is it?\n"))
    C = year/100
    epactval = (8 + (C/4) - C + ((8*C + 13)/25) + 11 * (year%19))%30
    print "The Epact is: ",epactval
 
main()
