// Link: https://codeforces.com/contest/381/problem/A

#include <iostream>
#define fast ios::sync_with_stdio(0), cin.tie(0)
#define ll long long
using namespace std;

int main(int argc, char const *argv[])
{
    // Make input output faster
    fast;

    // Get an integer from the user
    int numberOfCards;
    cin >> numberOfCards;

    // create array
    int array[numberOfCards];

    // Get contents of array
    for(int i = 0; i < numberOfCards; i++)
    {
        cin >> array[i];
    }

    // Prepare winner variables
    int Serja = 0, Dima = 0;
    
    // Loop through the cards, with i being rightmost card, j being leftmost card, and turn being whose turn is it
    for(int i = 0, j = numberOfCards - 1, turn = 0; turn < numberOfCards; turn++)
    {
        // If its Serja's turn
        if(turn % 2 == 0)
        {
            // Check which card is bigger, give it to Serja, and remove it from the deck
            if(array[i] > array[j])
            {
                Serja += array[i];
                i++;
            }
            else
            {
                Serja += array[j];
                j--;
            }
        }
        
        // IF its Dima's Turn
        else
        {
            // Check which card is bigger, give it to Serja, and remove it from the deck
            if(array[i] > array[j])
            {
                Dima += array[i];
                i++;
            }
            else
            {
                Dima += array[j];
                j--;
            }
        }
    }
   
    cout << Serja << " " << Dima;
    return 0;
}
