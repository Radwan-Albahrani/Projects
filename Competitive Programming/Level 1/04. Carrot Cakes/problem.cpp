#include <iostream>
#define fast ios::sync_with_stdio(0), cin.tie(0)
#define ll long long

using namespace std;
int main(int argc, char const *argv[])
{   
    // Get Arguments
    ll requiredCakes, timePerAmount, cakesPerTime, SecondOven;
    cin >> requiredCakes >> timePerAmount >> cakesPerTime >> SecondOven;

    // Simulate time required for 1 oven
    ll time1 = timePerAmount, cakes1 = cakesPerTime;
    while (cakes1 < requiredCakes)
    {
        time1 += timePerAmount;
        cakes1 += cakesPerTime;
    }

    // Prepare variables for second simulation
    ll time2 = 0, cakes2 = 0, timeOven1 = 0, timeOven2Start = SecondOven, timeOven2 = 0;

    // Simulate time required when building and then using second oven
    while (cakes2 < requiredCakes)
    {
        time2++;
        timeOven1++;
        if(timeOven1 >= timePerAmount)
        {
            cakes2 += cakesPerTime;
            timeOven1 = 0;
        }

        if(time2 >= timeOven2Start)
        {
            timeOven2++;
            if(timeOven2 > timePerAmount)
            {
                cakes2+=cakesPerTime;
                timeOven2 = 0;
            }
        }
    }

    // Print out Result
    if (time1 <= time2)
    {
        cout << "NO";
    }
    else
    {
       cout << "YES";
    }

    // // Get required Arguments
    // ll requiredCakes, timePerAmount, cakesPerTime, SecondOven;
    // cin >> requiredCakes >> timePerAmount >> cakesPerTime >> SecondOven;
    // requiredCakes--;
    

    // if (requiredCakes / cakesPerTime * timePerAmount > SecondOven)
    // {
    //     cout << "YES";
    // }
    // else
    // {
    //    cout << "NO";
    // }
    // return 0;


    return 0;
}
