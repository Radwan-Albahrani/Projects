#include<stdio.h>
#include <stdlib.h>
#include <stdint.h>

int main(int argc, char *argv[])
{
    // Check if usage of program is correct.
    if (argc != 2)
    {
        printf("Usage: ./recover FILENAME\n");
        return 1;
    }

    // Get the file name
    char *cardName = argv[1];

    // Assign File to a variable
    FILE *card = fopen(cardName, "r");

    // Check if file is opened. If file is null, tell user.
    if (card == NULL)
    {
        printf("Not a File\n");
        return 1;
    }

    // Delcaring Important variables.
    int isJpeg = 0;
    int fileCount = 0;
    char fileName[8];
    FILE *image = NULL;

    //Defining a BYTE variable for the buffer
    typedef uint8_t BYTE;
    BYTE buffer[512];

    // While loop to check if current file has a 512 bite chunk
    while (fread(buffer, 512, 1, card) == 1)
    {
        // Check if current block is start of jpeg
        if (buffer[0] == 0xff && buffer[1] == 0xd8 && buffer[2] == 0xff && (buffer[3] & 0xf0) == 0xe0)
        {
            // While looping, if current chunk is jpeg, close previous file.
            if (isJpeg == 1)
            {
                fclose(image);
            }

            // Else if this is the first file, make isjpeg true
            else
            {
                isJpeg = 1;
            }

            // Print filename into created string
            sprintf(fileName, "%03i.jpg", fileCount);

            // Open that file in write mode
            image = fopen(fileName, "w");

            // Increment filecount
            fileCount++;
        }

        // If currently on a file, write a chunk
        if (isJpeg == 1)
        {
            fwrite(&buffer, 512, 1, image);
        }
    }

    // After loop is done, close all files
    fclose(image);
    fclose(card);
    return 0;
}