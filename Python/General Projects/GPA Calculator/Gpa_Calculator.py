import logging
import os
import os
import csv
import time
import pandas
import requests
import logging
import sys
import cs50
import tqdm
import itertools
import sympy
import pwinput
from App import Main

if __name__ == "__main__":
    try:
        Main.main()
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
