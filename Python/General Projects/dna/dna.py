# Imports
import csv
import sys
import re


# Main Function
def main():
    # Check for arguments. If invalid, Exit
    if len(sys.argv) < 3:
        print("Usage: Python dna.py data.csv sequence.txt")
        exit()

    # Load in required data. Database, STRs, and the sequence.
    database, STR, sequence = load(sys.argv[1], sys.argv[2])

    # Start counting STRs in the given sequence
    seq = count(sequence, STR)

    # Check if sequence has a match, and give match's index
    index = check(database, seq)

    # If index is -2, it means no match found. So if it isnt, print the match.
    if index != -1:
        print(database[index][0])
    else:
        print("No Match")


# Load Function
def load(file, sequence):
    # Start a database list to load in data
    database = []

    # Open file as csvfile
    with open(file) as csvfile:
        # Start a normal reader object
        reader = csv.reader(csvfile)

        # Get first line
        STR = next(reader)

        # Pop first item "name"
        STR.pop(0)

        # For each row in csvfile, append it to the list.
        for row in reader:
            database.append(row)

    # Open sequence
    with open(sequence) as givenseq:
        # Read sequence and split lines if necessary
        seq = givenseq.read()

    # return database, list of str, and the sequence.
    return database, STR, seq


# Sequence STR counting function
def count(seq, STR):
    # Start a count list
    count = []

    # Loop a number of times equal to how many STRs we intend to count.
    for i in range(len(STR)):
        # Initialize Maximum Variable
        maximum = 0
        k = 0
        # Loop through sequence.
        while k < len(seq):
            # Make current count equal to 1.
            curr = 1

            # Get current STR we are looking for.
            current = STR[i]

            # Get its length.
            n = len(current)

            # If the current character matches the first letter of the current STR
            if seq[k] == current[0]:
                # Check if current set of DNA letters is the STR
                if seq[k:k+n] == current:

                    # IF it is, Loop through it if the next set of letters is the same as the STR
                    while seq[k:k+n] == seq[k+n:k+n+n]:
                        # Add to current.
                        curr += 1

                        # Move position by the length of the current STR
                        k = k + n

                    # If current consecutive set is more than the Maximum, make it the maximum.
                    if curr > maximum:
                        maximum = curr
            # At end of loop, Append Maximum and start the next loop for the next STR.
            if k == len(seq) - 1:
                count.append(maximum)
            k += 1
    # Return counted STR values.
    return count


# Check Function
def check(data, seq):
    # Start with a match index of -1 to indicate no matches found yet.
    match_index = -1

    # Start match as 0 for checking process
    match = 0

    # Loop through data by rows
    for i in range(len(data)):
        # If match was complete and all of the STRs have been validated return match index and break loop.
        if match == len(seq):
            match_index = i - 1
            break

        # IF no complete match was found, reset match variable.
        match = 0

        # Loop through sequence
        for k in range(len(seq)):
            # Check if current STR count matches the corresponding STR count in database. If it does, increase Match counter.
            if data[i][k+1] == str(seq[k]):
                match += 1

            # If match was interupted, break loop
            else:
                break
    # When done, return Match index
    return match_index


main()