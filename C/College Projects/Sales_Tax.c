/*
THIS PROGRAM WAS MADE BY
NAME: Radwan ali Albahrani
*/

// Included libraries
#include<stdio.h>
#include<cs50.h>
#include<string.h>

// Main Function
int main(int argc, char const *argv[])
{
    // Start by declaring variables
    float sales = 0;
    int monthNumber = 0;
    float countyTax, stateTax, totalTax;
    string month;

    // Start a while loop.
    while (monthNumber < 12)
    {
        // Get sales from user
        sales = get_float("Enter Total Amount Collected (-1 to quit): ");
        
        //If Sales is -1, quit program
        if (sales == -1)
        {
            printf("Program Quit Manually, Thank you for your time!\n");
        }

        // Start a nested while loop:
        while (1)
        {
            // Get name of month
            month = get_string("Enter Name of Month (First letter must be Cap. 3 Letter acronyms.): ");

            // Validate name of month:
            if (strcmp(month, "Jan") == 0 || strcmp(month, "Feb") == 0 || 
            strcmp(month, "Apr") == 0 || strcmp(month, "May") == 0 || 
            strcmp(month, "Jun") == 0 || strcmp(month, "Jul") == 0 || 
            strcmp(month, "Aug") == 0 || strcmp(month, "Sep") == 0 || 
            strcmp(month, "Oct") == 0 || strcmp(month, "Nov") == 0 || 
            strcmp(month, "Dec") == 0 || strcmp(month, "Mar") == 0)
            {
                //If accurate, Break loop.
                break;
            }
            else
            {
                // If not accurate, tell user then loop.
                printf("Not a real month\n");
            }
            
        }
        // Set Taxes
        countyTax = sales * 0.05f;
        stateTax = sales * 0.04f;
        totalTax = countyTax + stateTax;
        
        // Print Cash at register
        printf("Total Collection at the cash register: $%.2f\n", sales);
        
        // Print Sales after substracting total tax
        printf("Sales: $%.2f\n", sales - totalTax);
        
        // Print County Tax
        printf("Sales Tax at County Level: $%.2f\n", countyTax);
        
        // Print State Tax
        printf("Sales Tax at State Level: $%.2f\n", stateTax);
        
        // Print Total tax
        printf("Total Sales Tax Collected: $%.2f\n\n", totalTax);

        //Add 1 to month number
        monthNumber++;
        
        //If all months hae been collected, tell user.
        if (monthNumber == 12)
        {
            printf("All 12 Months Have been entered.\n");
        }

    }
    return 0;
}
