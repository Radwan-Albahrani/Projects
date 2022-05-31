// Link: https://codeforces.com/contest/344/problem/A

#include <iostream>
#define fast ios::sync_with_stdio(0), cin.tie(0)
#define ll long long
using namespace std;
int main(int argc, char const *argv[])
{
    // Make input and output Faster
    fast;

    // Prepare important variables
    int numberOfMagnets;
    int previousMag = 0;
    int currentMag;
    int groups = 1;

    // Get the number of magnets
    cin >> numberOfMagnets;

    // Loop based on the number of magnets
    for(ll i = 0; i < numberOfMagnets; i++)
    {
        // Get the magnet
        cin >> currentMag;

        // After the first turn, if the previous magnet is not the same as the current one, add a new group
        if(i > 0 && currentMag != previousMag)
        {
            groups++;
        }

        // Make previous = to current
        previousMag = currentMag;
    }

    // After loop, print out group
    cout << groups;
}
