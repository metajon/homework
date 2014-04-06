import feedparser
from bs4 import BeautifulSoup
url = ['http://www.therobotreport.com/feed']
d = feedparser.parse(url[0])

if 'content' in d['entries'][0].keys():
    c = d['entries'][0]['content']
else:
    c = d['entries'][0]['summary']
soup = BeautifulSoup(str(c))
print(soup.get_text())
