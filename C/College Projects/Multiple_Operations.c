/*
THIS PROGRAM WAS MADE BY
NAME: Radwan ali Albahrani
*/

// Included Libraries:
#include<stdio.h>

// Main function
int main(int argc, char const *argv[])
{
    //First, get variables x y z from user:
    int x, y ,z;
    printf("Enter 3 integers, x y z, Separated by a space: ");
    scanf("%d %d %d", &x, &y, &z);
    // a) Assign the sum of x and y to z and increment the value of x by 1 after the calculation.
    int sum = x++ + y + z;
    printf("The sum of the given values is: %d\nx is now: %d.\n", sum, x);
    // b) Multiply the variable product by 2 using the *= operator.
    sum *= 2;
    printf("The sum multiplied by 2 using sum *=2 is: %d\n", sum);

    // c) Multiply the variable product by 2 using the = and * operators.
    sum = sum * 2;
    printf("The sum multiplied by 2 using sum = sum * 2 is: %d\n", sum);

    // d) Test if the value of the variable count is greater than 10. If it is, print “Count is greaterthan 10.”
    if(sum > 10)
    {
        printf("Sum is currently greater than 10. Its value is: %d\n", sum);
    }
    else
    {
        printf("Sum is currently less than 10. Its value is: %d\n", sum);
    }
    
    // e) Decrement the variable x by 1, then subtract it from the variable total.
    sum -= --x;
    printf("Sum is now: %d, While x is: %d\n", sum, x);

    // f) Add the variable x to the variable total, then decrement x by 1.
    sum += x--;
    printf("Sum is now: %d, While x is: %d\n", sum, x);
    // g) Calculate the remainder after q is divided by divisor and assign the result to q. Write this statement in two different ways.
    int q = sum;
    printf("Currently, sum is equal to: %d, while z = %d. I will calculate the remainder if sum was divided by z\n", sum, z);
    printf("Method 1: sum %%= z\n");
    q %= z;
    printf("Sum is now: %d\n", q);
    q = sum;
    printf("Method 2: sum = sum %% z\n");
    q = q % z;
    printf("Sum is now: %d\n\n", q);

    // h) Print the value 123.4567 with 2 digits of precision. What value is printed?
    printf("The number 123.4567 printed with 2 digits precision is: %.2f\n", 123.4567f);

    // i) Print the floating-point value 3.14159 with three digits to the right of the decimal point.What value is printed?
    printf("The number 3.14159 printed with 3 digits after the decimal point is %.3f\n", 3.14159);
    return 0;
}
