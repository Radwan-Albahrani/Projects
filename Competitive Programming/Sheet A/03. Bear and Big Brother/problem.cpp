// Link: https://codeforces.com/contest/791/problem/A

#include <iostream>

using namespace std;

int main(int argc, char const *argv[])
{
    // declare limak and bob's weights
    int limak, bob;

    // Get both from standard input
    cin >> limak >> bob;

    // Start a year counter
    int counter = 0;

    // While limak's weight is less than bob's weight
    while(limak <= bob)
    {
        // Multiply limak by three and bob by 2, then add a year to the counter 
        limak *=3;
        bob *=2;
        counter++;
    }

    // Print the year counter
    cout << counter;
    return 0;
}
