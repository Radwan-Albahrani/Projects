#include <stdio.h>
#include <cs50.h>

int main(void)
{
    //Prompts user for Name
    string name = get_string("What is your name?\n");
    //Greets user with name
    printf("Hello, %s.\n", name);
}