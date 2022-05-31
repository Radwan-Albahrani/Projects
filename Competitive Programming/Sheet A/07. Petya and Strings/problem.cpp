// Link: https://codeforces.com/contest/112/problem/A

#include <iostream>
#include <string>
#include <cstring>
using namespace std;

int main(int argc, char const *argv[])
{
    // Get the first word and the second word
    string first;
    string second;
    cin >> first;
    cin >> second;

    // Compare them regardless of case
    int result = strcasecmp(first.c_str(), second.c_str());

    // Convert result to either -1, 0, or 1
    if(result < -1)
    {
        result = -1;
    }
    else if(result >= 1)
    {
        result = 1;
    }
    else
    {
        result = 0;
    }
    
    // Print out the result
    cout << result;
}
