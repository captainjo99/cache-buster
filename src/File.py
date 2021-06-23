from datetime import datetime
import os

def getVersion():
    fp = open("./version")
    data = fp.readline()
    fp.close()
    return data

def generateNames(fileList, version):
    #currentDate = datetime.date(datetime.now()).strftime("%Y-%m-%d")
    for index in range(0, len(fileList)):
        if fileList[index].endswith(".css"):
            fileList[index] = fileList[index].split('?', 1)[0].rstrip(".css") + '?' + version + ".css"
    return fileList

def regenerateFile(file, data):
    os.remove(file)
    fp = open(file, 'w')
    fp.write(str(data.prettify()))
    fp.close()
    return