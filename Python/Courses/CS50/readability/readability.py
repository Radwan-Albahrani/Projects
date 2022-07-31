from cs50 import get_string

# Defining Variables.
letters = 0
words = 0
sentences = 0


# Main Function
def main():
    # Get Global Variables
    global letters, words, sentences

    # Get a sentence from the user
    sentence = get_string("Text: ")

    # Call the count function.
    count(sentence)
    print(f"{letters} {words} {sentences}")
    # Calculate L and S for the formula if text was inputted.
    try:
        L = letters / words * 100
        S = sentences / words * 100
    except ZeroDivisionError:
        print("No text found.")
        exit()

    # Calculate index
    index = 0.0588 * L - 0.296 * S - 15.8

    # If index is less than 1, print that its before grade 1
    if index < 1:
        print("Before Grade 1")

    # If index between 1 and 16, print corresponding grade as an integer.
    elif index <= 16:
        print(f"Grade {round(index)}")

    # If grade is 16+, print that its 16+
    elif index > 16:
        print("Grade 16+")


# Define the count function
def count(sentence):
    # Get global variables
    global letters, words, sentences

    # Make variable to check for next word. Starts as true.
    isnextword = True

    # Temp variable to store current character.
    punct = None

    # loop through sentence.
    for i in sentence:
        # if its a space, set next word to true, continue loop.
        if i.isspace():
            isnextword = True

        else:
            # If its next word, make it not next word and add to word count.
            if isnextword:
                isnextsentence = False
                isnextword = False
                words += 1

            # If its a letter, add to letters
            if i.isalnum():
                letters += 1

            # if its a punctuation, add to sentences.
            if i in [".", "!", "?"]:
                # If previous punctuation character isnt the same as current character, add to sentences and change previous to current.
                if i != punct:
                    punct = i
                    sentences += 1
        punct = i


# Calling Main
if __name__ =="__main__":
    main()