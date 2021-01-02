#include <cs50.h>
#include <stdio.h>
#include <string.h>

// Max number of candidates
#define MAX 9

// Candidates have name and vote count
typedef struct
{
    string name;
    int votes;
}
candidate;

// Array of candidates
candidate candidates[MAX];

// Number of candidates
int candidate_count;

// Function prototypes
bool vote(string name);
void print_winner(void);

int main(int argc, string argv[])
{
    // Check for invalid usage
    if (argc < 2)
    {
        printf("Usage: plurality [candidate ...]\n");
        return 1;
    }

    // Populate array of candidates
    candidate_count = argc - 1;
    if (candidate_count > MAX)
    {
        printf("Maximum number of candidates is %i\n", MAX);
        return 2;
    }
    for (int i = 0; i < candidate_count; i++)
    {
        candidates[i].name = argv[i + 1];
        candidates[i].votes = 0;
    }

    int voter_count = get_int("Number of voters: ");

    // Loop over all voters
    for (int i = 0; i < voter_count; i++)
    {
        string name = get_string("Vote: ");

        // Check for invalid vote
        if (!vote(name))
        {
            printf("Invalid vote.\n");
        }
    }

    // Display winner of election
    print_winner();
}

// Update vote totals given a new vote
bool vote(string name)
{
    //Checking if name is in candidates.
    for (int i = 0; i < candidate_count; i++)
    {
        //comparing the vote with the candidates in array
        int result = strcmp(candidates[i].name, name);

        //if vote found, add a vote to that candidate then return true to end loop.
        if (result == 0)
        {
            candidates[i].votes++;
            return true;
        }

    }

    //if loop is done and no candidates have been found, return false.
    return false;
}

// Print the winner (or winners) of the election
void print_winner(void)
{
    //Prepare highest vote variable
    int highest_vote = 0;
    
    //Prepare array of winners
    string winners[candidate_count];
    
    //Start loop to check winners.
    for (int i = 0, f = 0; i < candidate_count; i++)
    {
        //If candidate has a vote higher than highest vote so far
        if (candidates[i].votes > highest_vote)
        {
            
            //Reset winner array
            for (int k = 0; k < candidate_count; k++)
            {
                winners[k] = 0;
            }
            
            //reset case of multiple winners index
            f = 0;
            
            //Change highest vote to current highest vote
            highest_vote = candidates[i].votes;
            
            //Add winner to winners array
            winners[f] = candidates[i].name;
        }
        
        //In case of a tie
        else if (candidates[i].votes == highest_vote)
        {
            //Increase winner index
            f++;
            
            //Add new winner to winners array
            winners[f] = candidates[i].name;
        }
    }
    
    //Start printing winners.
    for (int i = 0; i < candidate_count; i++)
    {
        if (winners[i] != 0)
        {
            printf("%s\n", winners[i]);
        }
    }
    return;
}

