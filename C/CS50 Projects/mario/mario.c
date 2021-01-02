//Standard including stuff
#include <cs50.h>
#include <stdio.h>

//Code start
int main(void)
{
    //Define height
    int height;
    do
    {
        //Ask user for height
        height = get_int("Height: ");
    }
    //Make sure user input is between specified parameters
    while (height < 1 || height > 8);

    //Define rows
    int row = 1;
    //start looping through lines
    while (row != (height + 1))
    {
        //Define spaces for each line
        int spaces = height - row;

        //While spaces isnt 0
        while (spaces != 0)
        {
            //Print a single space, then subtract from spaces
            printf(" ");
            spaces--;
        }
        //Define hashes on the left side per line
        int hashesL = 0;

        //while hashes in left side in row aren't equal to rows
        while (hashesL != row)
        {
            //Print a hash, then add to the number of hashes
            printf("#");
            hashesL++;
        }

        //Print spaces beteen hashes
        printf("  ");

        //Define Hashes on the right side.
        int hashesR = 0;
        //While hashes on the right arent equal to rows.
        while (hashesR != row)
        {
            //Print a hash, then add to the number of hashes
            printf("#");
            hashesR++;
        }
        //Move on to next line and add 1 to rows
        printf("\n");
        row++;
    }
}