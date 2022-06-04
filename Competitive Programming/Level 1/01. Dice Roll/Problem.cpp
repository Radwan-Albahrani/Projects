// Link: https://codeforces.com/contest/9/problem/A

#include <iostream>
#include <algorithm>
#define fast ios::sync_with_stdio(0), cin.tie(0)
#define ll long long
using namespace std;

int main(int argc, char const *argv[])
{
    // Make input output faster
    fast;

    // Get Dice Rolls
    int rolls[2];
    for(int i = 0; i < 2; i++)
    {
        cin >> rolls[i];
    }

    // Get the highest amount
    int highest  = max(rolls[0], rolls[1]);

    // Get the numerator using probability
    int numerator = 6 - highest + 1;

    // Set the denominator to N
    int denominator = 6;

    // Reduce the fraction as much as possible
    for(int i = 2; i <= 3; i++)
    {
        if(numerator % i == 0 && denominator % i == 0)
        {
            numerator /= i;
            denominator /= i;
        }
    }

    // Print out the probability
    cout << numerator << "/" << denominator;
    return 0;
}
