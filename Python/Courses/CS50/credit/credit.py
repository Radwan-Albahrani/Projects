import re
from cs50 import get_int


# Main function
def main():
    # Declare Variables for Regular Expression checks
    visa = "^4"
    master = "^5[1-5]"
    american = "^3(4|7)"

    # Get Credit card number from user
    crednum = str(get_int("Number: "))

    # Check if credit card length within parameters
    if len(crednum) in [13, 15, 16]:

        # Get the final result of checksum
        finalcount = calculated(crednum)

        # If checksum succeeds, use Regular expressions to check
        if finalcount == 0:
            # If visa regex suceeds, print VISA
            if re.search(visa, crednum):
                print("VISA")

            # If master regex succeeds, print MASTERCARD
            elif re.search(master, crednum):
                print("MASTERCARD")

            # If american regex succeeds, print AMEX
            elif re.search(american, crednum):
                print("AMEX")

            # Else, card is invalid, in all cases.
            else:
                print("INVALID")
        else:
            print("Invalid")
    else:
        print("INVALID")


# Function for checksum calculations
def calculated(crednum):
    # make a temp variable storing credit number as a list
    temp = list(crednum)

    # Get the digits starting with the second to last digit, stepping by 2.
    credn = firstalt(temp)

    # Get the digits starting with the last digit, stepping by 2
    credn2 = secondalt(temp)

    # Start a total variable
    total = 0

    # Loop through credn which is a list starting with the second to last digit moving backwards with a step of 2
    for digit in credn:
        # Multiply the digit by 2 and save it to a variable
        j = int(digit)*2

        # if the new digit is not a single digit number
        if len(str(j)) > 1:
            # Split it and make it an integer list of digits
            j = [int(x) for x in str(j)]

            # sum up digits and add it to total.
            total += sum(j)

        # Else if it is a single digit, just add it to total
        else:
            total += j

    # As for the second list, just make it into an integer list
    credn2 = [int(x) for x in credn2]

    # Add the sum of digits to total
    total += sum(credn2)

    # Make sure it is divisible by 10
    total = total % 10

    # Return the result of the divisibility check
    return total


# Function to make a list starting with second to last digit with a step of 2
def firstalt(credit):
    return credit[-2::-2]


# Function to make a list starting with last digit with a step of 2.
def secondalt(credit):
    return credit[::-2]


main()