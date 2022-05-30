// Link: https://codeforces.com/contest/112/problem/A

#include <iostream>
#include <string>
#include <cstring>
using namespace std;

int main(int argc, char const *argv[])
{
    string first;
    string second;
    cin >> first;
    cin >> second;

    int result = strcasecmp(first.c_str(), second.c_str());

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

    cout << result;
}
