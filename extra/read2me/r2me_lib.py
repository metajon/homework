import feedparser
from bs4 import BeautifulSoup
from urllib2 import urlopen
urls = {'The Robot Report':'http://www.therobotreport.com/feed'}
d = feedparser.parse(urls['The Robot Report'])
#
#if 'content' in d['entries'][0].keys():
#	c = d['entries'][0]['content']
#else:
#	c = d['entries'][0]['summary']
#soup = BeautifulSoup(str(c))
#print(soup.get_text())
def show_feeds(urls):
    print(urls.keys())

def show_titles(d):
    for i in range(len(d)):
        print('[' + str(i) + '] ' + d['entries'][i]['title'])

def request_content(article_list,d):
    if type(article_list) is not list:
        print('Function requires a list.')
    else:
        for i in range(len(article_list)):
        	soup = BeautifulSoup(urlopen(d['entries'][i]['link']))
        	return soup.find_all("p")