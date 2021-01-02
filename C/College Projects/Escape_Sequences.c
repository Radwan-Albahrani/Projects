/*
THIS PROGRAM WAS MADE BY
NAME: Radwan ali Albahrani
*/

// Included libraries:
#include<stdio.h>

// Main function
int main(int argc, char const *argv[])
{
    // a) Define the variables c, thisVariable, q76354 and number to be of type int.
    int c, thisVariable, q76354, number;

    // b) Prompt the user to enter an integer. End your prompting message with a colon (:) followed by a space and leave the cursor positioned after the space.
    printf("Enter an Integer: ");

    // c) Read an integer from the keyboard and store the value entered in integer variable a.
    scanf("%i", &c);

    // d) If number is not equal to 7, print "The variable number is not equal to 7."
    if(c != 7) {printf("The variable number is not equal to 7.\n");}

    // e) Print the message "This is a C program." on one line.
    printf("This is a C program.\n");

    // f) Print the message "This is a C program." on two lines so that the first line ends with C.
    printf("This is a C\nProgram\n");

    // g) Print the message "This is a C program." with each word on a separate line.
    printf("This\nIs\nA\nC\nProgram\n");

    // h) Print the message "This is a C program." with the words separated by tabs.
    printf("This\tIs\tA\tC\tProgram");
    return 0;
}
