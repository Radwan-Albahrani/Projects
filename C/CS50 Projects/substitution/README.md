# Substitution

This program will use a given encryption key and a plaintext to substitute alphabetical letters based on your key.

## Usage

```C
$ ./substitution //KEY
//Plaintext: ENTER PLAIN TEXT HERE. WILL OUTPUT CYPHERED TEXT
```

## Logic

Before running the program, we must check your encryption key/cipher to make sure it follows specific criteria:

* It must be alphabetic characters only.
* It must not contain repeated characters.
* It must be 26 characters long.

If all the above holds true about your key, it will swiftly store your key in two arrays, one containing the entire key in small letters, and one will hold the entire key in capital letters. This will be useful during encryption.

Your key is basically used as a new order for alphabetical letters. For example. If your key is 26 letters starting with `zxg`, then `a` will be `z`, `b` will be `x`, and `c` will be `g`.

During encryption, it will take your text and loop through each character in that text. It will test the character based on the following:

* If the character is a lowercase letter or uppercase, print the corresponding key of that letters location. To find the location, subtract the letter from the ascii number of the first letter: `A/a`.
* If the character is a digit, print it without change.
* If the character is a space, print it without change.\

This loop will go through each letter and test them separately, giving you the appropriate response. Once the loop is over, go to the next line then end the program.
