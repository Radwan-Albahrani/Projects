/*
THIS PROGRAM WAS MADE BY
NAME: Radwan ali Albahrani
*/
// Libraries
#include <stdio.h>
#include <stdlib.h>
#include<time.h>
void bubblesort (int *a, size_t n);
// Main
int main(int argc, char const *argv[])
{
    // Preperation of random number integer
    srand(time(0));

    // a) Multiply the value of element 4 of an integer array n with 3 and display it.
    // Introduce a.
    printf("a) Multiply the value of element 4 of an integer array n with 3 and display it.\n\n");
    // Declaring a random array
    int n1[5] = {1,2,3,4,5};
    
    // Multiplying 4th element by 3 and printing it
    int multiply = n1[3] * 3;
    printf("Multiplying the value of element four (n1[3]) of an integer array n by 3 will result in: %d\n", multiply);

    // b) Write a loop that adds all the elements of the array n[10] and stores the result in total
    printf("\n\nb) Write a loop that adds all the elements of the array n[10] and stores the result in total\n\n");
    // Declaring array
    int n[10];
    
    // First, this loop will fill this array with random numbers from 0 to 10, and print it
    for (int i = 0; i < 10; i++)
    {
        n[i] = rand() % 10;
        printf("n[%d] = %d\n", i, n[i]);
    }
    
    // Then, I will loop into the array and add all the elements and store them in a result total
    int result = 0;
    for (int i = 0; i < 10; i++)
    {
        result += n[i];
    }
    printf("Sum of elements in array (n) is: %d\n", result);
    
    // c) Initialize each of the 9 elements of a two-dimensional integer array m[3][3] to 3, using loops.
    printf("\n\nc) Initialize each of the 9 elements of a two-dimensional integer array m[3][3] to 3, using loops.\n\n");
    // Declare array
    int m[3][3];
    
    // Loop through 2D array using 2 for loops, then assign all elements to 3. Print array
    for (int i = 0; i < 3; i++)
    {
        for (int j = 0; j < 3; j++)
        {
            m[i][j] = 3;
            printf("m[%d][%d] = %d\n", i, j, m[i][j]);
        } 
    }
    
    // d) Find the largest and smallest element of a two-dimensional array sales[4][5].
    printf("\n\nd) Find the largest and smallest element of a two-dimensional array sales[4][5].\n\n");
    // Declare sales and fill it with random numbers from 1 to 1000
    int sales[4][5];
    for (int i = 0; i < 4; i++)
    {
        for (int j = 0; j < 5; j++)
        {
            sales[i][j] = rand() % 1000;
            printf("sales[%d][%d] = %d\n", i, j, sales[i][j]);
        }
        
    }

    // Get length of elements of sales
    int salesLength = sizeof(sales)/sizeof(sales[0][0]);

    // Bubble sort sales using bubblesort method using pointer to type.
    bubblesort(*sales, salesLength);
    
    // Print minimum and maximum
    printf("minimum is: %d\nMaximum is: %d\n", sales[0][0], sales[3][4]);

    // e) Copy a 100-element array into a 200-element array, starting from the 100th position of the larger array.
    printf("\n\ne) Copy a 100-element array into a 200-element array, starting from the 100th position of the larger array.\n\n");
    // Creating 2 arrays
    int array1[100];
    int array2[200];
    
    // Filling array 1 with random integers
    for (int i = 0; i < 100; i++)
    {
        array1[i] = rand() % 1000;
    }

    // Copying array 1 to array 2 from position 100
    int counter = 0;
    for (int i = 99; i < 200; i++)
    {
        array2[i] = array1[counter];
        counter++;
    }
    
    // Printing the first 5 elements of the first array
    printf("The first 5 elements of array1 is: \n");
    for (int i = 0; i < 5; i++)
    {
        printf("array1[%d] = %d\n", i, array1[i]);
    }
    printf("The 100 to 105th element of array 2 is: \n");
    // Printing element 100 to 105 in array 2
    for (int i = 99; i < 104; i++)
    {
        printf("array2[%d] = %d\n", i, array2[i]);
    }
    
    //f) Determine and store the sum and difference of the values contained in two, 100-element double arrays d1 and d2, into double arrays sum and difference.
    printf("\n\nf) Determine and store the sum and difference of the values contained in two, 100-element double arrays d1 and d2, into double arrays sum and difference.\n\n");
    // Creating 2 arrays
    // Declaring 4 arrays
    double d1[100];
    double d2[100];
    double sum[100];
    double difference[100];

    // Filling d1 and d2 with random numbers
    for (int i = 0; i < 100; i++)
    {
        d1[i] = rand() % 1000;
        d2[i] = rand() % 1000;
        
        // adding the sum to sum array
        sum[i] = d1[i] + d2[i];

        // Adding difference to difference array
        difference[i] = d1[i] - d2[i];
    }

    // Printing the first 5 elements of d1
    printf("The first 5 elements of each array provided is: \n");
    for (int i = 0; i < 5; i++)
    {
        printf("d1[%d] = %.2f\n", i, d1[i]);
        printf("d2[%d] = %.2f\n", i, d2[i]);
        printf("sum[%d] = %.2f\n", i, sum[i]);
        printf("difference[%d] = %.2f\n\n", i, difference[i]);

    }
    
    return 0;
}

void bubblesort(int *a, size_t n)
{
    // Loop through pointer like its a 1d array with max length equal to number of elements in sales
    for (int i = 0; i < n; i++) 
    {
        for (int j = i + 1; j < n; j++) 
        {
            // Bubble sorter
            if (a[i] > a[j]) 
            {
                int temp = a[j];
                a[j] = a[i];
                a[i] = temp;
            }
        }
    }
}
