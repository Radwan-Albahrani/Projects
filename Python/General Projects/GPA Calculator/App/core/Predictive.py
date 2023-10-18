import time
import pandas as pd
import logging
from cs50 import get_int, get_float
from tqdm import tqdm
from itertools import repeat
from sympy.utilities.iterables import multiset_combinations, multiset_permutations
from ..utils.utils import CalculateGPA, OpenDatabase
from ..public.variables import path


# Disable requests logging
logging.disable(logging.CRITICAL)


# Predict GPA scores
def PredictiveSetup():
    maxSubjects = 7

    # Get Total points and total hours from the GPA function
    totalPoints, totalHours = CalculateGPA(1)

    # If no scores found
    if totalHours == -1:
        return -1

    # Print out Current GPA
    currentGPA = round(totalPoints / totalHours, 3)
    print(f"Current GPA: {currentGPA}")

    # Get number of subjects
    subjects = get_int("How many subjects are you taking this Term: ")

    # Confirm Maximum subjects with user
    if subjects > maxSubjects:
        predictContinue = input(
            "Too many subjects to predict. This function will only tell you the maximum GPA. Do you want to continue? (y/n): "
        )
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
    maximumGPA = round(maxPoints / totalHours, 3)
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
        scores.append(
            {
                "name": subjectName,
                "SubjectNumber": subjectCounter,
                "credit": currentCredit,
            }
        )

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
    GPAconvert = {
        5.00: "A+",
        4.75: "A ",
        4.50: "B+",
        4.00: "B ",
        3.50: "C+",
        3.00: "C ",
        2.50: "D+",
        2.00: "D ",
        1.00: "F ",
    }

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

        donePermutations = {}

        # Loop through All permutations
        for combination in tqdm(allPossible, leave=False):
            # Get all Permutations
            All = multiset_permutations(combination, len(combination))

            # Loop through them and adjust scores to that permutation
            for permutation in All:
                for index in range(len(permutation)):
                    scores[index]["RawScore"] = permutation[index]
                    scores[index]["LetterGrade"] = GPAconvert[permutation[index]]

                # Combine all equivalent credit hour permutations
                credit_dict = {}
                for score in scores:
                    if score["credit"] in credit_dict.keys():
                        credit_dict[score["credit"]].append(score["LetterGrade"])
                    else:
                        credit_dict[score["credit"]] = [score["LetterGrade"]]

                # Sort all values
                for key, value in credit_dict.items():
                    credit_dict[key] = sorted(value)

                # Check if this equivalent permutation has been done before
                doneBefore = {}
                for key, value in credit_dict.items():
                    if key in donePermutations.keys():
                        if value in donePermutations[key]:
                            if doneBefore.get(key) is None:
                                doneBefore[key] = 1
                            else:
                                doneBefore[key] += 1
                        else:
                            donePermutations[key].append(value)
                    else:
                        donePermutations[key] = [value]

                # Check if this specific combination of credit hours has been done before
                if len(donePermutations.keys()) > 1 and "combined" in donePermutations.keys():
                    if credit_dict in donePermutations["combined"]:
                        doneBefore["combined"] = doneBefore.get("combined", 0) + 1
                    else:
                        donePermutations["combined"].append(credit_dict)
                else:
                    donePermutations["combined"] = [credit_dict]

                # if it has been done before, skip it
                if len(doneBefore.keys()) == len(donePermutations.keys()):
                    continue

                # Calculate GPA for the specified raw scores and letter grades
                tempPoints = 0
                for i in range(len(scores)):
                    # Get appropriate credit hour for raw score
                    credit = scores[i]["credit"]
                    raw = scores[i]["RawScore"]

                    # Calculate points and add it to total points
                    tempPoints += raw * credit

                # Get the current loop GPA
                loopGPA = round((totalPoints + tempPoints) / totalHours, 3)

                # If GPA is higher than expected and no equivalent permutation has been done before, add it to permutations
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
    lowestCredit = min(scores, key=lambda x: x["credit"])
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
