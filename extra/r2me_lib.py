import feedparser
from bs4 import BeautifulSoup
url = []
d = feedparser.parse(url)
c = d['entries'][0]['content']
soup = BeautifulSoup(str(c))
print(soup.get_text())
