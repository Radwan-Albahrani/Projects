/*
THIS PROGRAM WAS MADE BY
NAME: Radwan ali Albahrani
*/

//Included Libraries
#include<stdio.h>
#include<cs50.h>

// Main Function:
int main(int argc, char const *argv[])
{
    //Exercise 3-1
    // Introduce the problem
    printf("In this program, we will try solving given equation in multiple ways and decide which one is right.\n");
    printf("The equation is: ax^3 +7");

    // First, Assign a Value for A and X.
    int a = get_int("\nAssign integer Value for a in the equation: ");
    int x = get_int("Assign integer Value for x in the equation: ");

    // Try given methods.
    // a) y = a * x * x * x + 7;
    int result = a * x * x * x + 7;
    printf("\nUsing the method \n\"y = a * x * x * x + 7\",\nour result will be: %i\nThis Result is correct\n", result);

    // b) y = a * x * x * ( x + 7 );
    result = a * x * x * ( x + 7 );
    printf("\nUsing the method \n\"a * x * x * ( x + 7 )\", \nour result will be: %i\nThis Result is wrong\n", result);

    // c) y = ( a * x ) * x * ( x + 7 );
    result = ( a * x ) * x * ( x + 7 );
    printf("\nUsing the method \n\"( a * x ) * x * ( x + 7 )\", \nour result will be: %i\nThis Result is wrong\n", result);

    // d) y = ( a * x ) * x * x + 7;
    result = ( a * x ) * x * x + 7;
    printf("\nUsing the method \n\"( a * x ) * x * x + 7\", \nour result will be: %i\nThis Result is correct\n", result);

    // e) y = a * ( x * x * x ) + 7;
    result = a * ( x * x * x ) + 7;
    printf("\nUsing the method \n\"a * ( x * x * x ) + 7\", \nour result will be: %i\nThis Result is correct\n", result);

    // f) y = a * x * ( x * x + 7 );
    result = a * x * ( x * x + 7 );
    printf("\nUsing the method \n\"a * x * ( x * x + 7 )\", \nour result will be: %i\nThis Result is wrong\n\n", result);
    return 0;
}
