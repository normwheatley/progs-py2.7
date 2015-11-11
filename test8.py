def main():
    try:
        number = int(input("Please enter a number.\n"))
        half = number/2
        print "Half of the number you entered is ",half
    except NameError:
        print "Error."
    except ValueError:
        print "Error."
    except SyntaxError:
        print "Error."
    finally:
        print "I am executing the finally clause."
 
main()
