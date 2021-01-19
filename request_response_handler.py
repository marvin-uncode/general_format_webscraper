from urllib.request import urlopen
from urllib.error import HTTPError
from bs4 import BeautifulSoup

#scraps title from url
def getTitle(url):
    try:
        html = urlopen(url)     #sets url to variable html
    except HTTPError as e:
        return None             #if encountered http error, return None
    try:
        bsObj = BeautifulSoup(html.read())      #create beautiful soup object
        title = bsObj.body.h1                   #assigns title to h1 attribute from bsObj
    except AttributeError as e:
        return None                             #if attribute error occurs, return None
    return title

#----------------------------------------------------------------------------------
#Practice code
title = getTitle("http://www.pythonscraping.com/exercises/exercise1.html")

if title == None:
    print("Title could not be found")
else:
    print(title)

