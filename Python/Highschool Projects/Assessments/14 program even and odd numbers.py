parsed = False
# while loop for checking
while not parsed:
    # the first part of checking
    try:
        # the entry needed for the users
        x = int(input("Enter a number: "))
        # if it is a number, continue to the check
        parsed = True
        # unless it is not a number
    except ValueError:
        # tell the users it is not a number
        print ("Please make sure its a number.")

# if the user passed the number test, check if the number is even
if int(x) % 2 == 0:
    # if even, tell the user
    print("Your number is even")
# if the number is not even
else:
    # tell the user
    print("your number is odd")
