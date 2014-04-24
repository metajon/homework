import feedparser
from bs4 import BeautifulSoup
urls = {'Rescue Muni':'http://www.rescuemuni.org/feed/',
		'The N-Judah Chronicles':'http://feeds.feedburner.com/TheN-judahChronicles',
		'Muni Diaries':'http://www.munidiaries.com/feed/',
		'Streetsblog San Francisco':'http://sf.streetsblog.org/feed/'}
#d = feedparser.parse(urls['The Robot Report'])

def show_feeds(urls):
    print(urls.keys())

def parse_url(url):
	parsed_feed = feedparser.parse(url)
	return parsed_feed

def print_titles(parsed_feed):
    for i in range(len(parsed_feed['entries'])):
        print('[' + str(i) + '] ' + parsed_feed['entries'][i]['title'])

def print_all_titles(urls):
	for i in range(len(urls)):
		parsed_feed = parse_url(urls.values()[i])
		for j in range(len(parsed_feed['entries'])):
			print('[' + str(j) + '] ' + parsed_feed['entries'][j]['title'])