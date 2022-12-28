#include <iostream>
#define fast ios::sync_with_stdio(0), cin.tie(0)

using namespace std;

int main(int argc, char const *argv[])
{
    /* code */
    fast;
    int n, m;
    cin >> n >> m;

    int dominoes = n * m;
    int pairs = dominoes / 2;
    cout << pairs;
    return 0;
}
