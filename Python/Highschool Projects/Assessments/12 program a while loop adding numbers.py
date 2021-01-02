# algorithm:
# get numbers
# add numbers if less then 6 numbers are entered
# print the sum of all 5 numbers


# creating a list to hold the numbers
nums = []
# the count number for enteries
c=0
b=0
# the while loop for enteries
while (c<5):
    # starting the check if it is a number
    parsed = False
    # another while loop for checking
    while not parsed:
        # the first part of checking
        try:
            # the entry needed for the users
            e = int(input("Enter a number: "))
            # if it is an integer, continue the normal loop
            parsed = True
            # unless it is not a number
        except ValueError:
            # tell the users it is not a number
            print ("Please make sure its a number.")
    # if he passes the number check, that number will be appended to the list
    nums.append(e)
    # then it will adding an entry to the counter
    c = c+1
    # then adding the numbers
    b = int(e)+b
# when the number of enteries reach 5
else:
    # printing the added numbers
    print("The sum of all numbers is " + str(b))
