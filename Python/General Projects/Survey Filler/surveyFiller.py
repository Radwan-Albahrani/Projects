from selenium import webdriver
from webdriver_manager.microsoft import EdgeChromiumDriverManager

from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.edge.service import Service as EdgeService
from time import sleep
from pwinput import pwinput
import os
import logging

logging.disable(logging.CRITICAL)
def programRoutine():
    try:
        options = webdriver.EdgeOptions()
        options.add_argument('headless')
        options.add_argument('--disable-logging')
        options.add_argument('--log-level=1')
        browser = webdriver.Edge(service=EdgeService(
            EdgeChromiumDriverManager().install()), options=options)
    except Exception as e:
        print("Please install or update Edge Chromium from this link: https://www.microsoft.com/en-us/edge")
        sleep(3)
        raise e


    browser.get('https://estibana.iau.edu.sa/')

    username = input("Enter your Username: ")
    password = pwinput("Enter your Password: ")
    browser.find_element(By.ID, 'userNameInput').send_keys(username)
    browser.find_element(By.ID, 'passwordInput').send_keys(password)
    browser.find_element(By.ID, 'submitButton').click()

    try:
        browser.find_element(
            By.XPATH, "/html/body/form/div[5]/header/div/div[3]/ul/li[1]")
        print("Successfully logged in")
    except:
        print("Login Failed. Try again.")
        sleep(2)
        exit(1)
    while True:
        speedup = input("Would you like to speed up the process? (y/n): ")
        score = 0
        if speedup == 'y':
            while True:
                score = input(
                    "How would you like to rate All courses and Instructors: ")
                if int(score) < 1 or int(score) > 5:
                    print("Please enter a valid score")
                    continue
                else:
                    break
            break
        elif speedup == 'n':
            score = 0
            break
        else:
            print("Please enter a valid input")
    while True:
        try:
            browser.find_element(
                By.ID, f'cphMainContent_gvCesSurveysToFill_lbnCourseName_0').click()
            sleep(0.1)
            title = browser.find_element(
                By.ID, 'cphMainContent_lblCourseTitle').text
            if speedup == 'n':
                print(f"The course title is: {title}")
                while True:
                    score = input("How would you like to rate this course: ")
                    if score < 1 or score > 5:
                        print("Please enter a valid score")
                        continue
                    else:
                        break
            allInputs = browser.find_elements(By.TAG_NAME, 'input')
            for i in allInputs:
                try:
                    if i.get_attribute('type') == 'text':
                        i.send_keys(score)
                except Exception as e:
                    continue
            browser.find_element(By.ID, 'a_next').click()
            sleep(1)
            allInputs = browser.find_elements(By.TAG_NAME, 'input')
            for i in allInputs:
                try:
                    if i.get_attribute('type') == 'text':
                        i.send_keys(score)
                except Exception as e:
                    continue
            browser.find_element(By.ID, 'cphMainContent_lbnSubmitCES').click()
            sleep(0.1)
        except Exception as e:
            print("Done With Courses!")
            break

    while True:
        try:
            browser.find_element(
                By.ID, f'cphMainContent_gvSSLSSurveysToFill_lbnTeacher_0').click()
            sleep(1)
            title = browser.find_element(By.ID, 'cphMainContent_lblFaculty').text
            if speedup == "n":
                print(f"The Instructor is: {title}")
                score = input("How would you like to rate this Instructor: ")
                while True:
                    score = input("How would you like to rate this course: ")
                    if score < 1 or score > 5:
                        print("Please enter a valid score")
                        continue
                    else:
                        break
            allInputs = browser.find_elements(By.TAG_NAME, 'input')
            for i in allInputs:
                try:
                    if i.get_attribute('type') == 'text':
                        i.send_keys(score)
                except Exception as e:
                    continue
            browser.find_element(By.ID, 'a_next').click()
            sleep(1)
            allInputs = browser.find_elements(By.TAG_NAME, 'input')
            for i in allInputs:
                try:
                    if i.get_attribute('type') == 'text':
                        i.send_keys(score)
                except Exception as e:
                    continue
            browser.find_element(By.ID, 'cphMainContent_lbnSubmitSSLS').click()
            sleep(1)
        except Exception as e:
            print("Done With Instructors!")
            sleep(2)
            browser.close()
            break

if __name__ == "__main__":
    try:
        programRoutine()
    except Exception as e:
        try:
            sleep(0.1)
            os.mkdir("CrashLog")
        except FileExistsError:
            pass
        logging.disable(logging.NOTSET)
        logging.basicConfig(filename=r"CrashLog/ErrorLog.log", level=logging.DEBUG,
                            format='%(asctime)s %(levelname)s %(name)s %(message)s', force=True)
        logging.exception(e)
        print("Error has been logged in a file called \"CrashLogs\". Please Send it to creator to fix this crash!")
        sleep(3)