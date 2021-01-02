#include <cs50.h>
#include <stdio.h>
#include <string.h>
#include <ctype.h>

//Declaring Variables
int count;

//Declaring functions
int argcheck(int argc, string argv[]);
void printing(int argc, string argv[]);


int main(int argc, string argv[])
{
    //Store return value of argcheck into final
    int final = argcheck(argc, argv);

    //if final is 1. Return it, as there is an error in the argument.
    if (final == 1)
    {
        return final;
    }

    printing(argc, argv);

    return 0;

}

//function to check the argument.
int argcheck(int argc, string argv[])
{
    //First, Check if we even got an argument. If not, Remind user that argument is necessary
    if (argc < 2)
    {
        printf("Usage: ./substitution KEY\n");
        return 1;
    }

    //If argument is given, Get the length of the argument characters.
    int n = strlen(argv[1]);

    //If the length is correct, Move on to next check.
    if (n == 26)
    {
        //Start a for loop to check for any digits in given Argument
        for (int i = 0; i < n; i++)
        {
            int digit = isdigit(argv[1][i]);
            //If a digit is found anywhere, tell the user that digits arent allowed, and stop the program by returning 1.
            if (digit != 0)
            {
                printf("Key must contain only alphabetic characters.\n");
                return 1;
            }

        }

        //Start loop for checking if there are any repeated letters
        for (int i = 0; i < n; i++)
        {
            //Assign a count 1.
            count = 1;
            //Start a second loop to check the letter duplicates starting with the second letter.
            for (int j = i + 1; j < n; j++)
            {
                //If while going through the string starting after the previous letter, the letter would match the said previous letter, add to count.
                if (toupper(argv[1][j]) == toupper(argv[1][i]) && toupper(argv[1][i]) != ' ')
                {
                    count++;
                }
            }

            //After the loop is done, if the count at any point is bigger than 1. Tell user that there must not be repeated characters and end program.
            if (count > 1)
            {
                printf("Key must not contain repeated characters.\n");
                return 1;
            }
        }
    }

    //If the first test was not passed and the argument isnt 26 characters. Tell user that the argument has to be 26 characters.
    else
    {
        printf("Key must contain 26 characters.\n");
        return 1;
    }

    //if nothing is wrong, return 0.
    return 0;
}

void printing(int argc, string argv[])
{
    //Setup for storing they key in both uppercase letters and lowercase letters.
    char keyUp[26];
    char keyLow[26];

    //Set n to the length of the key
    int n = strlen(argv[1]);

    //Start a loop that puts each letter in the key as upper and lower case in specified variables.
    for (int i = 0; i < n; i++)
    {
        keyUp[i] = toupper(argv[1][i]);
        keyLow[i] = tolower(argv[1][i]);
    }

    //Get string input from user.
    string input = get_string("Plaintext: ");

    //Set n to the number of characters in that string input for upcoming loop.
    n = strlen(input);

    //Print ciphertext without new lines to prepare for upcoming loop.
    printf("ciphertext: ");

    //Start a loop that will loop depending on how many characters are in the given string
    for (int i = 0; i < n; i++)
    {
        //Get lower variables to check if the current character is upper, lower, digit, or a space.
        int lower = islower(input[i]);
        int upper = isupper(input[i]);
        int digit = isdigit(input[i]);
        int space = isspace(input[i]);

        //if its a digit, just print it out normally
        if (digit != 0)
        {
            printf("%c", input[i]);
        }

        //if its a lowercase letter, Subtract it from the ascii number of the first lowercase letter, or a, then use the result as an index to print a letter from the lowercase key.
        else if (lower != 0)
        {
            int x = (int) input[i] - (int) 'a';
            printf("%c", keyLow[x]);
        }

        //if its an uppercase letter, Subtract it from the ascii number of the first uppercase letter, or A, then use the result as an index to print a letter from the uppercsse key.
        else if (upper != 0)
        {
            int x = (int) input[i] - (int) 'A';
            printf("%c", keyUp[x]);
        }

        //if its a space, just print out a space.
        else if (space != 0)
        {
            printf(" ");
        }
    }

    //After the loop, go to next line
    printf("\n");
}