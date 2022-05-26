// Link: https://codeforces.com/contest/405/problem/A

#include <iostream>
#include <algorithm>

using namespace std;

int main(int argc, char const *argv[])
{
    // Enter Size of array
    int size = 0;
    cin >> size;

    // Make array
    int array[size];

    // Get array values
    for(int i = 0; i < size; i++)
    {
        cin >> array[i];
    }

    // Sort array
    sort(array, array + size);

    // Print array
    for(int i = 0; i < size; i++)
    {
        cout << array[i] << " ";
    }
    return 0;
}
