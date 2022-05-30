// Link: https://codeforces.com/contest/677/problem/A

#include <iostream>

using namespace std;

int main(int argc, char const *argv[])
{
    // Get people and height
    int people, height;
    cin >> people;
    cin >> height;

    // Start an array of people
    int input[people];

    // Start a sum
    int sum = 0;

    // Get all the people and test them against height
    for(int i = 0; i < people; i++)
    {
        cin >> input[i];

        // If less then height, add one
        if(input[i] <= height)
        {
            sum++;
        }

        // Else, add 2
        else
        {
            sum += 2;
        }
    }

    // Print out the sum
    cout << sum;


    return 0;
}
