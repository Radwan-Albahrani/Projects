// Link: https://codeforces.com/contest/427/problem/A

#include <iostream>
#include <algorithm>
#define fast ios::sync_with_stdio(0), cin.tie(0)
#define ll long long
using namespace std;


int main(int argc, char const *argv[])
{
    fast;

    // Get number of events
    ll events;
    cin >> events;

    // Number of police
    ll police = 0;
    
    // Untreated crime
    ll untreated = 0;

    // Current event
    ll currentEvent;

    // Loop through events
    for(ll i = 0; i < events; i++)
    {   
        // Get current event
        cin >> currentEvent;

        // Add it to number of police
        police += currentEvent;

        // If no police available, mark it as untreated
        if(police < 0)
        {
            untreated++;
            police = 0;
        }
    }

    cout << untreated;
    return 0;
}
