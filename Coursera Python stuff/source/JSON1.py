import json
import urllib

url = raw_input('Enter a url- ')

rawJSON = urllib.urlopen(url)

parsedJSON = json.load(rawJSON)

runningTotal = 0
for item in parsedJSON["comments"]:
    #print item
    runningTotal+= item["count"]
    
print runningTotal