# Necessary Imports
import logging
import os
import os
import time
import logging
from .core.Predictive import PredictiveSetup
from .core.Updates import checkForUpdate
from .API.DatabaseConnector import *
from cs50 import get_int


# Main Function
def main():
    # Global Variable
    global isModified

    # Check if an update is available
    updateMessage = "Removed Unnecessary Imports"
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
                changeModified(True)
                CalculateGPA(manual=1)
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


if __name__ == "__main__":
    try:
        main()
    except Exception as e:
        try:
            time.sleep(0.1)
            os.mkdir("CrashLog")
        except FileExistsError:
            pass
        logging.disable(logging.NOTSET)
        logging.basicConfig(filename=r"CrashLog/ErrorLog.log", level=logging.DEBUG,
                            format='%(asctime)s %(levelname)s %(name)s %(message)s', force=True)
        logging.exception(e)
        print("Error has been logged in a file called \"CrashLogs\". Please Send it to creator to fix this crash!")
        time.sleep(3)
