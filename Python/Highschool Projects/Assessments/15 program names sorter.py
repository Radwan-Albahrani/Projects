# Create a list for small names.
s_names = []
# Create a list for long name
l_names=[]
# The entry counter
c = 0
# start the while loop
while(c<5):
    # The input
    x = input("Enter a name: ")
    # if the length is short
    if len(x) <= 4:
        # Append it into the short list
        s_names.append(x)
    # if it is not short
    else:
        # Append it to the long list
        l_names.append(x)
    # Add to the counter for entries
    c = c+1
# print the small list
print("Small names are: " + str(s_names))
# print the long list
print("Long names are: " + str(l_names))
    
