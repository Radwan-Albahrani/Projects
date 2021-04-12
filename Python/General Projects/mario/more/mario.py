from cs50 import get_int


# Main Function
def main():
    # Get Input from user, make sure its within boundaries.
    while True:
        height = get_int("Height: ")
        if height >= 1 and height <= 8:
            break
    
    # Define row as a counter variable
    row = 1
    
    # While Row is not equal to height + 1, print out the two stairways in one print funciton.
    while row != (height + 1):
        print((" " * (height - row)) + ("#" * row) + "  " + ("#" * row))
        row += 1


# Call main
main()