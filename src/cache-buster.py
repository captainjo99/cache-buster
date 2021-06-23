from File import generateNames
from File import regenerateFile
from File import getVersion
from MyParser import MyParser
import fnmatch
import os

matches = []
for root, dirnames, filenames in os.walk('./'):
    for filename in fnmatch.filter(filenames, '*.html'):
        matches.append(os.path.join(root, filename))

parser = MyParser()
parser.getConfig()

for file in matches:
    data = parser.parseFile(file)
    links = parser.findTags(data, "link")

    fileList = parser.extractFiles(links)
    newFiles = generateNames(list(fileList), getVersion())

    for index in range(0, len(newFiles)):
        if not os.path.isfile(newFiles[index]):
            os.rename(fileList[index], newFiles[index])
        parser.generateTag(data, newFiles[index])

    data = parser.strip(data)

    regenerateFile(file, data) 