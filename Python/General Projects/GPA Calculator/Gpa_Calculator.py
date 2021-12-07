# Necessary Imports
from cs50 import SQL, get_int, get_float
import os
import csv
import time
import pandas as pd
import sqlite3

# make a global Path Variable
parent_dir = os.getenv("APPDATA")
directory = "GPA Calculator"
path = os.path.join(parent_dir, directory)
try:
    os.mkdir(path)
except FileExistsError:
    pass

# Main Function
def main():
    while True:
        # Ask User for response to continue.
        print("\n\n\nThis program will be responsible for calculating your GPA")
        print("First: Choose an option by inputting a number")
        print("1. Add New Courses.")
        print("2. Remove Course.")
        print("3. Modify Course Score.")
        print("4. View Current Database.")
        print("5. Calculate expected GPA.")
        print("6. Exit.")

        response = get_int("Choice: ")

        # Match statement for the response
        match response:
            # Adding Courses
            case 1:
                AddCourse()
            
            # Deleting Courses
            case 2:
                DeleteCourse()
            
            # Modifying Scores
            case 3:
                ModifyScore()
            
            # Displaying Database
            case 4:
                DisplayDatabase()
            
            # Calculating GPA
            case 5:
                CalculateGPA()
            
            # Exiting Program
            case 6:
                # Open Database
                db = OpenDatabase()

                # Open New CSV file
                with open(path + "/Grades.csv", "w", newline='') as file:
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
            db = SQL("sqlite:///" + path + "/grades.db")
        except RuntimeError:
            open(path + "/grades.db", "w").close()
            db = SQL("sqlite:///" + path + "/grades.db")
        
        # Check if accessed database already has a table.
        answer = db.execute("SELECT COUNT(name) FROM sqlite_master WHERE type='table'")
        answer = answer[0]["COUNT(name)"]
        
        # If database does not have a table, create a table and fill it from the csv file
        if answer != 1:
            db.execute("CREATE TABLE grades (code TEXT, name TEXT, score NUMBER, credit NUMBER)")
            try: 
                with open(path + "/Grades.csv") as file:
                    reader = csv.reader(file)
                    row1 = next(reader)
                    for row in reader:
                        db.execute("INSERT INTO grades VALUES(?)", row)

            except FileNotFoundError:
                # Open New CSV file
                with open(path + "/Grades.csv", "w", newline='') as file:
                    pass
                        
        return db

# Function to add a course to the database
def AddCourse():
    # Course letter converter
    GPAconvertLetters = {("A+", "a+") : 100 , ("A", "a") : 90, ("B+", "b+") : 85, ("B", "b") : 80, ("C+", "c+"): 75, ("C" , "c") : 70, ("D", "d") : 65, ("F", "f") : 0}
    # Get number of courses to add
    counter = get_int("How many courses do you want to add: ")
    
    # Prepare a list of courses
    courselist = []
    
    # Start with first course.
    courseNo = 1
    
    # Start a loop
    while counter > 0:
        
        # Get first course information (code, name, grade, and credit hours)
        coursecode = input(f"Enter Course [code] for course Number {courseNo}: ")
        coursename = input(f"Enter Course [name] for course Number {courseNo}: ")

        # Loop
        while True:
            # Ask user for grade
            coursegrade = input(f"Enter Course [grade] in (Letter or percentage) for course number {courseNo}: ")
            
            # Validate grade with function
            coursegrade = GetScore(coursegrade)

            # if invalidated, keep looping. Else break.
            if coursegrade == -1:
                print("Grade entered is invalid, try again.")
                continue
            else:
                break


        coursecredit = get_float(f"Enter [Credit hours] for course Number {courseNo}: ")

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
    
    # Select the course
    checknew = SelectCourse(coursename)

    # If check passed and a course was returned continue, otherwise don't.
    if checknew != 0:
        answer = input("Are you sure you want to delete this course? (y/n) ")
        
        # If confirmed, delete it and notify user
        if answer == "y" or answer == "Y":
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


def ModifyScore():
    # Ask User for Course name
    coursename = input("Enter course Name: ")
    
    # Open the database
    db = OpenDatabase()
    
    # Select the course
    selectedCourse = SelectCourse(coursename)
    if selectedCourse != 0:

        # Check with the user if the correct course has been selected
        answer = input("Is this the course you want to modify? (y/n): ")
        # If it is
        if answer.lower() == "y":
            # Check if score was received from the function

            # While it has not been received
            while True:
                # Get a score from the user
                newscore = input("Enter new score in letter or percentage: ")
                
                # Get the accurate score from the function
                newscore = GetScore(newscore)

                # If score found, add it to database and exit loop
                if newscore == -1:
                    print("Score invalid, Try again.")
                    continue
                else:
                    break
            # Once score is correct, update database if possible
            final = db.execute("UPDATE grades SET score = ? WHERE name = ?", newscore, selectedCourse[0]["name"])
            if final != 0:
                print(f"{coursename} Successfully Updated. New score: {newscore}")
                time.sleep(1)
            else:
                print("Error: No course found.")
        else:
            print("Action Cancelled.")
            time.sleep(1)


# Function to display Database
def DisplayDatabase():
    # Connect to database with normal sqlite3
    conn = sqlite3.connect(path + '/grades.db')
    
    # Print database using Pandas so its clean
    print(pd.read_sql_query("SELECT * FROM grades", conn))

    # Sleep for a bit so user can view.
    time.sleep(5)

# Function to Calculate GPA
def CalculateGPA():
    # Prepare list of associations
    GPAconvert = {(95, 100) : 5.00 , (90, 95) : 4.75, (85, 90) : 4.50, (80, 85) : 4.00, (75, 80): 3.50, (70 , 75) : 3.00, (60, 70) : 2.50, (0, 60) : 2.00}
    
    # prepare total points and total hours
    totalpoints = 0
    totalhours = 0

    # Start a loop to check if user wants cumulative gpa or term gpa.
    while True:
        # Ask user for input
        question = input("Cumulative score or term score? (1 for [Using Database], 2 for [Manual Input]): ")

        # If user wants cumulative score:
        if question == "1":

            # Call function to open database
            db = OpenDatabase()

            # Get scores from table
            scores = db.execute("SELECT score FROM grades")

            # Get credit hours from table
            credits = db.execute("SELECT credit FROM grades")

            # Get number of subjects
            subjects = get_int("Please input the number of subjects you want to test (0 if already in database): ")

            # Get out of loop.
            break
        
        # if user wants term score:
        elif question == "2":
            # Create empty lists
            scores = []
            credits = []

            # Ask if you want to input previous GPA
            previous = input("Do you want to input your previous GPA? (y/n): ")

            # Get previous GPA data
            while True:
                if previous.lower() == "y":
                    # Get previous and credit
                    currentGPA = get_float("Enter your previous GPA: ")
                    totalCredit = get_int("Enter your total credit hours so far: ")

                    # Add to total points and total credit
                    totalpoints = currentGPA * totalCredit
                    totalhours += totalCredit
                    break
                # If no previous GPA, get out of loop.
                elif previous.lower() == "n":
                    break
                else:
                    print("Invalid input.")
                    continue
            # Get number of subjects
            subjects = get_int("Please input the number of subjects you want to test: ")
            if subjects == 0:
                print("No Subjects Entered")
            # Get out of loop
            break

        # If input was invalid:
        else:
            # Tell user and reloop.
            print("Choice in valid, try again.")
            
    # Prepare list to figure out raw scores.
    rawscores = []

    # Start a subject counter
    subjectcounter = 1

    # While not done with subjects
    while subjects > 0:
        # Get credit and score from user
        currentcredit = get_int(f"Please input credit hours for subject number {subjectcounter}: ")
        
        # loop
        while True:
                # Get a score from the user
                currentscore = input(f"Please input score for subject number {subjectcounter}: ")
                
                # Get the accurate score from the function
                currentscore = GetScore(currentscore)

                # If score found, add it to database and exit loop
                if currentscore == -1:
                    print("Score invalid, Try again.")
                    continue
                else:
                    break


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

        # If the score is 100, just add 5.0 to the scores and reloop
        if score == 100:
            rawscores.append(list(GPAconvert.values())[0])
            continue
        
        # Loop through keys to determine where the grade lies. Then append the corresponding value
        for keys, values in GPAconvert.items():
            if score >= keys[0] and score < keys[1]:
                rawscores.append(values)
                break

    # Loop through as much times as there are raw scores.
    for i in range(len(rawscores)):
        # Get appropriate credit hour for raw score
        credit = credits[i]["credit"]
        
        # Calculate points and add it to total points
        totalpoints += rawscores[i] * credit

        # Add credit hours to total hours.
        totalhours += credit
    
    # Print current GPA
    try:
        print(f"Calculated GPA: {round(totalpoints/totalhours, 3)}")
    except ZeroDivisionError:
        print("No Courses Entered. Try again.")
    time.sleep(1)


def SelectCourse(coursename):
    #Open Database
    db = OpenDatabase()
    
    # Check if the course name is available
    check = db.execute("SELECT * FROM grades WHERE name LIKE ?", f"%{coursename}%")

    # If multiple courses found: 
    if len(check) > 1:
        # Print the courses found
        # Connect to database
        conn = sqlite3.connect(path + '/grades.db')
    
        # Print database using Pandas so its clean
        print("Courses Selected: \n" + str(pd.read_sql_query(f"SELECT * FROM grades WHERE name LIKE '%{coursename}%'", conn)))

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
                return checknew

            # if not found, tell user its not found, then loop.
            else:
                print("Course Not found, Try again.")
                return 0
    # If No courses were found from the query, tell user, then go back to main.
    elif len(check) == 0:
        print("Course Not Found.")
        time.sleep(1)
        return 0

    # If only one course is found:
    else:
        checknew = check
        # Select course and print it.
        # Connect to database
        conn = sqlite3.connect(path + '/grades.db')
        # Print database using Pandas so its clean
        print("Courses Selected: \n" + str(pd.read_sql_query(f"SELECT * FROM grades WHERE name LIKE '%{coursename}%'", conn)))
        return checknew

def GetScore(score):
    # Dictionary to convert score
    GPAconvertLetters = {("A+", "a+") : 100 , ("A", "a") : 90, ("B+", "b+") : 85, ("B", "b") : 80, ("C+", "c+"): 75, ("C" , "c") : 70, ("D", "d") : 65, ("F", "f") : 0}
    
    try:
        # if it passed as a percentage, check it, then return it
        score = float(score)
        # If score is not within score limits, return error code
        if score > 100 or score < 0:
            return -1
        return score
    except ValueError:
        # Convert it directly using the letters convert dictionary if it was not a percentage
        for keys, values in GPAconvertLetters.items():
            if score == keys[0] or score == keys[1]:
                score = values
                return score
    
    # if nothing has been returned thus far, return -1
    return -1

if __name__ == "__main__":
    main()
