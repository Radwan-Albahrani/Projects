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
    int sum = 0;
    int submissions = 0;

    // Loop through the number of questions times 3
    for(int i = 0; i <= numberOfProblems * 3; i++)
    {
        // If i is bigger than 3 and the remainder of dividing by 3 is zero
        if(i >= 3 && i % 3 == 0)
        {
            // Add the values inside the array
            sum += array[0] + array[1] + array[2];

            // Two or more, accept the submission and reset the sum
            if(sum >=2)
            {
                submissions++;
            }

            // If not the end of the loop, get the next value
            if(i != numberOfProblems * 3)
            {
               cin >> array[i%3]; 
            }
            sum = 0;
        }

        // Else, get the next value
        else
        {
            cin >> array[i%3];
        }
    }

    // Print out number of submissions
    cout << submissions;
    return 0;
}
