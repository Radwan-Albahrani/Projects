// Link: https://codeforces.com/contest/71/problem/A

#include <iostream>
#define fast ios::sync_with_stdio(0), cin.tie(0)
#define ll long long
#include <string>
#include <cstring>
#include <sstream>

using namespace std;

int main(int argc, char const *argv[])
{
    // Make sure io is fast
    fast;

    // Start a variable for number of words and get it
    ll numberOfWords;
    cin >> numberOfWords;

    // Start an array of strings
    string words[numberOfWords];

    // A temp variable to hold each word
    string word;

    // Loop through number of words
    for(int i = 0; i < numberOfWords; i++)
    {
        // Get the word
        cin >> word;
        
        // If the word length is greater than 10
        if(word.length() > 10)
        {
            // Start a string buffer
            stringstream buffer;
            
            // Convert the word to its abbreviation
            buffer << word[0] << word.length() - 2 << word[word.length() - 1];

            // Put it in the array
            words[i] = buffer.str();

            // Empty the buffer
            buffer.str(std::string());
        }
        else
        {
            // Put the word as is
            words[i] = word;
        }
    }

    // Print out all abbreviated words
    for(int i = 0; i < numberOfWords; i++)
    {
        cout << words[i] << endl;
    }
    return 0;
}
