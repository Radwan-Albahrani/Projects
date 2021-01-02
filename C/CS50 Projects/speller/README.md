# Speller

This program will detect spelling errors in a text based on a the dictionary provided.

## Usage

```C
$./speller /*[DICTIONARY]*/ text
```

## Logic

This program will load in your dictionary in a hash table using a hash function, then will use that table to quickly and efficiently check spellings of extremely large text files. The hash table is created from nodes, each node containing a word, and a pointer to the next word. The table of nodes has 456976 memory locations freed for nodes.

### Load

This function will take the given dictionary and load it into the Hash table. In order to do so, it will open the dictionary in read only format, and then will scan the dictionary for words (separated by a new line) using `fscanf()` until the end of file. Each time it finds a word, it will send it to the Hash function and then put it in a node of its own, unless that index was already taken. If it was taken, the word will take first spot in that node, then point to the node that was before it. It will also save a wordCount variable incase it is needed.

When done, it will close the opened file to free up memory.

### Hash

This is me trying to make my own hash function, though it turned out to be inefficient. My idea was to get the first 3 letters of a word and use those to hash this word to a specific point in my large hash table. If you take a look, it will basically calculate the index by doing the following:

<!-- $$
(FirstLetter * 26) + (SecondLetter * 26) + (ThirdLetter)
$$ --> 

<div align="center"><img src="https://render.githubusercontent.com/render/math?math=(FirstLetter%20*%2026)%20%2B%20(SecondLetter%20*%2026)%20%2B%20(ThirdLetter)%0D" width = "500"></div>

### Check

The check function will ensure that the word in your text is inside the dictionary. First it will ensure your word is lower cased so the hashing and comparing goes smoothly, using the `tolower()`. Then it will hash that word, and use a for loop to check the linked list associated with that word. If the word is found, return true, making it a correctly spelled word. Else, return false.

### Unload

Unload will go through the entire hash table and free up every linked list in the table. To do so will require two loops, one loops through every element in the table, and the other will loop through every node connected to that element in the list. If a node is found, save that node's address in a temporary variable, move the cursor to the next node in the list, then free up that previous node. Once done, return true.

### Hash_It

Hash it is a hash function I got from an online source to ensure efficiency in hashing.
