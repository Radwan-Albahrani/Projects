// Link: https://codeforces.com/contest/734/problem/A

#include <iostream>

using namespace std;

int main(int argc, char const *argv[])
{
    // Get number of games
    int numberOfGames;
    cin >> numberOfGames;

    // Array of winners
    char winners[numberOfGames];

    // Variables for winner counts
    int anton = 0;
    int danik = 0;

    // Loop through and get the winners
    for(int i = 0; i < numberOfGames; i++)
    {
        cin >> winners[i];

        // Winner is Anton, add to anton wins
        if(winners[i] == 'A')
        {
            anton++;
        }

        // Winner is danik. Add to Danik wins.
        else if(winners[i] == 'D')
        {
            danik++;
        }
    }

    // Print out winner
    if(anton > danik)
    {
        cout << "Anton";
    }
    else if(danik > anton)
    {
        cout << "Danik";
    }
    else
    {
        cout << "Friendship";
    }
    return 0;
}
