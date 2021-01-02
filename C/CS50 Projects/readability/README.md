# Readability

This program will measure how readable a given text is, and will rate it from a grade 1 level to a grade 12 level.

## Usage

```C
Text: // Get text here
// Print grade level here
```

## Logic

This program will test a sentences readability level based on an index called Coleman-Liau index. This index is basically:

<div align="center"><img src="https://render.githubusercontent.com/render/math?math=index%20%3D%200.0588%20*%20L%20-%200.296%20*%20S%20-%2015.8%0D" width = "250"></div>

This formula will give you a number that, when rounded to the nearest whole number, will give you the grade level of that text. But what is L and what is S?

L is the average number of letters per 100 words, and S is the average number of sentences per 100 words. To calculate those, I've implemented a function called `count()`. This function will be responsible for counting letters, words, and sentences in a text. After the count is done, we simply use these formulas to calculate L and S:

This for L:

<div align="center"><img src="https://render.githubusercontent.com/render/math?math=L%20%3D%20%5Cfrac%7BLetters%7D%7BWords%7D%20*%20100%0D" width = "250"></div>

This for S:

<div align="center"><img src="https://render.githubusercontent.com/render/math?math=S%20%3D%20%5Cfrac%7BSentences%7D%7BWords%7D*%20100%0D" width = "250"></div>

### The count function

* The count function will utilize libraries such as `string.h` and `ctype.h` to count letters, words, and sentences. It will also utilize a boolean variable responsible for knowing when the next word is starting.

* First, it will start by getting the length of the inputted text, and will loop over that text letter by letter using that length.

* It will try to detect any punctuation or spaces using `isspace()` and `ispunct()` as those will be necessary when counting letters or detecting the next word. These functions will return 0 if a space or a punctuation was not detected.

* If the current character is not a space, it will first check if this is the next word. If it is, it will increment words, set next word to false, and start incrementing any none-punctuation letters.

* If the current character is the end of a sentence (! or ? or .), it will increment sentences.

* Then it will loop until it is a space. if it is, it will make `isNextWord` true. Then it will loop until it is not a space again.

* This will keep going until it is at the end of the sentence. After the end, it will go back to main to start printing out output based on the index.
