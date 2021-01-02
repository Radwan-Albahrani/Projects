/*
THIS PROGRAM WAS MADE BY
NAME: Radwan ali Albahrani
*/

// Included Libraries:
#include<stdio.h>
#include<stdlib.h>
#include<string.h>

// Main function
int main(int argc, char const *argv[])
{
    //Introduce program:
    printf("This program will find the summation of all negative numbers given.\n");

    //Declare variables:
    float sum;
    // Start loop:
    while (1)
    {
        // Creating a character array with 30 bits memory
        char str[30];
        
        // Asking the user for a number
        printf("Enter a Negative Number (When done, Type \"Break\"): ");

        // Getting the input as string and putting it inside str array
        scanf("%s", &str); 

        // Converting Str array to a float number
        float f1 = strtof(str, NULL);

        // If number is negative, add it to sum.
        if (f1 < 0)
        {
            sum += f1;
            printf("Sum is now: %.2f\n", sum);
        }

        // If user types break, loop will end
        else if (strcmp(str, "Break") == 0)
        {
            printf("\nFinal total is: %.2f\n", sum);
            printf("Thank you for using this program.\n");
            break;
        }
        
        // Else, Tell user it is not negative.
        else
        {
            printf("Number is not negative. Try again\n");
        }
    }
    return 0;
}
