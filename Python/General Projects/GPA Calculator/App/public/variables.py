import os

# make a global Path Variable
parent_dir = os.getenv("APPDATA")
directory = "GPA Calculator"
path = os.path.join(parent_dir, directory)
try:
    os.mkdir(path)
except FileExistsError:
    pass

# Global Variables
isModified = False
cached = []


def changeModified(value):
    global isModified
    isModified = value


def getModified():
    global isModified
    return isModified


def setCached(newCached):
    global cached
    cached = newCached


def getCached():
    global cached
    return cached
