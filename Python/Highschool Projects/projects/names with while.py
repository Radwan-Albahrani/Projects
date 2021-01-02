fnamelist = []
lnamelist = []

while True:
    s1fname = input("Enter Student 1 first name: ")
    s1lname = input("Enter Student 1 last name: ")
    s2fname = input("Enter Student 2 first name: ")
    s2lname = input("Enter Student 2 last name: ")
    s3fname = input("Enter Student 3 first name: ")
    s3lname = input("Enter Student 3 last name: ")

    fnamelist.append(s1fname)
    fnamelist.append(s2fname)
    fnamelist.append(s3fname)
    lnamelist.append(s1lname)
    lnamelist.append(s2lname)
    lnamelist.append(s3lname)
    

    print("First names: " + fnamelist + " last names: " + lnamelist + ".")

