import requests
import os
import time
import sys

from tqdm import tqdm


# Function to Check for update
def checkForUpdate(currentMessage):
    # Try to get the latest commit and compare the names. Else. Tell the user something is wrong with the internet
    try:
        response = requests.get(
            'https://api.github.com/repos/Radwan-Albahrani/Projects/commits?path=Python/General%20Projects/GPA%20Calculator&%20&page=1').json()
        newMessage = response[0]['commit']['message']
    except Exception as e:
        print(
            "Something went wrong with the update checker. Check your internet connection.")
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
                                   bar_format="{desc}: {percentage:.2f}%|{bar}| {n_fmt}/{total_fmt} {remaining}",
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
