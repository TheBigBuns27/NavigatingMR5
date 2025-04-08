import pandas as pd

def setDf():
    roomAssignments = pd.read_excel("https://raw.githubusercontent.com/TheBigBuns27/NavigatingMR5/main/ENGR1020/MR5 Room Number Assignments.xlsx")
    roomAssignments.set_index("Room Number", inplace=True, drop=True)
    roomAssignments.index.name = None
    return roomAssignments

def roomNums():
    roomNums = list(setDf().index)
    roomNums.insert(0, "BLANK")
    return roomNums

def locations():
    locations = list(setDf()["Location Name"])
    locations.insert(0, "BLANK")
    return locations
