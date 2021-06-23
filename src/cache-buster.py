from File import generateNames
from File import regenerateFile
from File import getVersion
from MyParser import MyParser
import fnmatch
import os

print("Initializing html parser.")
parser = MyParser()
print("Reading configuration file.")
if not parser.getConfig():
    print("Starting failed!!!")
    exit()

version = parser.version

print("Found configuration.")
print("Domain: " + parser.domainName)
print("Web directory: " + parser.webDir)
print("Version: " + parser.version)
print("Looking for html files.")

matches = []
for root, dirnames, filenames in os.walk(parser.webDir):
    for filename in fnmatch.filter(filenames, '*.html'):
        matches.append(os.path.join(root, filename))

if len(matches) == 0:
    print("No available files. Cancelling...")
    exit()

print("Number of files found: " + len(matches))
print("Listing files...")
for match in matches:
    print(match)

for file in matches:
    print("Parsing: " + file)
    data = parser.parseFile(file)
    links = parser.findTags(data, "link")

    fileList = parser.extractFiles(links)
    newFiles = generateNames(list(fileList), version)

    for index in range(0, len(newFiles)):
        if not os.path.isfile(newFiles[index]):
            os.rename(fileList[index], newFiles[index])
        parser.generateTag(data, newFiles[index])

    data = parser.strip(data)

    regenerateFile(file, data) 