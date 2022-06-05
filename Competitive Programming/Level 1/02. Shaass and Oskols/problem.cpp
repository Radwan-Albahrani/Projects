// Link: https://codeforces.com/contest/294/problem/A

#include <iostream>
#define fast ios::sync_with_stdio(0), cin.tie(0)
using namespace std;

int main(int argc, char const *argv[])
{
    // IO fast
    fast;

    // Get number of parallel lines
    int numberOfLines;
    cin >> numberOfLines;

    // Create array of birds
    int BirdsOnLines[numberOfLines];

    // Get number of birds per line
    for(int i = 0; i < numberOfLines; i++)
    {
        cin >> BirdsOnLines[i];
    }

    // Get number of shot
    int numberOfShots;
    cin >> numberOfShots;

    // For each shot
    for(int i = 0; i < numberOfShots; i++)
    {
        // Get selected line
        int line;
        cin >> line;
        line--;

        // Get the number of shot bird
        int shotBird;
        cin >> shotBird;

        // If line is the last line, birds move left and the rest fly away
        if(line == numberOfLines - 1)
        {
            BirdsOnLines[line - 1] += shotBird - 1;
            BirdsOnLines[line] = 0;
        }

        // If line is first line, birds move right and the rest fly away
        else if(line == 0)
        {
            BirdsOnLines[line + 1] += BirdsOnLines[line] - shotBird;
            BirdsOnLines[line] = 0;
        }

        // If line in the middle, some move left and some move right
        else
        {
            BirdsOnLines[line + 1] += BirdsOnLines[line] - shotBird;
            BirdsOnLines[line - 1] += shotBird - 1;
            BirdsOnLines[line] = 0;
        }
    }

    // Print out output
    for(int i = 0; i < numberOfLines; i++)
    {
        cout << BirdsOnLines[i] << endl;
    }
    return 0;
}
