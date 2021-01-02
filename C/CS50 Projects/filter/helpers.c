#include "helpers.h"
#include<math.h>
#include<string.h>

int cap(int number);

// Convert image to grayscale
void grayscale(int height, int width, RGBTRIPLE image[height][width])
{
    // Starting a loop that will go through pixels in the height
    for (int i = 0; i < height; i++)
    {
        // Starting a loop that will go through pixels in the width on the current height
        for (int j = 0; j < width; j++)
        {
            // Assign red green and blue their own variables
            float red = image[i][j].rgbtRed;
            float green = image[i][j].rgbtGreen;
            float blue = image[i][j].rgbtBlue;

            // Get the average rgb value from red green and blue
            float average = (red + green + blue) / 3.00f;

            // Round the average value and make it an int incase of not whole average
            int finalaverage = round(average);

            // Set this new average to a current pixel's rgb values
            image[i][j].rgbtBlue = finalaverage;
            image[i][j].rgbtRed = finalaverage;
            image[i][j].rgbtGreen = finalaverage;
        }
    }
    return;
}

// Reflect image horizontally
void reflect(int height, int width, RGBTRIPLE image[height][width])
{
    // Create temporary variable
    RGBTRIPLE temp;

    // Starting a loop that will go through pixels in the height
    for (int i = 0; i < height; i++)
    {
        // Starting a loop that will go through half pixels in the width on the current height
        for (int j = 0; j < width / 2; j++)
        {
            // Save this pixel to temp
            temp = image[i][j];

            // Swap Current pixel with the pixel opposite to it, like a mirror
            image[i][j] = image[i][width - j - 1];

            //Set the pixel opposite to the same pixel that was current.
            image[i][width - j - 1] = temp;
        }
    }
    return;
}

// Blur image
void blur(int height, int width, RGBTRIPLE image[height][width])
{
    // Create temporary variable
    RGBTRIPLE temp[height][width];

    // Loop over height of image
    for (int i = 0; i < height; i++)
    {
        // Loop over width of image
        for (int j = 0; j < width; j++)
        {
            // Copy Each value from real image into temp variable
            temp[i][j].rgbtRed = image[i][j].rgbtRed;
            temp[i][j].rgbtGreen = image[i][j].rgbtGreen;
            temp[i][j].rgbtBlue = image[i][j].rgbtBlue;

        }

    }


    // Loop over height of image
    for (int i = 0; i < height; i++)
    {
        // Loop over row of image
        for (int j = 0; j < width; j++)
        {
            // Every time a full loop over width is done, Reset average counter. Keep float for rounding later
            float average = 0.0;

            // With full loop, Reset RGB values to zero as well to start the next average
            int red = 0;
            int green = 0;
            int blue = 0;

            // Loop over the pixel before and after current pixel
            for (int k = -1; k <= 1; k++)
            {
                // Loop over the pixels above and below current pixel
                for (int l = -1; l <= 1; l++)
                {
                    // If current index is within index bounds (minimum 0 maximum height - 1)
                    if (i + k != height && i + k != -1 && j + l != width && j + l != -1)
                    {
                        // Add current pixel RGB values to the aforementioned RGB counters.
                        red += temp[i + k][j + l].rgbtRed;
                        green += temp[i + k][j + l].rgbtGreen;
                        blue += temp[i + k][j + l].rgbtBlue;

                        // Add 1 to average to use for calculations later
                        average++;
                    }
                }
            }
            // Once we get all rgb values for each of the pixels around current pixel, Set original image rgb values to the average of those pixels taken.
            image[i][j].rgbtRed = round(red / average);
            image[i][j].rgbtGreen = round(green / average);
            image[i][j].rgbtBlue = round(blue / average);
        }
    }
}

// Detect edges
void edges(int height, int width, RGBTRIPLE image[height][width])
{
    // Assign the sobel operator into variables for x and y
    int Gx[3][3] = {{-1, 0, 1}, {-2, 0, 2}, {-1, 0, 1}};
    int Gy[3][3] = {{-1, -2, -1}, {0, 0, 0}, {1, 2, 1}};

    // Create temporary variable
    RGBTRIPLE temp[height][width];

    // Loop over height of image
    for (int i = 0; i < height; i++)
    {
        // Loop over width of image
        for (int j = 0; j < width; j++)
        {
            // Copy Each value from real image into temp variable
            temp[i][j].rgbtRed = image[i][j].rgbtRed;
            temp[i][j].rgbtGreen = image[i][j].rgbtGreen;
            temp[i][j].rgbtBlue = image[i][j].rgbtBlue;

        }

    }

    // Loop over height of image
    for (int i = 0; i < height; i++)
    {
        // Loop over row of image
        for (int j = 0; j < width; j++)
        {
            // Delare RGB x values
            int RedX = 0;
            int GreenX = 0;
            int BlueX = 0;

            // Declare RGB y values
            int RedY = 0;
            int GreenY = 0;
            int BlueY = 0;


            // Loop over the pixel before and after current pixel
            for (int k = -1; k <= 1; k++)
            {
                // Loop over the pixels above and below current pixel
                for (int l = -1; l <= 1; l++)
                {
                    // If current index is within index bounds (minimum 0 maximum height - 1)
                    if (i + k != height && i + k != -1 && j + l != width && j + l != -1)
                    {
                        // Getting the weight value for x and y
                        int weightX = Gx[k + 1][l + 1];
                        int weightY = Gy[k + 1][l + 1];

                        // Adding Weighted sum to RGB values of x
                        RedX += weightX * temp[i + k][j + l].rgbtRed;
                        GreenX += weightX * temp[i + k][j + l].rgbtGreen;
                        BlueX += weightX * temp[i + k][j + l].rgbtBlue;

                        // Adding Weighted Sum to RGB values of y
                        RedY += weightY * temp[i + k][j + l].rgbtRed;
                        GreenY += weightY * temp[i + k][j + l].rgbtGreen;
                        BlueY += weightY * temp[i + k][j + l].rgbtBlue;

                    }
                }
                // Setting current pixel to the sobel operator results
                image[i][j].rgbtRed = cap(round(sqrt((RedX * RedX) + (RedY * RedY))));
                image[i][j].rgbtBlue = cap(round(sqrt((BlueX * BlueX) + (BlueY * BlueY))));
                image[i][j].rgbtGreen = cap(round(sqrt((GreenX * GreenX) + (GreenY * GreenY))));

            }

        }

    }
    return;
}

int cap(int number)
{
    if (number > 255)
    {
        number = 255;
        return number;
    }
    return number;
}