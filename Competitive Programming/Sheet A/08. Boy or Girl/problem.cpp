// Link: http://codeforces.com/contest/236/problem/A

#include <iostream>
#include <string>

using namespace std;

int main(int argc, char const *argv[])
{
    string username;
    string resultant;
    cin >> username;

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

    string result = (resultant.length() % 2) == 0 ? "CHAT WITH HER!" : "IGNORE HIM!";
    cout << result;
    return 0;
}
