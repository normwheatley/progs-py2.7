print "Type Control C or -1 to exit"
number = 1
while number != -1:
    try:
        number = int(raw_input("Enter a number: "))
        print "You entered:", number
    except ValueError:
        print "That was not a number."
