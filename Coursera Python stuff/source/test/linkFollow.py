import urllib
from BeautifulSoup import *

#url = raw_input('Enter - ')
#html = urllib.urlopen("http://python-data.dr-chuck.net/comments_42.html").read()


linkPosition = 18
linkDepth = 7
i = 0
#url = "http://python-data.dr-chuck.net/known_by_Fikret.html"
url = "http://python-data.dr-chuck.net/known_by_Walid.html"
while i < linkDepth :
    html = urllib.urlopen(url).read()
    soup = BeautifulSoup(html)
    tags = soup('a')
    #print tags
    #print tags[linkPosition-1].get('href',None)
    print tags[linkPosition-1].contents[0]
    url = tags[linkPosition-1].get('href',None)
    i +=1
	
    
