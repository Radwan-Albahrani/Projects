# Imports
from cs50 import get_string


# Main function
def main():
    # Get name from user
    name = get_string("What is your name?\n")

    # Greet user
    print("Hello, " + name)


main()