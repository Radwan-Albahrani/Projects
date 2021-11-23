#include <iostream>
#include <string>

using namespace std;

int main()
{
    // Define Needed Variables
    string math;
    string numbers[100];
    string symbols;

    // Start a counter to determine how many numbers we have.
    int counter = 0;

    // Prompt User for expression
    cout << "Input a math equation with + - * or /: ";

    // Get the user's expression
    getline(cin, math);

    // Loop through the expression.
    for (int i = 0; i < math.length(); i++)
    {
        // If you find a digit
        if (isdigit(math[i]))
        {
            // Start a temporary string and a new temporary variable x.
            string temp;
            int x;

            // start a second loop starting with the first digit in the upcoming number.
            for (x = i; x <= math.length(); x++)
            {
            // As long as the number is still a digit, add it to the temporary string
            if (isdigit(math[x]))
            {
                temp += math[x];
            }
            
            // As soon as the current character is no longer a digit
            else
            {
                // Add the number to the numbers array and increase counter, then exit loop.
                numbers[counter] = temp;
                counter += 1;
                break;
            }
            }
            // continue the original loop starting with the last none digit character.
            i = x;
        }

        // If its a symbol from the following symbols.
        if (math[i] == '+' || math[i] == '-' || math[i] == '/' || math[i] == '*')
        {
            // Add it to symbols string.
            symbols.push_back(math[i]);
        }
    }

    // After the loop, Validate the expression using number of symbols compared to number of numbers.
    if (counter - symbols.length() == 1)
    {
        int loopc = counter;
        // Loop through the amount of numbers you have.
        for (int i = 0; i < loopc; i++)
        {
            // If you no longer have any numbers, break the loop.
            if (counter == 0)
            {
                break;
            }

            // Start with any possible division.
            int index = symbols.find('/');
            
            // If division is found
            if(index != -1)
            {
                // Check if the second number in that division is not a 0
                if (stod(numbers[index + 1]) != 0)
                {
                    // DEBUG:
                    string expression = numbers[index] + " / " + numbers[index + 1];
                    cout << "Expression: " << expression << endl; 

                    // Evaluate division
                    double answer = stod(numbers[index]) / stod(numbers[index + 1]);
                    
                    // Put the answer back into the array
                    numbers[index] = to_string(answer);

                    // Move everything to the right back one.
                    for(int x = index + 1; x < counter - 1; x++)
                    {
                    numbers[x] = numbers[x+1];
                    }

                    // Reduce counter.
                    counter -= 1;

                    // Erase used symbol.
                    symbols.erase(symbols.begin() + index);
                    
                    // DEBUG:
                    cout << "Answer: " << answer << endl;
                }

                // If it is a zero, tell the user, then break the loop and exit the program.
                else
                {
                    cout << "Division by 0 is not possible" << endl;
                    break;
                }

                continue;
            }

            // Start with multiplication.
            index = symbols.find('*');

            if (index != -1)
            {
                // DEBUG:
                string expression = numbers[index] + " * " + numbers[index + 1];
                cout << "Expression: " << expression << endl; 

                // Evaluate multiplication
                double answer = stod(numbers[index]) * stod(numbers[index + 1]);
                
                // Put the answer back into the array
                numbers[index] = to_string(answer);

                // Move everything to the right back one.
                for(int x = index + 1; x < counter - 1; x++)
                {
                numbers[x] = numbers[x+1];
                }

                // Reduce counter.
                counter -= 1;

                // Erase used symbol.
                symbols.erase(symbols.begin() + index);
                
                // DEBUG:
                cout << "Answer: " << answer << endl;

                continue; 
            }

            // Next, addition
            index = symbols.find('+');

            if (index != -1)
            {
                // DEBUG:
                string expression = numbers[index] + " + " + numbers[index + 1];
                cout << "Expression: " << expression << endl; 

                // Evaluate addition
                double answer = stod(numbers[index]) + stod(numbers[index + 1]);
                
                // Put the answer back into the array
                numbers[index] = to_string(answer);

                // Move everything to the right back one.
                for(int x = index + 1; x < counter - 1; x++)
                {
                numbers[x] = numbers[x+1];
                }

                // Reduce counter.
                counter -= 1;

                // Erase used symbol.
                symbols.erase(symbols.begin() + index);
                
                // DEBUG:
                cout << "Answer: " << answer << endl; 

                continue;
            }

            // finally, subtraction.
            index = symbols.find('-');
            if (index != -1)
            {
                // DEBUG:
                string expression = numbers[index] + " - " + numbers[index + 1];
                cout << "Expression: " << expression << endl; 

                // Evaluate subtraction
                double answer = stod(numbers[index]) - stod(numbers[index + 1]);
                
                // Put the answer back into the array
                numbers[index] = to_string(answer);

                // Move everything to the right back one.
                for(int x = index + 1; x < counter - 1; x++)
                {
                numbers[x] = numbers[x+1];
                }

                // Reduce counter.
                counter -= 1;

                // Erase used symbol.
                symbols.erase(symbols.begin() + index);
                
                // DEBUG:
                cout << "Answer: " << answer << endl; 

                continue;
            }
        }

        // After the loop, print out the answer
        cout << "The final answer is: " << stod(numbers[0]) << endl;
    }


    // If the expression was not validated, tell the user.
    else
    {
        cout << "Expression Error, Try again!\n";
    }
}