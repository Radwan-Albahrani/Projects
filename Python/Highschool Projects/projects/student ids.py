# This program will assign you a record
# First ask the user for his 5-digit student id
# If the student id has 2 letters and 3 numbers in that order, move on
# Then ask the user for his 4-digit year of birth.
# If its 4-digits, move on
# Then calculate the age of the user by using his year of birth
# After all checks, organize the list according to the to:
# Student id in records, year of birth in yob, and age in age.
# Keep asking infintely for inputs
# If the user types: print, allow him to choose which record to print.
# Make sure that the number he puts is actually a record.
# If its not a record, ask him again
# Make sure that the number of records is shown
# Add every record to a forrecord list


forrecords = [""]
records = [""]
yob = [""]
age = [""]
y = 0
letters = ["Q","W","E","R","T","Y","U","I","O","P","A","S","D","F","G","H","J","K","L","Z","X","C","V","B","N","M","q","w","e","r","t","y","u","i","o","p","a","s","d","f","g","h","j","k","l","z","x","c","v","b","n","m"]
numbers = ["1","2","3","4","5","6","7","8","9","0"]

while True:
    a = 0   

    student_id = input("Enter your 5-digit Student ID,(To print a record, type: print): ")
    if student_id == "print" or student_id == "Print":
        
        
        parsed = False
        while not parsed:
            try:
                printer = int(input("Enter a record number to print it(Must be a number), you have " + str(y) + " records: "))
                parsed = True 
            except ValueError:
                print ("Please make sure its a number.")
        
        a = a + int(printer)
        
        if int(printer) > y:
            print("Student not found")

        else:
            print("Student id: "+ str(records[a]) + ". " + "year of birth: " + str(yob[a]) + ". " + "age: " + str(age[a]))
            
            
            

    else:
        if len(student_id) == 5 and student_id[0] in letters and student_id[1] in letters and student_id[2] in numbers and student_id[3] in numbers and student_id[4] in numbers:
            
            print("Student Id Confirmed.")     
            yearofbirth = input("Enter your 4-digit year of birth: ")
            if len(yearofbirth) == 4 and yearofbirth[0] in numbers and yearofbirth[1] in numbers and yearofbirth[2] in numbers and yearofbirth[3] in numbers:
                print("Your information have been recorded.")
                y = y + 1
                records.append(student_id)
                yob.append(yearofbirth)
                sage = 2015 - int(yearofbirth)
                age.append(sage)
            else:
                print("Please retry, invalid length, or invalid date.")
        else:
            print("please retry, must have 2 letters at the begining, 3 numbers at the end.")


for x in records:
    if x in records:
        forrecords.append(x)



        
