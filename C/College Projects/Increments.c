/*
THIS PROGRAM WAS MADE BY
NAME: Radwan ali Albahrani
*/

// Including Libraries:
#include<stdio.h>

// Main function
int main(int argc, char const *argv[])
{
    //Introducing program:
    printf("This program will introduce increment methods.\n\n");

    // Assigning Variables
    int i = 5;

    //Printing Starting Value:
    printf("Starting Value is: %d\n", i);

    // Increment method 1: 
    i = i + 1;
    printf("With Method i = i + 1: i would become: %d\n", i);

    // Increment method 2: 
    i += 1;
    printf("With Method i += 1: i would become: %d\n", i);

    // Increment method 3:
    i++;
    printf("With Method i++: i would become: %d\n", i);

    //Increment method 4:
    ++i;
    printf("With Method ++i: i would become: %d\n", i);
    return 0;
}
