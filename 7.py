import selenium
logat=input("enter loghat")
import requests
import urllib
from bs4 import BeautifulSoup as bs
r=requests.get('http://dehkhoda.ut.ac.ir/fa/dictionary')
soup =bs(r.content)
print(soup.prettify())
find_header =soup.find(logat)
print(find_header)
header =soup.find_all(logat)
header
search= bs('http://dehkhoda.ut.ac.ir/fa/dictionary')
search.find_all('loghat')
if True :
    print("hast")
else :
    BeautifulSoup.append(logat)
