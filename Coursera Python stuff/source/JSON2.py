import json
import urllib

endpoint = "http://python-data.dr-chuck.net/geojson?"



while True:
    searchLocation = raw_input("Enter search location:")
    requestURL = endpoint + urllib.urlencode({'sensor':'false','address':searchLocation})
    rawJSON = urllib.urlopen(requestURL).read()
    print "retrieved ",len(rawJSON)," characters"
    print "from ",requestURL
    
    try:parsedJSON = json.loads(str(rawJSON))
    except: js = None
    if 'status' not in parsedJSON or parsedJSON['status'] != 'OK':
        print 'Failure to retrieve'
        #print json.dumps(parsedJSON,indent=4)
        print parsedJSON
        break
    else:
        break

#print json.dumps(parsedJSON,indent=4)
print parsedJSON["results"][0]["place_id"]