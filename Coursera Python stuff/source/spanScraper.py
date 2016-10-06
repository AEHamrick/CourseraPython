import urllib
from BeautifulSoup import *

#url = raw_input('Enter - ')
#html = urllib.urlopen("http://python-data.dr-chuck.net/comments_42.html").read()
html = urllib.urlopen("http://python-data.dr-chuck.net/comments_306123.html").read()

soup = BeautifulSoup(html)

runningTotal = 0
tags = soup('span')
for tag in tags:
    # Look at the parts of a tag
    runningTotal += int(tag.contents[0]) 
    
print runningTotal