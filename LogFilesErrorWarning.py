import re
def logFileExtraction():
    regex = "^(0[1-9]|1[0-2])\/(0[1-9]|1\d|2\d|3[01]) (2[0-3]||0[0-9]|1[0-9]):([0-5][0-9]):([0-5][0-9]) (ERROR|WARNING).*[\n]$"
    f = open("./logfilesPython.txt", "r")
    inputLogList = f.readlines()
    ouputLogList = []
    for y in inputLogList:
        x = re.search(regex, y)
        if x != None and x.start() == 0:
            ouputLogList.append(y)
    outputLog = open("finalLogFile.txt", "x")
    outputLog = open("./finalLogFile.txt", "w")
    for element in ouputLogList:
        outputLog.write(element + "\n")
    outputLog.close()
logFileExtraction()