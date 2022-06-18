// Link:  https://codeforces.com/contest/443/problem/A

#include <iostream>
#define fast ios::sync_with_stdio(0), cin.tie(0)
#define ll long long
#include <string>
#include <cstring>

using namespace std;

int main(int argc, char const *argv[])
{
    // String to hold line
    string line;

    // String containing found letters
    string found;

    // Get the line
    getline(cin, line);

    // Loop through the line
    for(int i = 0; i < line.length(); i++)
    {
        // If the letter was never found and its a an alphabetic letter
        if(found.find(line[i]) == string::npos && isalpha(line[i]))
        {
            // Add it to found
            found += line[i];
        }
    }

    // Print the length of found
    cout << found.length();
    return 0;
}
