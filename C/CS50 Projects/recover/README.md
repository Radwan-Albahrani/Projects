# Recover

This program will try to detect JPEG files in a memory card and retrieve them for the user.

## Usage

```C
$ ./recover //CARD.RAW
// WILL OUTPUT ALL FILES IN CURRENT FOLDER.
```

## Logic

This program will look for specific byte structures in order to figure out the datatype of the specific file. If that file is a Jpeg file, it will recover it and then start recovering every jpeg file after it.

### Recovery Process

After it has received your memory card, the first thing it will do is start reading it in chunks of 512 bits. With each chunk, it will read the first 4 bits and make sure they match the Jpeg signature.

* The first bit has to be  `0xff`
* The second bit has to be `0xd8`
* The third bit has to be `0xff`
* The forth bit is different in that it has to be between `0xe0` and `0xef`, So it needs a bit of manipulation to ensure that you change it into `0xe0`

Once a Jpeg is found, mark that its found and start recovering it into a file that is given a numbered name (based on how many you have recovered so far, Starting at 000), keep recovering it in 512 bit chunks until you encounter the next Jpeg file.

The problem with this method is that it assumes the Jpeg files are neatly arranged one after the other. Meaning that even if there was a different type of file between the current Jpeg and the new Jpeg, it will keep writing into the Jpeg until it encounters that next Jpeg, which would corrupt the current Jpeg file

