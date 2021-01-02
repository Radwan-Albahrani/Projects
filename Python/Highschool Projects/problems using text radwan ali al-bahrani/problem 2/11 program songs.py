#importing everything needed

import os

#opening the file and closing it

f = open(r"sayings.txt","w")
f.close()

#confirming that there are 99 bottles

c = 10

#using a while loop to spit out stuff

while c>=0:
    f = open(r"sayings.txt","a")

#first writing but it is looping

    f.write(str(c) + " bottles of saudi champagne on the wall\n")
    f.close()

#decreminting the amount of bottles
    
    c = c-1
    if c == 0:
        f = open(r"sayings.txt","a")
        f.write("No more bottles of saudi champagne on the wall")
        f.close()
        break

    

