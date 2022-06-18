// Link: https://codeforces.com/contest/709/problem/A

#include <iostream>
#define fast ios::sync_with_stdio(0), cin.tie(0)
#define ll long long

using namespace std;
int main(int argc, char const *argv[])
{
    // fast input output
    fast;

    // Get starter inputs
    ll numberOfOranges, maxOrangeSize, wasteCondition;
    cin >> numberOfOranges >> maxOrangeSize >> wasteCondition;

    // Prepare loop inputs
    ll currentOrange, totalOranges = 0, wasted = 0;

    // Loop for the amount of Oranges
    for(ll i = 0; i < numberOfOranges; i++)
    {
        // Get current orange
        cin >> currentOrange;

        // If orange is bigger than max orange size, ignore it
        if (currentOrange > maxOrangeSize)
        {
            continue;
        }

        // If orange size is not greater, add it to total oranges
        else
        {
            totalOranges += currentOrange;
        }

        // Check if time for waste
        if(totalOranges > wasteCondition)
        {
            wasted++;
            totalOranges = 0;
        }
    }

    // Ouput how many wasted oranges
    cout << wasted;
    return 0;
}
