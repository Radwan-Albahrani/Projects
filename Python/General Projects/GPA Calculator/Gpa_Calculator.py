# Necessary Imports
from cs50 import SQL, get_int, get_float
import os
import csv
import time
import pandas as pd
import sqlite3
import requests
import logging
import sys
from bs4 import BeautifulSoup
from pwinput import pwinput
from tqdm import tqdm
from itertools import repeat
from sympy.utilities.iterables import multiset_combinations, multiset_permutations

# Disable requests logging
urllib3_log = logging.getLogger("urllib3")
urllib3_log.setLevel(logging.CRITICAL)

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
    # Check if an update is available
    updateMessage = "Prevented Error when Closing Program"
    checkForUpdate(updateMessage)

    while True:
        # Ask User for response to continue.
        print("\n\n\nThis program will be responsible for calculating your GPA")
        print("First: Choose an option by inputting a number")
        print("1. Add New Courses.")
        print("2. Remove Course.")
        print("3. Modify Course.")
        print("4. View Current Database.")
        print("5. Calculate expected GPA.")
        print("6. Calculate Needed Scores to maintain a GPA.")
        print("7. Get Data from SIS website.")
        print("8. Exit.")

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
                ModifyCourse()
            # Displaying Database
            case 4:
                DisplayDatabase()
            # Calculating GPA
            case 5:
                CalculateGPA()
            # Predictive GPA function
            case 6:
                PredictiveSetup()
            # SIS Gathering
            case 7:
                DataExtractor()
            # Exiting Program
            case 8:
                exitRoutine()
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
                with open(path + "/Grades.csv", encoding="utf8") as file:
                    reader = csv.reader(file)
                    row1 = next(reader)
                    for row in reader:
                        db.execute("INSERT INTO grades VALUES(?)", row)

            except FileNotFoundError:
                # Open New CSV file
                with open(path + "/Grades.csv", "w", newline='', encoding="utf8") as file:
                    pass
                        
        return db

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
        courseCode = input(f"Enter Course [code] for course Number {courseNo}: ").upper()
        courseName = input(f"Enter Course [name] for course Number {courseNo}: ")

        # Loop
        while True:
            # Ask user for grade
            courseGrade = input(f"Enter Course [grade] in (Letter or percentage) for course number {courseNo}: ")
            
            # Validate grade with function
            courseGrade = GetScore(courseGrade)

            # if invalidated, keep looping. Else break.
            if courseGrade == -1:
                print("Grade entered is invalid, try again.")
                continue
            else:
                break


        courseCredit = get_float(f"Enter [Credit hours] for course Number {courseNo}: ")

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
            final = db.execute("DELETE FROM grades WHERE name = ?", checkNew[0]["name"])
            if final != 0:
                print(f"{checkNew} Successfully Deleted")
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
                        final = db.execute("UPDATE grades SET code = ? WHERE name = ?", newCode, selectedCourse[0]["name"])

                        # If modified successfully, inform user.
                        if final != 0:
                            print(f"{courseName} Successfully Updated. New Code: {newCode}")
                            selectedCourse[0]["code"] = newCode
                            time.sleep(1)
                        else:
                            print("Error: No course found.")
                    # This case to modify the name of the course
                    case 2:
                        # Get the name from the user
                        newName = input("Enter New Course Name: ")

                        # Try to add it to database
                        final = db.execute("UPDATE grades SET name = ? WHERE name = ?", newName, selectedCourse[0]["name"])
                        
                        # If modified successfully, inform user.
                        if final != 0:
                            print(f"{courseName} Successfully Updated. New Name: {newName}")
                            selectedCourse[0]["name"] = newName
                            time.sleep(1)
                        else:
                            print("Error: No course found.")
                    # This case to modify the score of the course
                    case 3:
                        # While it has not been received
                        while True:
                            # Get a score from the user
                            newScore = input("Enter new score in letter or percentage: ")
                            
                            # Get the accurate score from the function
                            newScore = GetScore(newScore)

                            # If score found, add it to database and exit loop
                            if newScore == -1:
                                print("Score invalid, Try again.")
                                continue
                            else:
                                break
                        
                        # Once score is correct, update database if possible
                        final = db.execute("UPDATE grades SET score = ? WHERE name = ?", newScore, selectedCourse[0]["name"])
                        if final != 0:
                            print(f"{courseName} Successfully Updated. New score: {newScore}")
                            selectedCourse[0]["score"] = newScore
                            time.sleep(1)
                        else:
                            print("Error: No course found.")
                    # This case to modify the credit of the course
                    case 4:
                        # Get the new Credit
                        newCredit = get_int("Enter New Course Credit: ")
                        
                        # Try to add it to database
                        final = db.execute("UPDATE grades SET credit = ? WHERE name = ?", newCredit, selectedCourse[0]["name"])
                        
                        # If modified successfully, inform user.
                        if final != 0:
                            print(f"{courseName} Successfully Updated. New Credit: {newCredit}")
                            selectedCourse[0]["credit"] = newCredit
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
    df = ChangeScores(df)

    # Print out dataFrame
    print(df)

    # Sleep for a bit so user can view.
    time.sleep(5)

# change the scores of a dataFrame
def ChangeScores(df:pd.DataFrame):
    # Dictionary to convert to letters
    GPAconvert = {(95, 100) : "A+" , (90, 95) : "A ", (85, 90) : "B+", (80, 85) : "B ", (75, 80): "C+", (70 , 75) : "C ", (67, 70) : "D+", (60, 67) : "D ", (0, 60) : "F "}

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

# Function to Calculate GPA
def CalculateGPA(GetGPA = 0):
    # Prepare list of associations
    GPAconvert = {(95, 100) : 5.00 , (90, 95) : 4.75, (85, 90) : 4.50, (80, 85) : 4.00, (75, 80): 3.50, (70 , 75) : 3.00, (60, 70) : 2.50, (0, 60) : 2.00}
    
    # prepare total points and total hours
    totalPoints = 0
    totalHours = 0

    # If this is calling the function directly
    if GetGPA == 0:
        while True:
            # Ask user for input
            question = input("Cumulative GPA (using Database) or term GPA (Manual Input)? (1 for [Using Database], 2 for [Manual Input]): ")

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
                        totalPoints = currentGPA * totalCredit
                        totalHours += totalCredit
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
    # If calling from predictive Function
    else:
        # Call function to open database
        db = OpenDatabase()

        # Get scores from table
        scores = db.execute("SELECT score FROM grades")

        # Get credit hours from table
        credits = db.execute("SELECT credit FROM grades") 
        
        # No Subject
        subjects = 0
    
    # Prepare list to figure out raw scores.
    rawScores = []

    # Start a subject counter
    subjectCounter = 1

    # While not done with subjects
    while subjects > 0:
        # Get credit and score from user
        currentCredit = get_int(f"Please input credit hours for subject number {subjectCounter}: ")
        
        # loop
        while True:
            # Get a score from the user
            currentScore = input(f"Please input score for subject number {subjectCounter}: ")
            
            # Get the accurate score from the function
            currentScore = GetScore(currentScore)

            # If score found, add it to database and exit loop
            if currentScore == -1:
                print("Score invalid, Try again.")
                continue
            else:
                break


        # Increment subject counter
        subjectCounter += 1

        # Append score and credit to their appropriate lists
        scores.append({'score' : currentScore}) 
        credits.append({'credit' : currentCredit})

        # Reduce subjects by 1.
        subjects -= 1
        
    # Loop through scores.
    for score in scores:
        # Get current score.
        score = score["score"]

        # If the score is 100, just add 5.0 to the scores and reloop
        if score == 100:
            rawScores.append(list(GPAconvert.values())[0])
            continue
        
        # Loop through keys to determine where the grade lies. Then append the corresponding value
        for keys, values in GPAconvert.items():
            if score >= keys[0] and score < keys[1]:
                rawScores.append(values)
                break

    # Loop through as much times as there are raw scores.
    for i in range(len(rawScores)):
        # Get appropriate credit hour for raw score
        credit = credits[i]["credit"]
        
        # Calculate points and add it to total points
        totalPoints += rawScores[i] * credit

        # Add credit hours to total hours.
        totalHours += credit
    
    # Print current GPA
    try:
        GPA = round(totalPoints/totalHours, 3)
        if GetGPA == 0:
            print(f"Calculated GPA: {GPA}")
        time.sleep(1)
        return totalPoints, totalHours
    except ZeroDivisionError:
        print("No Courses Found. Try again.")
        time.sleep(1)
        return [-1, -1]
    
# Predict GPA scores
def PredictiveSetup():
    maxSubjects = 7
    
    # Get Total points and total hours from the GPA function
    totalPoints, totalHours = CalculateGPA(1)
    
    # If no scores found
    if totalHours == 0:
        return -1
    
    # Print out Current GPA
    currentGPA = round(totalPoints/totalHours, 3)
    print(f"Current GPA: {currentGPA}")
    
    # Get number of subjects
    subjects = get_int("How many subjects are you taking this Term: ")
    
    # Confirm Maximum subjects with user
    if subjects > maxSubjects:
        predictContinue = input("Too many subjects to predict. This function will only tell you the maximum GPA. Do you want to continue? (y/n): ")
        if predictContinue.lower() != "y":
            return
    if subjects <= 0:
        print("Cannot have negative or no subjects")
        return
    
    scores, totalHours = GetSubjectsPredict(subjects, totalHours)
    
    # Loop through Scores
    maxPoints = totalPoints
    for i in range(len(scores)):
        # Get appropriate credit hour for raw score
        credit = scores[i]["credit"]
        
        # Calculate points and add it to total points
        maxPoints += 5.00 * credit
    
    # Print Maximum GPA
    maximumGPA = round(maxPoints/totalHours, 3)
    print(f"Maximum GPA this term is: {maximumGPA}\n")
    time.sleep(1)
    if subjects > maxSubjects:
        print("Too many Subjects to calculate possibilities.")
        return
    
    # Start the prediction Process
    CalculatePredict(subjects, maximumGPA, scores, totalHours, totalPoints)

# Get subjects for predictive Function
def GetSubjectsPredict(subjects, totalHours):
    names = []
    scores = []
    subjectCounter = 1
    # While not done with subjects
    while subjects > 0:
        # Get Subject Name
        subjectName = input(f"Enter the name of Subject number: {subjectCounter}: ")
        if subjectName not in names:
            names.append(subjectName)
        else:
            print("Name already Added. Try again")
            continue
        
        # Get credit and score from user
        currentCredit = get_int(f"Please input credit hours for {subjectName}: ")
       
        # Append score and credit to their appropriate lists
        scores.append({"name" : subjectName, "SubjectNumber" : subjectCounter, "credit" : currentCredit}) 

        # Add hours
        totalHours += currentCredit

        # Increment subject counter
        subjectCounter += 1

        # Reduce subjects by 1.
        subjects -= 1
    
    return scores, totalHours

# Calculate all Predictions
def CalculatePredict(subjects, maximumGPA, scores, totalHours, totalPoints):
    # Prepare list of associations
    GPAconvert = {5.00 : "A+" , 4.75 : "A ", 4.50 : "B+", 4.00 : "B ", 3.50: "C+", 3.00 : "C ", 2.50 : "D ", 2.00 : "F "}

    # Start a loop to keep the user here until they are done with the function
    expectedGPA = 0
    while expectedGPA != -1:
        # Start a List to keep track of permutations
        permutationsFound = []
        listCounter = 0
        
        # Get expected GPA
        expectedGPA = get_float("What do you want your GPA to be (-1 to go back to menu): ")
        if expectedGPA == -1:
            break
        # If expected is bigger than Maximum
        if expectedGPA > maximumGPA:
            print(f"GPA cannot be achieved as it exceeds the maximum GPA {maximumGPA} which you can get this term.")
            continue
        
        # Get possible GPAs then remove any unnecessary Values
        GPAValues = list(GPAconvert.keys())
        GPAValues = _removeExtra(scores, GPAValues, expectedGPA, totalHours, totalPoints)

        # Repeat and get all possible combinations
        GPAValues = [x for item in GPAValues for x in repeat(item, subjects)]
        allPossible = list(multiset_combinations(GPAValues, subjects))

        # Loop through All permutations
        for combination in tqdm(allPossible, leave=False):
            All = multiset_permutations(combination, len(combination))
            for permutation in All:
                # Set the raw scores and letter grades
                for index in range(len(permutation)):
                    scores[index]["RawScore"] = permutation[index]
                    scores[index]["LetterGrade"] = GPAconvert[permutation[index]]
                
                # Calculate GPA for the specified raw scores and letter grades
                tempPoints = 0
                for i in range(len(scores)):
                    # Get appropriate credit hour for raw score
                    credit = scores[i]["credit"]
                    raw = scores[i]["RawScore"]
                    # Calculate points and add it to total points
                    tempPoints += raw * credit
                loopGPA = round((totalPoints + tempPoints) / totalHours, 3)
                
                # If GPA is higher than expected, add it to permutations
                if loopGPA >= expectedGPA:
                    permutationsFound.append({})
                    for score in scores:
                        permutationsFound[listCounter][score["name"]] = score["LetterGrade"] 
                    permutationsFound[listCounter]["GPA"] = loopGPA
                    listCounter += 1
            
        # Prepare Printable
        print("Possible Grades to achieve the GPA: ")
        printableData = pd.DataFrame(permutationsFound)
        printableData = printableData.sort_values("GPA")
        printableData = printableData.reset_index(drop=True)
        print(printableData.loc[printableData["GPA"] == printableData["GPA"][0]])

# Remove unnecessary values in GPA prediction
def _removeExtra(scores, GPAValues, expectedGPA, totalHours, totalPoints):
    # Get the lowest Credit
    lowestCredit = min(scores, key=lambda x:x['credit'])
    lowestCredit = lowestCredit["credit"]
    
    # Get total points
    minPoints = totalPoints
    passedLowest = False

    # Assume everything else is A+ except for the lowest Credit
    for i in range(len(scores)):
        credit = scores[i]["credit"]
        if credit == lowestCredit and not passedLowest:
            passedLowest = True
            continue
        minPoints += credit * 5.00
    
    # Test out lowest credit and once it fails, eliminate everything lower than it
    for index, value in enumerate(GPAValues):
        tempPoints = minPoints
        tempPoints += lowestCredit * value
        tempGPA = round(tempPoints / totalHours, 3)
        if tempGPA < expectedGPA:
            GPAValues = GPAValues[0:index]
            break
    # Return new optimized list
    return GPAValues

# Function to select specific course from database
def SelectCourse(courseName):
    #Open Database
    db = OpenDatabase()
    
    # Check if the course name is available
    check = db.execute("SELECT * FROM grades WHERE name LIKE ?", f"%{courseName}%")

    # If multiple courses found: 
    if len(check) > 1:
        # Print the courses found
        # Connect to database
        conn = sqlite3.connect(path + '/grades.db')
    
        # Print database using Pandas so its clean
        print("Courses Selected: \n" + str(pd.read_sql_query(f"SELECT * FROM grades WHERE name LIKE '%{courseName}%'", conn)))

        # Start a loop
        while True:
            # Ask user to select a course by code.
            courseCode = input("Please Select one of the courses by typing its code: ")
            
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
        print("Courses Selected: \n" + str(pd.read_sql_query(f"SELECT * FROM grades WHERE name LIKE '%{courseName}%'", conn)))
        return checkNew

# Function to check and convert score based on if its a letter or a percentage
def GetScore(score):
    # Dictionary to convert score
    GPAconvertLetters = {("A+", "a+") : 100 , ("A", "a") : 90, ("B+", "b+") : 85, ("B", "b") : 80, ("C+", "c+"): 75, ("C" , "c") : 70, ("D+", "d+") : 68, ("D", "d") : 65,  ("F", "f") : 0}
    
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
            if score in keys:
                score = values
                return score
    
    # if nothing has been returned thus far, return -1
    return -1

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

# Function to Check for update
def checkForUpdate(currentMessage):
    # Try to get the latest commit and compare the names. Else. Tell the user something is wrong with the internet
    try:
        response = requests.get('https://api.github.com/repos/Radwan-Albahrani/Projects/commits?path=Python/General%20Projects/GPA%20Calculator&%20&page=1').json()
        newMessage = response[0]['commit']['message']
    except Exception as e:
        print("Something went wrong with the update checker. Check your internet connection.")
        return 0


    # Check if the commit message matches the coded in message.
    if currentMessage == newMessage:
        print("You are on the latest version!")

    # If it doesn't match, ask if the user wants to update
    else:
        # Get input from user to check if they want to update
        print("New Version has been found.")
        
        # Print out Changes
        print("\nChanges: ")
        
        # In case of duplicate commits
        messageList = []

        # Loop through all changes
        for i in range(len(response)):
            # Get a message
            previousMessage = response[i]["commit"]["message"]
            
            # If its the current Version, Stop
            if previousMessage == currentMessage:
                break

            # If it hasn't been displayed before, Display it
            if previousMessage not in messageList:
                print("\t- ", response[i]["commit"]["message"])
                messageList.append(previousMessage)
        
        update = input("Do you want to Install the new Update? (y/n): ")
        # If they do, get the new file
        if update.lower() == "y":
            url = "https://github.com/JackyXteam/Projects/blob/master/Python/General%20Projects/GPA%20Calculator/Gpa_Calculator.exe?raw=true"
            # Try to get the new file and download it
            try:
                # Get the Download
                download = requests.get(url, stream=True)

                # Get the total Size of the download
                totalSize = float(download.headers["content-length"])

                # Create a new directory to store the download
                os.mkdir("New")
                # Creating Progress Bar
                progressBar = tqdm(total=totalSize, 
                    unit_scale=True, 
                    bar_format = "{desc}: {percentage:.2f}%|{bar}| {n_fmt}/{total_fmt} {remaining}", 
                    desc="Downloading New GPA Calculator")
                # Open a new file in binary
                with open("New/GPA_Calculator.exe", 'wb') as file:
                    # Loop through the download in chunks to create progress bar
                    for data in download.iter_content(chunk_size=1024):
                        # Update Progress Bar
                        progressBar.update(len(data))
                        
                        # Write Data in Chunks
                        file.write(data)
                # Close Progress Bar
                progressBar.close()

                # Tell User the file has been downloaded.
                print("File has been downloaded in \"New\" Directory. Please Use it to replace this current program. This program will close in 5 seconds.")
                time.sleep(5)
                sys.exit()
            
            # Print out any error that occurs.
            except Exception as e:
                print("Hmm. An error has occurred. Maybe check your internet? \n\n")
                print("Error Message: \n" + str(e))

# Function to get Data from IAU Website
def DataExtractor():
    # Needed URLs
    loginUrl = "https://sis.iau.edu.sa/psp/hcs9prd/EMPLOYEE/SA/?&cmd=login&languageCd=ENG"
    returnURl = "https://sis.iau.edu.sa/psc/hcs9prd_60/EMPLOYEE/SA/c/SSR_STUDENT_ACAD_REC_FL.SSR_CRSE_HIST_FL.GBL"

    # Get Username and Password From User:
    username = input("Enter your Username: ")
    password = pwinput(prompt="Enter your Password: ")

    # Prepare login Form Data
    formData = { 
        "userid": username,
        "pwd": password
    }

    # Send in request and get to appropriate page for grades
    with requests.session() as s:
        s.post(loginUrl, data=formData)
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
    for i in range(len(startList)):
        if startList[i] == "Taken":
            if startList[i-2] == "IP" or startList[i-2] == "NP" or startList[i-2] == "NF" or startList[i-2] == "W":
                continue
            finalList.append(startList[i-5] + "," + startList[i-4] + "," + str(GetScore(startList[i-2])) + "," + startList[i-1])

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

    # Tell user
    print("Data Extracted Successfully")
    time.sleep(2)

if __name__ == "__main__":
    try:
        main()
    except Exception as e:
        try:
            time.sleep(0.1)
            os.mkdir("CrashLog")
        except FileExistsError:
            pass
        logging.basicConfig(filename=r"CrashLog/ErrorLog.log", level=logging.DEBUG, format='%(asctime)s %(levelname)s %(name)s %(message)s', force=True)
        logging.exception(e)
        print("Error has been logged in a file called \"CrashLogs\". Please Send it to creator to fix this crash!")
        time.sleep(3)
