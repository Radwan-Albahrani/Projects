// Link: https://codeforces.com/contest/59/problem/A

#include <iostream>
#include <string>
#include <cstring>

using namespace std;

int main(int argc, char const *argv[])
{
    string word;
    cin >> word;

    int upper = 0, lower = 0;
    for(int i = 0; i < word.length(); i++)
    {   
        if(isupper(word[i]))
        {
            upper++;
        }
        else if(islower(word[i]))
        {
            lower++;
        }
        word[i] = tolower(word[i]);
    }

    if(upper > lower)
    {
        for(int i = 0; i < word.length(); i++)
        {
            word[i] = toupper(word[i]);
        }
    }

    cout << word;
    return 0;
}
