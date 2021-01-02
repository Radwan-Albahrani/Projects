# ask the user for his first and last name, store them in a list
# ask the user for his 4-digit year of birth.
# if its not a 4-digit, ask him again
# if it is more then 2000, kick him for being young.
# if it is less then 1920, kick him for being too old.
# if the year of birth is in between 1920 and 2000, store it in a list

fname = []
lname = []
yob = []
while True:   
    fname1 = input("Enter your first name: ")
    lname1 = input("Enter your last name: ") 
    year_of_birth = input("Enter your year of birth: ")
    if len(year_of_birth) == 4:
        if int(year_of_birth) > 2000 or int(year_of_birth) < 1920:
            print("You are too young/old to register.")
            break
        else:
            print("Your data has been added to the Database.")
            break
    else:
        print("invalid length.")
    fname.append(fname1)
    lname.append(lname1)
    yob.append(year_of_birth)
