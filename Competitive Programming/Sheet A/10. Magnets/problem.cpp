// Link: https://codeforces.com/contest/344/problem/A

#include <iostream>
#define fast ios::sync_with_stdio(0), cin.tie(0)
#define ll long long
using namespace std;
int main(int argc, char const *argv[])
{
    fast;
    int numberOfMagnets;
    int previousMag = 0;
    int currentMag;
    int groups = 1;

    cin >> numberOfMagnets;

    for(ll i = 0; i < numberOfMagnets; i++)
    {
        cin >> currentMag;
        if(i > 0 && currentMag != previousMag)
        {
            groups++;
        }
        previousMag = currentMag;
    }

    cout << groups;
}
