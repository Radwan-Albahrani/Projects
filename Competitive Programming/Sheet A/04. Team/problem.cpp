// Link: https://codeforces.com/contest/231/problem/A

#include <iostream>

using namespace std;

int main(int argc, char const *argv[])
{
    // Get number of problems
    int numberOfProblems;
    cin >> numberOfProblems;

    // prepare an array of 3
    int array[3];

    // Prepare a sum and number of submissions
    int submissions = 0;

    // Loop through the number of questions times 3
    for(int i = 0; i < numberOfProblems; i++)
    {
        cin >> array[0] >> array[1] >> array[2];
        submissions += (array[0] + array[1] + array[2] >= 2);
    }

    // Print out number of submissions
    cout << submissions;
    return 0;
}
