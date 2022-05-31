// Link: http://codeforces.com/contest/236/problem/A

#include <iostream>
#include <string>

using namespace std;

int main(int argc, char const *argv[])
{
    // prepare variables
    string username;
    string resultant;

    // Get the username
    cin >> username;

    // Loop through the username and remove any repeated characters. Add unique characters to resultant
    for(int i = 0; i < username.length(); i++)
    {
        size_t found = resultant.find(username[i]);
        if(found != string::npos)
        {
            continue;
        }
        else
        {
            resultant += username[i];
        }
    }

    // Get the length and if its even its a girl if its odd its a boy
    string result = (resultant.length() % 2) == 0 ? "CHAT WITH HER!" : "IGNORE HIM!";
    cout << result;
    return 0;
}
