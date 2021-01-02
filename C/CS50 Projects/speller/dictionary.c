// Implements a dictionary's functionality

#include <stdbool.h>
#include <stdio.h>
#include <string.h>
#include <stdlib.h>
#include <ctype.h>
#include <strings.h>
#include "dictionary.h"

// Represents a node in a hash table
typedef struct node
{
    char word[LENGTH + 1];
    struct node *next;
}
node;
unsigned int hash_it(const char *word);
// Number of buckets in hash table
const unsigned int N = 456976;

// Hash table
node *table[N];

// Word count Variable
int wordcount = 0;

// Loads dictionary into memory, returning true if successful else false
bool load(const char *dictionary)
{
    // Loading dictionary
    FILE *dict = fopen(dictionary, "r");

    // If not found, return false.
    if (!dict)
    {
        return false;
    }

    // Create a variable to hold a word and initialize it to null
    char word[LENGTH + 1];

    // Start a while loop to read a word from the dictionary and add it to word as long as not end of file
    while (fscanf(dict, "%s", word) != EOF)
    {
        // Get the index in the hash table of this word using the hash function.
        unsigned int index = hash_it(word);

        // Get an empty node
        node *n = malloc(sizeof(node));

        // Null check n
        if (n == NULL)
        {
            printf("Memory Error");
            free(n);
            return false;
        }

        // Copy current word into node
        strcpy(n->word, word);

        // Set next to null
        n->next = NULL;

        // If current index on table is null
        if (table[index] == NULL)
        {
            // Give it current node
            table[index] = n;

            // Increase word count.
            wordcount++;
        }

        // else if its not empty
        else
        {
            // Give node the first node in the table
            n->next = table[index];

            // Give the table the current node
            table[index] = n;

            // Increase word count.
            wordcount++;
        }

    }

    // Closing dictionary
    fclose(dict);

    // If while loop successful, return true
    return true;
}

// My hash function (inefficient)
unsigned int hash(const char *word)
{
    // Get first letter from word
    char first_letter = word[0];

    // Get Second Letter from word
    char second_letter = word[1];

    // Get third letter
    char third_letter = word[2];

    // Initialize index
    int index = 0;

    // If first letter capital case
    if (first_letter >= 'A' && first_letter <= 'Z')
    {
        // Subtract it by A then multiply by 26.
        index += (first_letter - 'A') * 26;

        // If second letter Capital
        if (second_letter >= 'A' && second_letter <= 'Z')
        {
            // Subtract by A and add to index, return index
            index += (second_letter - 'A') * 26;

            // Third letter
            if (third_letter >= 'A' && third_letter <= 'Z')
            {
                index += (third_letter - 'A');
                return index;
            }

            else if (third_letter >= 'a' && third_letter <= 'z')
            {
                index += (third_letter - 'a');
                return index;
            }
        }

        // If second letter is lower case
        else if (second_letter >= 'a' && second_letter <= 'z')
        {
            // Subtract by A and add to index, return index
            index += (second_letter - 'a') * 26;

            // Third letter
            if (third_letter >= 'A' && third_letter <= 'Z')
            {
                index += (third_letter - 'A');
                return index;
            }

            else if (third_letter >= 'a' && third_letter <= 'z')
            {
                index += (third_letter - 'a');
                return index;
            }
        }
    }

    // If first letter is lower case
    else if (first_letter >= 'a' && first_letter <= 'z')
    {
        // Subtract by a and multiply by 26.
        index += (first_letter - 'a') * 26;

        // if second letter is capital:
        if (second_letter >= 'A' && second_letter <= 'Z')
        {
            // Subtract by A and add to index, return index
            index += (second_letter - 'A') * 26;

            // Third letter
            if (third_letter >= 'A' && third_letter <= 'Z')
            {
                index += (third_letter - 'A');
                return index;
            }

            else if (third_letter >= 'a' && third_letter <= 'z')
            {
                index += (third_letter - 'a');
                return index;
            }
        }

        // If second letter is small
        else if (second_letter >= 'a' && second_letter <= 'z')
        {
            // Subtract by A and add to index, return index
            index += (second_letter - 'a') * 26;

            // Third letter
            if (third_letter >= 'A' && third_letter <= 'Z')
            {
                index += (third_letter - 'A');
                return index;
            }

            else if (third_letter >= 'a' && third_letter <= 'z')
            {
                index += (third_letter - 'a');
                return index;
            }
        }
    }

    // if not a letter, tell us its not in range
    else
    {
        printf("Not in range: ");
        return first_letter;
    }
    return 0;
}

// Returns number of words in dictionary if loaded else 0 if not yet loaded
unsigned int size(void)
{
    // returns word count which is calculated in Load
    return wordcount;
}

// Returns true if word is in dictionary else false
bool check(const char *word)
{
    // Get the word's length
    int loopc = strlen(word);

    // Prepare a string to write to
    char str[LENGTH + 1];

    // Start a for loop
    for (int i = 0; i < loopc + 1; i++)
    {
        str[i] = tolower(word[i]);
    }
    unsigned int index = hash_it(str);
    // Spell checker. Get first node, and while its not null, every loop go to next item in list
    for (node *tmp = table[index]; tmp != NULL; tmp = tmp->next)
    {
        // If its correct, stop loop and return true
        if (strcasecmp(str, tmp->word) == 0)
        {
            return true;
        }
    }

    // if loop is done, that means it wasn't found, so it was misspelled.
    return false;
}

// Unloads dictionary from memory, returning true if successful else false
bool unload(void)
{
    // Loop times equal to buckets in table
    for (int i = 0; i < N; i++)
    {
        for (node *cursor = table[i]; cursor != NULL;)
        {
            // Crate another temp variable to hold it
            node *temp = cursor;

            // Move cursor to next location
            cursor = cursor->next;

            // Free previous variable
            free(temp);
        }
    }

    return true;
}


// Taken from: this hash function was found on the internet but there was no author mentioned. Found here: https://gist.github.com/OxiBo/91abfc3d9ff7c8fcfa281895111314db
unsigned int hash_it(const char *word)
{
    unsigned int hash = 0;
    for (int i = 0; word[i] != '\0'; i++)
    {
        hash = 5 * hash + word[i];
    }
    return hash % N;
}
