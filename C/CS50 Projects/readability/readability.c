#include <cs50.h>
#include <stdio.h>
#include <string.h>
#include <ctype.h>

//Declaring Required Variables
int letters;
int words;
int sentences;
float L;
float S;
bool isNextWord = true;
string sentence;

//Declaring required Functions.
void Count(void);

int main(void)
{
    //Getting a String from the user.
    sentence = get_string("Text: ");

    //Assigning some variables to 0 as a start
    letters = 0;
    words = 0;
    sentences = 0;

    //Calling the count function
    Count();

    //Calculating L and S for index
    L = (float) letters / words * 100;
    S = (float) sentences / words * 100;

    //Calculating Index
    float index = 0.0588 *  L - 0.296 * S - 15.8;

    //If index is less than 1, Print before grade 1
    if (index < 1)
    {
        printf("Before Grade 1\n");
    }

    //If Index is between 1 and 16, print grade level
    else if (index >= 1 && index <= 16)
    {
        printf("Grade %.0f\n", index);
    }

    //If its bigger than 16, print 16+
    else
    {
        printf("Grade 16+\n");
    }
}

//The counting function
void Count(void)
{
    //Starting with a loop that will go through every character in given string above
    for (int i = 0, n = strlen(sentence); i < n; i++)
    {
        //A variable holding whether or not we are at a space. If its 0, its not a space, otherwise its a space.
        int space = isspace(sentence[i]);
        int punct = ispunct(sentence[i]);

        //If its not a space
        if (space == 0)
        {
            //Check first if its a new word.
            if (isNextWord == true)
            {
                //If its a new word, Tell it that its no longer a new word. Add to word count and letter count.
                words++;
                isNextWord = false;
                if (punct == 0)
                {
                    letters++;
                }
            }

            //Check if it is end of sentence using specified Ends. If it is, add a count to sentences
            else if (sentence[i] == '!' || sentence[i] == '?' || sentence[i] == '.')
            {
                sentences++;
            }

            //If its neither a new word nor a new sentence, just add to the number of letters.
            else if (punct == 0)
            {
                letters++;
            }

        }

        //If we reach a space, make sure the program knows that next time its not a space, its a new word.
        else
        {
            isNextWord = true;
        }

    }
}