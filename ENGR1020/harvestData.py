import pandas as pd

def setDf():
    roomAssignments = pd.read_excel("ENGR1020/rooms.xlsx")
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

def convertRoomToInt(room):
    df = setDf()
    roomNum = str(df.loc[df['Location Name'] == room].index.tolist()[0])
    return roomNum
