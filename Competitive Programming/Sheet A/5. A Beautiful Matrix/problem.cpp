// link: https://codeforces.com/contest/263/problem/A

#include <iostream>
using namespace std;

int main(int argc, char const *argv[])
{
    // Rows and Columns
    int row = 0, column = 0;

    // Array
    int array[5];

    // Loop through and gather the matrix
    for(int i = 0; i < 5 * 5; i++)
    {
        cin >> array[i % 5];

        // If the one is found, get the row and column of the 1
        if(array[i % 5] == 1)
        {
            column = i % 5;
            row = i / 5;
        }
    }

    // Get the number of moves
    int counter = abs(row - 2) + abs(column - 2);
    
    // Print out that number
    cout << counter;
    return 0;
}
