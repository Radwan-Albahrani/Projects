# Plurality

This is a presidential candidate voting program using a single person voting ballad method. Meaning, each person gets to vote for one person.

## Usage

```C
$ ./plurality //Candidates
Number of voters: // Number of voters
Vote: //Enter your vote
```

## Logic

The logic is quite simple in this one. Basically, You will decide on the number of candidates and their names at the start of the program, then you will declare how many voters get to vote.

Each candidate will be put into a special type as follows:

```C
typedef struct
{
    string name;
    int votes;
}
candidate;
```

Where it will link the voter's name and the number of votes they have.

After each vote, you will compare the voter's input to all candidates. If the candidate is in the list of candidates, add a vote to them.

At the end, find out who has the highest votes. In case of a tie, print out both winners.
