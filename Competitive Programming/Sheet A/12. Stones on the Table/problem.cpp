// Link: https://codeforces.com/contest/266/problem/A

#include <iostream>
#include <algorithm>
#define fast ios::sync_with_stdio(0), cin.tie(0)
#define ll long long
using namespace std;

int main(int argc, char const *argv[])
{
    // Fast
    fast;

    // Get number of stones
    int numberOfStones;
    cin >> numberOfStones;
    
    // Prepare number of removed stones
    int removed = 0;
    
    // Get Stones
    char CurrentStone, previousStone;

    // Loop through stones
    for(int i = 0; i < numberOfStones; i++)
    {   
        // Get stone
        cin >> CurrentStone;

        // If first loop, stone equal previous stone, continue
        if(i == 0)
        {
            previousStone = CurrentStone;
            continue;
        }

        // next loops
        else
        {   
            // If previous stone is the same color as the current stone
            if(previousStone == CurrentStone)
            {
                // Remove it
                removed++;
            }
        }
        previousStone = CurrentStone;
    }

    // Print number of stones removed
    cout << removed;
    return 0;
}
