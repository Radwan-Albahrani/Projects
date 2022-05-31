// Link: https://codeforces.com/contest/59/problem/A

#include <iostream>
#include <string>
#include <cstring>

using namespace std;

int main(int argc, char const *argv[])
{
    // Get a word from the user
    string word;
    cin >> word;

    // Prepare counters for lowercase letters and uppercase letters
    int upper = 0, lower = 0;

    // Use a loop to count them
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

        // Always convert to lower by default
        word[i] = tolower(word[i]);
    }

    // If more uppercase than lowercase, convert to upper 
    if(upper > lower)
    {
        for(int i = 0; i < word.length(); i++)
        {
            word[i] = toupper(word[i]);
        }
    }

    // Print the word
    cout << word;
    return 0;
}
