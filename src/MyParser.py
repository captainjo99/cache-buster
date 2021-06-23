from bs4 import BeautifulSoup
import os

class MyParser:
    configPath = "./src/"

    def __init__(self):
        self.domainName = ""
        self.webDir = ""

    def parseFile(self, file):
        fp = open(file, "r+")
        data = BeautifulSoup(fp, "html.parser")
        fp.close()
        return data

    def findTags(self, data, tag):
        tags = data.find_all(tag)
        return tags

    def extractFiles(self, linkList):
        fileList = []
        for link in linkList:
            if str(link["rel"]) == "['stylesheet']" and str(link["href"]).startswith(self.domainName):
                fileList.append(self.webDir + str(link["href"]).replace(self.domainName, ""))
                link.decompose()
        return fileList

    def generateTag(self, data, file):
        newTag = data.new_tag("link", href=self.domainName + file.replace(self.webDir, ""), rel="stylesheet")
        data.head.append(newTag)
        data.head.append('\n')
        return newTag

    def strip(self, data):
        data = BeautifulSoup(os.linesep.join([s for s in str(data).splitlines() if s]), "html.parser")
        return data

    #Read configuration file, returns true if reading was successful, false otherwise
    def getConfig(self):
        try:
            confFile = open(self.configPath + "buster.conf", 'r')
            data = BeautifulSoup(confFile, "html.parser")
            confFile.close()
        except:
            print("Unable to open configuration file")
            return False
        self.domainName = data.domain.text
        self.webDir = data.webdir.text
        return True