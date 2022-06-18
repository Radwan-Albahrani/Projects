// Link: https://codeforces.com/contest/686/problem/A

#include <iostream>
#define fast ios::sync_with_stdio(0), cin.tie(0)
#define ll long long

using namespace std;

int main(int argc, char const *argv[])
{
    // Prepare variables needed
    ll numberOfOperations, IceCreamLeft, iceCreamNow;
    char operation;

    // Get number of operations and ice cream available
    cin >> numberOfOperations >> IceCreamLeft;

    // Set kids in distress to 0
    ll kidsInDistress = 0;

    // Loop over number of operations
    for(ll i = 0; i < numberOfOperations; i++)
    {
        // Get the current operation
        cin >> operation;

        // Get the amount of ice cream
        cin >> iceCreamNow;

        // If operation is subtraction
        if(operation == '-')
        {
            // If that subtraction would result in a negative number, kid goes home
            if((IceCreamLeft - iceCreamNow) < 0)
            {
                kidsInDistress++;
            }

            // Else, perform subtraction
            else
            {
                IceCreamLeft -= iceCreamNow;
            } 
        }

        // If addition, perform addition
        else
        {
            IceCreamLeft += iceCreamNow;
        }
    }

    // Print out ice cream left and kids in distress
    cout << IceCreamLeft << " " << kidsInDistress;
    return 0;
}
