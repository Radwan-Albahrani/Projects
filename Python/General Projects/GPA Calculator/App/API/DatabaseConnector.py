# Imports
import time
import sqlite3
import pandas as pd
import sqlite3
import requests
import csv

from tqdm import tqdm
from cs50 import get_float, get_int
from ..utils.utils import CalculateGPA, GetScore, OpenDatabase
from ..public.variables import path, changeModified
from pwinput import pwinput
from python_translator import Translator
from bs4 import BeautifulSoup
from urllib3.exceptions import InsecureRequestWarning

# Disable Insecure Request Warning
requests.packages.urllib3.disable_warnings(InsecureRequestWarning)


# Function to add a course to the database
def AddCourse():
    # Get number of courses to add
    counter = get_int("How many courses do you want to add: ")

    # Prepare a list of courses
    courseList = []

    # Start with first course.
    courseNo = 1

    # Start a loop
    while counter > 0:

        # Get first course information (code, name, grade, and credit hours)
        courseCode = input(
            f"Enter Course [code] for course Number {courseNo}: ").upper()
        courseName = input(
            f"Enter Course [name] for course Number {courseNo}: ")

        # Loop
        while True:
            # Ask user for grade
            courseGrade = input(
                f"Enter Course [grade] in (Letter or percentage) for course number {courseNo}: ")

            # Validate grade with function
            courseGrade = GetScore(courseGrade)

            # if invalidated, keep looping. Else break.
            if courseGrade == -1:
                print("Grade entered is invalid, try again.")
                continue
            else:
                break

        courseCredit = get_float(
            f"Enter [Credit hours] for course Number {courseNo}: ")

        # Append course to course list to add to database later
        courseList.append([courseCode, courseName, courseGrade, courseCredit])

        # Do necessary increment and decrement for loop.
        courseNo += 1
        counter -= 1

    # Open the database
    db = OpenDatabase()

    # Add courses to database from the course list.
    for i in range(len(courseList)):
        print(f"Adding course: {courseList[i]}")
        db.execute("INSERT INTO grades VALUES(?)", courseList[i])
        changeModified(True)

    # Notify User after done.
    print("All Courses Added Successfully.")
    time.sleep(1)


# Function to remove a course from the database
def DeleteCourse():
    # Ask User for Course name
    courseName = input("Enter course Name: ")

    # Open the database
    db = OpenDatabase()

    # Select the course
    checkNew = SelectCourse(courseName)

    # If check passed and a course was returned continue, otherwise don't.
    if checkNew != 0:
        answer = input("Are you sure you want to delete this course? (y/n) ")

        # If confirmed, delete it and notify user
        if answer == "y" or answer == "Y":
            final = db.execute(
                "DELETE FROM grades WHERE name = ?", checkNew[0]["name"])
            if final != 0:
                print(f"{checkNew} Successfully Deleted")
                changeModified(True)
                time.sleep(1)
            else:
                print("Error. No Course Found.")
        # If no, Cancel action, go back to main.
        else:
            print("Action Cancelled")
            time.sleep(1)


# Function to Modify score of inputted data in database
def ModifyCourse():
    # Ask User for Course name
    courseName = input("Enter course Name: ")

    # Open the database
    db = OpenDatabase()

    # Select the course
    selectedCourse = SelectCourse(courseName)
    if selectedCourse != 0:
        # Check with the user if the correct course has been selected
        answer = input("Is this the course you want to modify? (y/n): ")

        # If it is
        if answer.lower() == "y":
            courseName = selectedCourse[0]["name"]
            while True:
                CourseInformation = pd.Series(selectedCourse[0])
                print("\n" + str(pd.DataFrame(CourseInformation).transpose()) + "\n\n")
                # Present New Menu
                print("1. Modify Course Code.")
                print("2. Modify Name.")
                print("3. Modify Score.")
                print("4. Modify Credit Hours.")
                print("5. Back to Main Menu.")

                response = get_int("Choice: ")

                match response:
                    # This case to modify the code of the course
                    case 1:
                        # Get the code and make sure its upper case
                        newCode = input("Enter New Course Code: ").upper()

                        # Try to add it to database
                        final = db.execute(
                            "UPDATE grades SET code = ? WHERE name = ?", newCode, selectedCourse[0]["name"])

                        # If modified successfully, inform user.
                        if final != 0:
                            print(
                                f"{courseName} Successfully Updated. New Code: {newCode}")
                            selectedCourse[0]["code"] = newCode
                            time.sleep(1)
                        else:
                            print("Error: No course found.")
                    # This case to modify the name of the course
                    case 2:
                        # Get the name from the user
                        newName = input("Enter New Course Name: ")

                        # Try to add it to database
                        final = db.execute(
                            "UPDATE grades SET name = ? WHERE name = ?", newName, selectedCourse[0]["name"])

                        # If modified successfully, inform user.
                        if final != 0:
                            print(
                                f"{courseName} Successfully Updated. New Name: {newName}")
                            selectedCourse[0]["name"] = newName
                            time.sleep(1)
                        else:
                            print("Error: No course found.")
                    # This case to modify the score of the course
                    case 3:
                        # While it has not been received
                        while True:
                            # Get a score from the user
                            newScore = input(
                                "Enter new score in letter or percentage: ")

                            # Get the accurate score from the function
                            newScore = GetScore(newScore)

                            # If score found, add it to database and exit loop
                            if newScore == -1:
                                print("Score invalid, Try again.")
                                continue
                            else:
                                break

                        # Once score is correct, update database if possible
                        final = db.execute(
                            "UPDATE grades SET score = ? WHERE name = ?", newScore, selectedCourse[0]["name"])
                        if final != 0:
                            print(
                                f"{courseName} Successfully Updated. New score: {newScore}")
                            selectedCourse[0]["score"] = newScore
                            changeModified(True)
                            time.sleep(1)
                        else:
                            print("Error: No course found.")
                    # This case to modify the credit of the course
                    case 4:
                        # Get the new Credit
                        newCredit = get_int("Enter New Course Credit: ")

                        # Try to add it to database
                        final = db.execute(
                            "UPDATE grades SET credit = ? WHERE name = ?", newCredit, selectedCourse[0]["name"])

                        # If modified successfully, inform user.
                        if final != 0:
                            print(
                                f"{courseName} Successfully Updated. New Credit: {newCredit}")
                            selectedCourse[0]["credit"] = newCredit
                            changeModified(True)
                            time.sleep(1)
                        else:
                            print("Error: No course found.")
                    case 5:
                        break
        else:
            print("Action Cancelled.")
            time.sleep(1)


# Function to display Database
def DisplayDatabase():
    # Open Database to make sure its created Properly
    OpenDatabase()

    # Connect to database with normal sqlite3
    conn = sqlite3.connect(path + '/grades.db')

    # Store Database into dataFrame
    df = pd.read_sql_query("SELECT * FROM grades", conn)

    # Change score to letter grade
    if df.empty:
        print("No courses Found. Add courses to database to view them.")
        time.sleep(2)
        return -1
    df = ChangeScores(df)

    # Print out dataFrame
    print(df)

    # Get Total points and total hours from the GPA function and calculate GPA
    totalPoints, totalHours = CalculateGPA(1)
    GPA = round(totalPoints/totalHours, 3)

    # Print GPA and Total Hours
    print(f"\n\nTotal hours: {totalHours}\nGPA: {GPA}")

    # Sleep for a bit so user can view.
    time.sleep(5)


# change the scores of a dataFrame
def ChangeScores(df: pd.DataFrame):
    # Dictionary to convert to letters
    GPAconvert = {(95, 100): "A+", (90, 95): "A ", (85, 90): "B+", (80, 85): "B ",
                  (75, 80): "C+", (70, 75): "C ", (65, 70): "D+", (60, 65): "D ", (0, 60): "F "}

    # Loop over the DataFrame
    for index, row in df.iterrows():
        # Get the score
        score = row["score"]
        # IF score is 100, A+ and next loop
        if score == 100:
            df.loc[index, "score"] = "A+"
            continue

        # Loop through keys to determine where the grade lies. Then append the corresponding Letter grade
        for keys, values in GPAconvert.items():
            if score >= keys[0] and score < keys[1]:
                df.loc[index, "score"] = values
                break
    # Return the modified DataFrame
    return df


# Function to select specific course from database
def SelectCourse(courseName):
    # Open Database
    db = OpenDatabase()

    # Check if the course name is available
    check = db.execute(
        "SELECT * FROM grades WHERE name LIKE ?", f"%{courseName}%")

    # If multiple courses found:
    if len(check) > 1:
        # Print the courses found
        # Connect to database
        conn = sqlite3.connect(path + '/grades.db')

        # Print database using Pandas so its clean
        print("Courses Selected: \n" + str(pd.read_sql_query(
            f"SELECT * FROM grades WHERE name LIKE '%{courseName}%'", conn)))

        # Start a loop
        while True:
            # Ask user to select a course by code.
            courseCode = input(
                "Please Select one of the courses by typing its code: ")

            # Check if code is found, and if it is, select it and put it into a new list
            for i in range(len(check)):
                if courseCode.upper() in check[i]["code"]:
                    checkNew = []
                    checkNew.append(check[i])
                    break
                else:
                    checkNew = []

            # Notify User that the course is found, then exit loop.
            if len(checkNew) == 1:
                print("\n\nCourse Found: \n" + str(pd.DataFrame(checkNew)))
                return checkNew

            # if not found, tell user its not found, then loop.
            else:
                print("Course Not found, Try again.")
                time.sleep(2)
                return 0
    # If No courses were found from the query, tell user, then go back to main.
    elif len(check) == 0:
        print("Course Not Found.")
        time.sleep(1)
        return 0

    # If only one course is found:
    else:
        checkNew = check
        # Select course and print it.
        # Connect to database
        conn = sqlite3.connect(path + '/grades.db')
        # Print database using Pandas so its clean
        print("Courses Selected: \n" + str(pd.read_sql_query(
            f"SELECT * FROM grades WHERE name LIKE '%{courseName}%'", conn)))
        return checkNew


# Function to get Data from IAU Website
def DataExtractor():

    # Needed URLs
    loginUrl = "https://sis.iau.edu.sa/psp/ps/?cmd=login&languageCd=ENG&"
    returnURl = "https://sis.iau.edu.sa/psc/ps_6/EMPLOYEE/SA/c/SSR_STUDENT_ACAD_REC_FL.SSR_CRSE_HIST_FL.GBL"

    # Get Username and Password From User:
    username = input("Enter your Username: ")
    password = pwinput(prompt="Enter your Password: ")

    # Prepare login Form Data
    formData = {
        "userid": username,
        "pwd": password
    }

    # Send in request and get to appropriate page for grades
    try:
        with requests.session() as s:
            s.post(loginUrl, data=formData)
            r = s.get(returnURl)
            f = BeautifulSoup(r.content, "html.parser")
            if "Oracle PeopleSoft" in f.prettify():
                print("Login Failed. Ensure you have the correct Username and Password.")
                return -1
    except Exception as e:
        print("Certificate Verification Failed. This is an issue from the University Website. Request Will be made without SSL verification. \n\nFind out More here: https://www.sslshopper.com/ssl-checker.html#hostname=https://sis.iau.edu.sa/psp/hcs9prd/EMPLOYEE/SA/?&cmd=login&languageCd=ENG\nMaking Request....")
        with requests.session() as s:
            s.post(loginUrl, data=formData, verify=False)
            r = s.get(returnURl)
            f = BeautifulSoup(r.content, "html.parser")
            if "Oracle PeopleSoft" in f.prettify():
                print("Login Failed. Ensure you have the correct Username and Password.")
                return -1

    # Remove any HTML
    text = f.getText()
    # break into lines and remove leading and trailing space on each
    lines = (line.strip() for line in text.splitlines())
    # break multi-headlines into a line each
    chunks = (phrase.strip() for line in lines for phrase in line.split("  "))
    # drop blank lines
    text = '\n'.join(chunk for chunk in chunks if chunk)

    # Create a list from the text
    startList = list(text.split("\n"))

    # Final list Variable
    finalList = []

    # Loop through list and add any Taken courses, except for courses that have IP as a grade
    translator = Translator()
    for i in tqdm(range(len(startList)), leave=False):
        if startList[i] == "Taken":
            if startList[i-2] == "IP" or startList[i-2] == "NP" or startList[i-2] == "NF" or startList[i-2] == "W":
                continue

            # Get the subject
            subject = startList[i-4]

            # If it is not english, Try to translate it
            if not subject.isascii():
                try:
                    subject = translator.translate(
                        subject, target_language="en", source_language="ar")
                    if subject == None:
                        subject = startList[i-4]
                        print(
                            f"Could not translate subject: {subject}. Using Original Name.")

                # If Error in translation, just add it normally.
                except Exception as e:
                    subject = startList[i-4]
                    print(
                        f"Could not translate subject: {subject}. Using Original Name.")

            # Append to final list
            finalList.append(startList[i-5] + "," + str(subject) + "," +
                             str(GetScore(startList[i-2])) + "," + startList[i-1])

    # Create CSV file
    with open(path + "/Grades.csv", "w", encoding="utf8") as file:
        file.write("code,name,score,credit\n")
        for i in finalList:
            file.write(i)
            file.write("\n")

    # Empty the DB file
    with open(path + "/grades.db", "w") as file:
        pass
    # Create new DB file
    OpenDatabase()

    # Mark as Modified
    changeModified(True)
    # Tell user
    print("Data Extracted Successfully")
    time.sleep(2)


# Exit Routine
def exitRoutine():
    # Open Database
    db = OpenDatabase()

    # Open New CSV file
    with open(path + "/Grades.csv", "w", newline='', encoding="utf8") as file:
        # Connect a writer
        writer = csv.writer(file)

        # Write the header
        writer.writerow(["code", "name", "score", "credit"])

        # Select everything from database
        data = db.execute("SELECT * FROM grades")

        # Write it into CSV file
        for i in data:
            writer.writerow(i.values())
