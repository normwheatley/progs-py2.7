a = 0
b = 1
while a < 10:
    print a
    a = a + b
print "continuing"
n = input("Number? ")
if n < 0:
    print "The absolute value of",n,"is",-n
else:
    print "The absolute value of",n,"is",n

#Asks for a number.
#Prints if it is even or odd
number = input("Tell me a number: ")
if number % 2 == 0:
    print number,"is even."
elif number % 2 == 1:
    print number,"is odd."
else:
    print number,"is very strange."
    
