/*
THIS PROGRAM WAS MADE BY
NAME: Radwan ali Albahrani
*/

//Included Libraries
#include<stdio.h>

// Main Function
int main(int argc, char const *argv[])
{
    // Introducting the program:
    printf("This program will find the sum, difference, quotient, and remainder of two numbers\n");
    
    // Declaring Variables:
    float no1, no2;
    
    // Prompting the user for two numbers:
    printf("Please Enter two numbers, separated by a space: ");

    // Using Scanf to get those numbers:
    scanf("%f %f", &no1, &no2);

    // Printing the sum:
    printf("\nThe Sum of the two numbers is (%.1f + %.1f): %.1f\n", no1, no2, (no1 + no2));

    //Printing the difference:
    printf("\nThe difference of the two numbers is (%.1f - %.1f): %.1f\n", no1, no2, (no1 - no2));
    
    //Printing the quotient:
    printf("\nThe quotient of the two numbers is (%.1f / %.1f): %.1f\n", no1, no2, (no1 / no2));

    //Printing the quotient:
    printf("\nThe Modulo of the two numbers is (%.1f % % %.1f): %i\n", no1, no2, ((int) no1 % (int) no2));
    return 0;
}
