/*
THIS PROGRAM WAS MADE BY
NAME: Radwan ali Albahrani
*/

// Included Libraries:
#include<stdio.h>

// Main Function
int main(int argc, char const *argv[])
{
    // Declare Variables
    int number;
    // Introduce program:
    printf("This program will check if your number is even or odd.\n");
    // Ask the user for a number:
    printf("Please Enter a Number: ");
    scanf("%d",&number);

    // Start if statement
    if(number % 2 == 0)
    {
        printf("Your number is even.");
    }
    else
    {
        printf("Your Number is odd.");
    }
    
    return 0;
}
