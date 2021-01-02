//Main includes
#include <stdio.h>
#include <cs50.h>

//Assigning method specific variables
int count = 0;
bool isVisa = false;
bool isMaster = false;
bool isAmerican = false;
bool invalid = false;

//Assigning my functions
long dout(long num);

//Main function
int main(void)
{
    //Assigning variables
    long crednum = get_long("Number: ");
    count = 0;
    long tempcrednum = crednum;

    //Counting digits loop
    while (tempcrednum > 0)
    {
        tempcrednum /= 10;
        count++;
    }

    //Get the final count from the function below.
    int finalcount = dout(crednum);

    //If the credit card was not invalidated
    if (invalid == false)
    {
        //Check if the final count is divisible by 10
        if (finalcount % 10 == 0)
        {
            //Check which type of card it is
            if (isVisa == true)
            {
                printf("VISA\n");
            }
            else if (isMaster == true)
            {
                printf("MASTERCARD\n");
            }
            else if (isAmerican == true)
            {
                printf("AMEX\n");
            }

            //If its not any of those cards, make it invalid
            else
            {
                printf("INVALID\n");
            }
        }

        //Of course if it was already invalid just invalidate it.
        else
        {
            printf("INVALID\n");
        }
    }

    else
    {
        printf("INVALID\n");
    }
}



long dout(long num)
{
    //declaring important variables
    int totaln2 = 0;
    int total2 = 0;

    //creating a temporary variable to hold the main num
    long tempnum = num;

    //creating a loop counter
    int loopc = count;

    //Creating a boolean variable to change every digit
    bool value = true;

    //While loop counter is bigger or equal to 0
    while (loopc > 0)
    {
        //if value is true, then we are on the last digit
        if (value == true)
        {
            //get the digit
            long d = tempnum % 10;

            //Add it to total
            totaln2 += d;

            //devide tempnum by 10 and assign it to get rid of that digit
            tempnum = tempnum / 10;

            //set value to false then subtract from loopcounter to start the next loop
            value = false;
            loopc--;

        }

        //if value is false
        else
        {
            //Get last digit and multiply it by 2
            long d = tempnum % 10;
            d = d * 2;

            //If d now is a 2 digit number
            if ((d / 10) != 0)
            {
                //Add the last digit of that number
                total2 += d % 10;

                //Divide the number by 10
                d = d / 10;
                //Add that to the total
                total2 += d;
            }

            //If its not a two digit number
            else
            {
                //add the digit to total
                total2 += d;
            }


            //Clear last digit
            tempnum = tempnum / 10;

            //Set value to true and reduce loopcounter to loop again.
            value = true;
            loopc--;
        }
    }

    //refilling loopcount again.
    loopc = count;

    //refilling tempnum
    tempnum = num;

    //Make sure the digit count is valid for it to be any of the credit card types
    if (loopc == 13 || loopc == 16 || loopc == 15)
    {
        //Shred it to pieces till you get the first two digits
        while (loopc > 2)
        {
            tempnum = tempnum / 10;
            loopc--;
        }

        //If the first digit is 4, then its definitely a visa
        if (tempnum / 10 == 4)
        {
            isVisa = true;
        }

        //If the first 2 digits are any of these numbers, its gotta be a mastercard
        else if (tempnum == 51 || tempnum == 52 || tempnum == 53 || tempnum == 54 || tempnum == 55)
        {
            isMaster = true;
        }

        //if the first 2 digits are any of these numbers, its gotta be an american express
        else if (tempnum == 34 || tempnum == 37)
        {
            isAmerican = true;
        }

        //if its none of the above it has to be invalid
        else
        {
            invalid = true;
        }
    }

    //finally, return the final total.
    return (total2 + totaln2);
}