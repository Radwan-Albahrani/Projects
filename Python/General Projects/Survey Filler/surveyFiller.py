# -*- coding: utf-8 -*
from selenium import webdriver
from webdriver_manager.microsoft import EdgeChromiumDriverManager

from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.edge.service import Service as EdgeService
from selenium.webdriver.remote.remote_connection import LOGGER

from time import sleep
from pwinput import pwinput
import os
import logging

logging.disable(logging.CRITICAL)

def programRoutine():
    try:
        options = webdriver.EdgeOptions()
        options.add_argument("--headless=new")
        options.add_argument("--inprivate")
        options.add_argument("--disable-gpu")
        options.add_argument("--log-level=3")
        options.add_argument("--disable-extensions")
        options.add_argument("--window-size=1920,1080")
        options.add_experimental_option("excludeSwitches", ["enable-logging"])
        user_agent = 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/60.0.3112.50 Safari/537.36'
        options.add_argument(f'user-agent={user_agent}')


        browser = webdriver.Edge(options=options)
    except Exception as e:
        print("Please install or update Edge Chromium from this link: https://www.microsoft.com/en-us/edge")
        sleep(3)
        raise e


    browser.get('https://estibana.iau.edu.sa/')
    username = input("Enter your Username: ")
    password = pwinput("Enter your Password: ")
    try:
        browser.find_element(By.ID, 'userNameInput').send_keys(username)
        browser.find_element(By.ID, 'passwordInput').send_keys(password)
        browser.find_element(By.ID, 'submitButton').click()
    except:
        print("Login Failed. This could be an error from the website. Check the screenshot saved in the same directory as this program.")
        browser.get_screenshot_as_file("screenshot.png")
        sleep(2)
        exit(1)

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
                    try:
                        score = int(score)
                    except:
                        print("Please enter a valid score")
                        continue
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
                while True:
                    score = input("How would you like to rate this instructor: ")
                    try:
                        score = int(score)
                    except:
                        print("Please enter a valid score")
                        continue
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
        sleep(1)