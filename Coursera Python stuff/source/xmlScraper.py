import urllib
import xml.etree.ElementTree as ET

#inputFile = file.open('C:\Users\Evan\Documents\Work\Coursera\Python\comments_42.xml')
#$inputFile = 'C:\Users\Evan\Documents\Work\Coursera\Python\comments_306120.xml'

inputURL = raw_input('Enter location:')
inputURLHandler = urllib.urlopen(inputURL)
inputData = inputURLHandler.read()
tree = ET.fromstring(inputData)

counts = tree.findall('.//count')
runningTotal = 0
for tag in counts :
    runningTotal += int(tag.text)
    
print runningTotal