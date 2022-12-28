#include <iostream>
#define fast ios::sync_with_stdio(0), cin.tie(0)

using namespace std;

int main(int argc, char const *argv[])
{
    fast;
    int n, m, k;
    cin >> n >> m >> k;

    printf("%d", (7 - n) + (7 - m) + (7 - k));
    return 0;
}
