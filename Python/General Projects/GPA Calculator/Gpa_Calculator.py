# Necessary Imports
from cs50 import SQL, get_int, get_float
import csv
import time
import pandas as pd
import sqlite3

# Main Function
def main():
    while True:
        # Ask User for response to continue.
        print("This program will be responsible for calculating your GPA")
        print("First: Choose an option by inputting a number")
        print("1. Add New Courses.")
        print("2. Remove Course")
        print("3. View Current Database.")
        print("4. Calculate expected GPA.")
        print("5. Exit.")

        response = get_int("Choice: ")

        # If add new Course
        if response == 1:
            AddCourse()
        
        # If delete course
        elif response == 2:
            DeleteCourse()

        #If Display current database
        elif response == 3:
            DisplayDatabase()

        # If Calculating expected GPA
        elif response == 4:
            CalculateGPA()

        # If exiting program.
        elif response == 5:
            # Open Database
            db = OpenDatabase()

            # Open New CSV file
            with open("GPA Calculator/Grades.csv", "w", newline='') as file:
                # Connect a writer
                writer = csv.writer(file)
                
                # Write the header
                writer.writerow(["code", "name", "score", "credit"])
                
                # Select everything from database
                data = db.execute("SELECT * FROM grades")
                
                # Write it into CSV file
                for i in data:
                    writer.writerow(i.values())
            break

# Function to open database
def OpenDatabase():
    # First, Try to access the grades database. If it does not exist, create a new one and access it.
        try: 
            db = SQL("sqlite:///GPA Calculator/grades.db")
        except RuntimeError:
            open("GPA Calculator/grades.db", "w").close()
            db = SQL("sqlite:///GPA Calculator/grades.db")
        
        # Check if accessed database already has a table.
        answer = db.execute("SELECT COUNT(name) FROM sqlite_master WHERE type='table'")
        answer = answer[0]["COUNT(name)"]
        
        # If database does not have a table, create a table and fill it from the csv file
        if answer != 1:
            db.execute("CREATE TABLE grades (code TEXT, name TEXT, score NUMBER, credit NUMBER)")

            with open("GPA Calculator/Grades.csv") as file:
                reader = csv.reader(file)
                row1 = next(reader)
                for row in reader:
                    db.execute("INSERT INTO grades VALUES(?)", row)
        return db

# Function to add a course to the database
def AddCourse():
    # Get number of courses to add
    counter = get_int("How many courses do you want to add: ")
    
    # Prepare a list of courses
    courselist = []
    
    # Start with first course.
    courseNo = 1
    
    # Start a loop
    while counter > 0:
        
        # Get first course information (code, name, grade, and credit hours)
        coursecode = input(f"Enter Course code for course Number {courseNo}: ")
        coursename = input(f"Enter Course name for course Number {courseNo}: ")
        coursegrade = get_float(f"Enter Grade in Percentage for course Number {courseNo}: ")
        coursecredit = get_float(f"Enter Credit hours for course Number {courseNo}: ")

        # Append course to course list to add to database later
        courselist.append([coursecode, coursename, coursegrade, coursecredit])

        # Do necessary increment and decrement for loop.
        courseNo += 1
        counter -= 1

    # Open the database
    db = OpenDatabase()

    # Add courses to database from the course list.
    for i in range(len(courselist)):
        print(f"Adding course: {courselist[i]}")
        db.execute("INSERT INTO grades VALUES(?)", courselist[i])
    
    # Notify User after done.
    print("All Courses Added Successfully.")
    time.sleep(1)

# Function to remove a course from the database
def DeleteCourse():
    # Ask User for Course name
    coursename = input("Enter course Name: ")
    
    # Open the database
    db = OpenDatabase()

    # Check if the course name is available
    check = db.execute("SELECT * FROM grades WHERE name LIKE ?", f"%{coursename}%")

    # If multiple courses found: 
    if len(check) > 1:
        # Print the courses found
        print(f"Course(s) Selected: {check}. ")

        # Start a loop
        while True:
            # Ask user to select a course by code.
            coursecode = input("Please Select one of the courses by typing its code: ")
            
            # Check if code is found, and if it is, select it and put it into a new list
            for i in range(len(check)):
                if coursecode == check[i]["code"]:
                    checknew = []
                    checknew.append(check[i])
                    break
            
            # Notify User that the course is found, then exit loop.
            if len(checknew) == 1:
                print("Course Found.")
                break

            # if not found, tell user its not found, then loop.
            else:
                print("Course Not found, Try again.")
    # If No courses were found from the query, tell user, then go back to main.
    elif len(check) == 0:
        print("Course Not Found.")
        time.sleep(1)

    # If only one course is found:
    else:
        checknew = check
    # Select course and print it.
    print(f"Course Selected: {checknew}")

    # Confirm user intention to delete it
    answer = input("Are you sure you want to delete this course? (y/n) ")
    
    # If confirmed, delete it and notify user
    if answer == "y":
        final = db.execute("DELETE FROM grades WHERE name = ?", checknew[0]["name"])
        if final != 0:
            print(f"{checknew} Successfully Deleted")
            time.sleep(1)
        else:
            print("Error. No Course Found.")
    # If no, Cancel action, go back to main.
    else:
        print("Action Cancelled")
        time.sleep(1)

# Function to display Database
def DisplayDatabase():
    # Connect to database with normal sqlite3
    conn = sqlite3.connect('GPA Calculator/grades.db')
    
    # Print database using Pandas so its clean
    print(pd.read_sql_query("SELECT * FROM grades", conn))

    # Sleep for a bit so user can view.
    time.sleep(5)

# Function to Calculate GPA
def CalculateGPA():
    # Start a loop to check if user wants cumulative gpa or term gpa.
    while True:
        # Ask user for input
        question = input("Cumulative score or term score? (1 for cumulative, 2 for term): ")

        # If user wants cumulative score:
        if question == "1":

            # Call function to open database
            db = OpenDatabase()

            # Get scores from table
            scores = db.execute("SELECT score FROM grades")

            # Get credit hours from table
            credits = db.execute("SELECT credit FROM grades")

            # Get out of loop.
            break
        
        # if user wants term score:
        elif question == "2":
            # Create empty lists
            scores = []
            credits = []

            # Get out of loop
            break

        # If input was invalid:
        else:
            # Tell user and reloop.
            print("Choice in valid, try again.")
            
    # Prepare list to figure out raw scores.
    rawscores = []
    
    # Get how many subjects you want to test
    subjects = get_int("Please input the number of subjects you want to test(0 if already in database): ")

    # Start a subject counter
    subjectcounter = 1

    # While not done with subjects
    while subjects > 0:
        # Get credit and score from user
        currentcredit = get_int(f"Please input credit hours for subject number {subjectcounter}: ")
        currentscore = get_int(f"Please input score for subject number {subjectcounter}: ")

        # Increment subject counter
        subjectcounter += 1

        # Append score and credit to their appropriate lists 
        scores.append({'score' : currentscore})
        credits.append({'credit' : currentcredit})

        # Reduce subjects by 1.
        subjects -= 1
        
    # Loop through scores.
    for score in scores:
        # Get current score.
        score = score["score"]

        # Figure out raw score based on current score. Append appropriate raw score to table. Based on University Standards.
        if score >= 95:
            rawscores.append(5.00)
        elif score >= 90:
            rawscores.append(4.75)
        elif score >= 85:
            rawscores.append(4.50)
        elif score >= 80:
            rawscores.append(4.00)
        elif score >= 75:
            rawscores.append(3.50)
        elif score >= 70:
            rawscores.append(3.00)
        elif score >= 65:
            rawscores.append(2.50)
        elif score >= 60:
            rawscores.append(2.00)
        else:
            rawscores.append(0)
    
    # Prepare total points and total hours for calculation
    totalpoints = 0
    totalhours = 0

    # Loop through as much times as there are raw scores.
    for i in range(len(rawscores)):
        # Get appropriate credit hour for raw score
        credit = credits[i]["credit"]
        
        # Calculate points and add it to total points
        totalpoints += rawscores[i] * credit

        # Add credit hours to total hours.
        totalhours += credit
    
    # Print current GPA
    print(f"Calculated GPA: {round(totalpoints/totalhours, 3)}")
    time.sleep(1)


if __name__ == "__main__":
    main()
