import time
import csv
import time

from cs50 import get_int, get_float
from cs50 import SQL
from ..public.variables import path, changeModified, getModified, setCached, getCached


# Function to open database
def OpenDatabase():
    # First, Try to access the grades database. If it does not exist, create a new one and access it.
    try:
        db = SQL("sqlite:///" + path + "/grades.db")
    except RuntimeError:
        open(path + "/grades.db", "w").close()
        db = SQL("sqlite:///" + path + "/grades.db")

    # Check if accessed database already has a table.
    answer = db.execute(
        "SELECT COUNT(name) FROM sqlite_master WHERE type='table'")
    answer = answer[0]["COUNT(name)"]

    # If database does not have a table, create a table and fill it from the csv file
    if answer != 1:
        db.execute(
            "CREATE TABLE grades (code TEXT, name TEXT, score NUMBER, credit NUMBER)")
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


# Function to Calculate GPA
def CalculateGPA(GetGPA=0, manual=0):
    if not getModified() and len(getCached()) > 0:
        return getCached()
    # Prepare list of associations
    GPAconvert = {(95, 100): 5.00, (90, 95): 4.75, (85, 90): 4.50, (80, 85): 4.00,
                  (75, 80): 3.50, (70, 75): 3.00, (65, 70): 2.50, (60, 65): 2.00, (0, 60): 1.00}

    # prepare total points and total hours
    totalPoints = 0
    totalHours = 0

    # If this is calling the function directly
    if GetGPA == 0:
        while True:
            # Ask user for input
            question = input(
                "Cumulative GPA (using Database) or term GPA (Manual Input)? (1 for [Using Database], 2 for [Manual Input]): ")

            # If user wants cumulative score:
            if question == "1":

                # Call function to open database
                db = OpenDatabase()

                # Get scores from table
                scores = db.execute("SELECT score FROM grades")

                # Get credit hours from table
                credits = db.execute("SELECT credit FROM grades")

                # Get number of subjects
                subjects = get_int(
                    "Please input the number of subjects you want to test (0 if already in database): ")

                # Get out of loop.
                break

            # if user wants term score:
            elif question == "2":
                # Create empty lists
                scores = []
                credits = []

                # Ask if you want to input previous GPA
                previous = input(
                    "Do you want to input your previous GPA? (y/n): ")

                # Get previous GPA data
                while True:
                    if previous.lower() == "y":
                        # Get previous and credit
                        currentGPA = get_float("Enter your previous GPA: ")
                        totalCredit = get_int(
                            "Enter your total credit hours so far: ")

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
                subjects = get_int(
                    "Please input the number of subjects you want to test: ")
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
        currentCredit = get_int(
            f"Please input credit hours for subject number {subjectCounter}: ")

        # loop
        while True:
            # Get a score from the user
            currentScore = input(
                f"Please input score for subject number {subjectCounter}: ")

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
        scores.append({'score': currentScore})
        credits.append({'credit': currentCredit})

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
            print(f"Total Hours: {totalHours}\nCalculated GPA: {GPA}")
        time.sleep(1)
        if manual == 0:
            setCached([totalPoints, totalHours])
        changeModified(False)
        return getCached()
    except ZeroDivisionError:
        print("No Courses Found. Try again.")
        time.sleep(1)
        return [-1, -1]


# Function to check and convert score based on if its a letter or a percentage
def GetScore(score):
    # Dictionary to convert score
    GPAconvertLetters = {("A+", "a+"): 100, ("A", "a"): 90, ("B+", "b+"): 85, ("B", "b"): 80,
                         ("C+", "c+"): 75, ("C", "c"): 70, ("D+", "d+"): 68, ("D", "d"): 65,  ("F", "f"): 0}

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
