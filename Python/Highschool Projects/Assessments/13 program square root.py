# importing math
import math
# The start of the loop that checks if the input is a number
parsed = False
# while loop for checking the input
while not parsed:
    # Checcking starts here
    try:
        # the entry needed from the users
        e = int(input("Enter a number: "))
        # if it is a number, continue to the square root
        parsed = True
        # unless it is not a number
    except ValueError:
        # tell the users it is not a number
        print ("Please make sure its a number.")
# Square root the number given
r = math.sqrt(e)
# Print the answer
print("The square root of your number is: " + str(r))
