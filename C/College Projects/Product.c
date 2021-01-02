/*
THIS PROGRAM WAS MADE BY
NAME: Radwan ali Albahrani
*/

// Included libraries:
#include<stdio.h>

int main(int argc, char const *argv[])
{
    // a) State that a program will calculate the product of three integers.
    printf("This program will calculate the product of 3 integers.\n");

    //b) Prompt the user to enter three integers.
    printf("Enter 3 integers, separated by a space: \n");

    // c) Define the variables x, y and z to be of type int.
    int x, y, z;
    
    // d) Read three integers from the keyboard and store them in the variables x, y and z.
    scanf("%i%i%i", &x, &y, &z);

    // e) Define the variable result, compute the product of the integers in the variables x, y and z, and use that product to initialize the variable result.
    int product = x * y * z;

    // f) Print "The product is" followed by the value of the integer variable result.
    printf("The product is: %i", product);

    return 0;
}
