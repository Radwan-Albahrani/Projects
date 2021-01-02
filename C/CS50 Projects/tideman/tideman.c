#include <cs50.h>
#include <stdio.h>
#include <string.h>

// Max number of candidates
#define MAX 9

// preferences[i][j] is number of voters who prefer i over j
int preferences[MAX][MAX];

// locked[i][j] means i is locked in over j
bool locked[MAX][MAX];

// Each pair has a winner, loser
typedef struct
{
    int winner;
    int loser;
    int mos;
}
pair;

// Array of candidates
string candidates[MAX];
pair pairs[MAX * (MAX - 1) / 2];

int pair_count;
int candidate_count;

// Function prototypes
bool vote(int rank, string name, int ranks[]);
void record_preferences(int ranks[]);
void add_pairs(void);
void sort_pairs(void);
void lock_pairs(void);
void print_winner(void);
bool checkLocked(int winner, int loser);

int main(int argc, string argv[])
{
    // Check for invalid usage
    if (argc < 2)
    {
        printf("Usage: tideman [candidate ...]\n");
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
        candidates[i] = argv[i + 1];
    }

    // Clear graph of locked in pairs
    for (int i = 0; i < candidate_count; i++)
    {
        for (int j = 0; j < candidate_count; j++)
        {
            locked[i][j] = false;
        }
    }

    pair_count = 0;
    int voter_count = get_int("Number of voters: ");

    // Query for votes
    for (int i = 0; i < voter_count; i++)
    {
        // ranks[i] is voter's ith preference
        int ranks[candidate_count];

        // Query for each rank
        for (int j = 0; j < candidate_count; j++)
        {
            string name = get_string("Rank %i: ", j + 1);

            if (!vote(j, name, ranks))
            {
                printf("Invalid vote.\n");
                return 3;
            }
        }

        record_preferences(ranks);

        printf("\n");
    }

    add_pairs();
    sort_pairs();
    lock_pairs();
    print_winner();
    return 0;
}

// Update ranks given a new vote
bool vote(int rank, string name, int ranks[])
{
    //Start a loop that will loop x times where x is candidate count.
    for (int i = 0; i < candidate_count; i++)
    {
        //compare the ith candidate with the given name in specified rank.
        int result = strcmp(candidates[i], name);

        //If candidate found, add candidate index to current rank.
        if (result == 0)
        {
            ranks[rank] = i;
            return true;
        }
        //else reloop till found.
    }

    //if not found, return false, end program.
    return false;
}

// Update preferences given one voter's ranks
void record_preferences(int ranks[])
{
    //After collecting ranked candidates in array ranks, update preferences based on who won against who.
    //First, loop through again x times where x is candidate count.
    for (int i = 0; i < candidate_count; i++)
    {
        //Save first rank. Since ranks array already sorted.
        int prevrank = ranks[i];

        //loop for the rest of ranks
        for (int j = 1; j < candidate_count - i; j++)
        {
            //get rank right after ith rank previously recorded. i is current rank. J will increase for every rank after i.
            int next_rank = ranks[i + j];

            //Use current rank and next rank to add a point to winner.
            preferences[prevrank][next_rank]++;
        }
    }
    //when done, return to end function.
    return;
}

// Record pairs of candidates where one is preferred over the other
void add_pairs(void)
{
    //grab a single row and start a loop for that row.
    for (int i = 0; i < candidate_count; i++)
    {
        //Start looking through all columns in that row.
        for (int j = 0; j < candidate_count; j++)
        {
            //Start assigning winners, losers, and margin of error based on rows and columns remembering that i is preferred over j
            if (preferences[i][j] > preferences[j][i])
            {
                //Assign winner as i, loser as j, and assign margin of success based on preference of i over j minus preference of j over i.
                pairs[pair_count].winner = i;
                pairs[pair_count].loser = j;
                pairs[pair_count].mos = (preferences[i][j] - preferences[j][i]);

                //Make sure to count how many pairs this has made.
                pair_count++;
            }
        }
    }
    return;
}

void sort_pairs(void)
{
    // Use a sorting algorithm
    // Iterate over pairs
    for (int i = 0; i < pair_count; i++)
    {
        // Iterate over next pairs
        for (int j = 1; j < pair_count - i; j++)
        {
            // If this pair's winner has less votes than the next one
            if (preferences[pairs[i].winner][pairs[i].loser] < preferences[pairs[j].winner][pairs[j].loser])
            {
                // Swap the pairs
                pair temp = pairs[i];
                pairs[i] = pairs[j];
                pairs[j] = temp;
            }
        }
    }
}

// Lock pairs into the candidate graph in order, without creating cycles
void lock_pairs(void)
{
    //loop through all pairs
    for (int i = 0; i < pair_count; i++)
    {
        //give current pair winner and current pair loser to recursive function to check for any connection.
        if (checkLocked(pairs[i].winner, pairs[i].loser) == false)
        {
            //if no connection. You can create an edge
            locked[pairs[i].winner][pairs[i].loser] = true;
        }
    }
    return;
}

// Print the winner of the election
void print_winner(void)
{
    // TODO
    //loop over candidates so you can loop over the locked table.
    for (int i = 0; i < candidate_count; i++)
    {
        //Have a counter to check all pairs
        int counter = 0;

        //loop again to check all other candidates against current candidate
        for (int j = 0; j < candidate_count; j++)
        {
            //if loser isn't connected to winner, add to counter
            if (locked[j][i] == false)
            {
                counter++;
            }
        }

        //if nobody has an edge over current candidate, candidate is source. print candidate.
        if (counter == candidate_count)
        {
            printf("%s\n", candidates[i]);
        }
    }
    return;
}

bool checkLocked(int winner, int loser)
{
    //Check if loser connects to winner.
    if (locked[loser][winner])
    {
        return true;
    }

    //if it doesn't. Check if loser connects to anything that connects to winner.
    for (int i = 0; i < pair_count; i++)
    {
        //If loser connects to any other candidate
        if (locked[loser][i])
        {
            //redo function with the same winner but the loser being the new loser.
            if (checkLocked(winner, i)) 
            {
                return true;
            }
        }
    }
    return false;

}