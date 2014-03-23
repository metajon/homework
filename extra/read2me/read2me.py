#!/usr/bin/python
# encoding: utf-8
#
# Licensed under the BSD License.
#
# This is a work in progress.  Not intended for production use.
#
# read2me.py reads the news.
#
from urllib2 import urlopen
from xml.dom import minidom
from bs4 import BeautifulSoup
#
sf_feeds = ['http://blog.sfgate.com/cityinsider/feed/','http://blog.sfgate.com/matierandross/feed/','http://feeds.feedburner.com/BeersmithcomHomeBrewingBlog?format=xml']
#
xmldocs = []
#
for feed in sf_feeds:
	xmldocs.append(minidom.parse(urlopen(feed)))
#
# Just prints the titles.
for i in range(len(xmldocs)):
	for j in range(len(xmldocs[i].getElementsByTagName('title'))):
		print xmldocs[i].getElementsByTagName('title')[j].firstChild.data
#
# We need a holder dictionary.
articles = {}
#
xmldoc = minidom.parse(urlopen(sf_feeds[2]))
#
for i in range(len(xmldoc.getElementsByTagName('title'))):
	articles.update({xmldoc.getElementsByTagName('title')[i].firstChild.data: xmldoc.getElementsByTagName('link')[i].firstChild.data})
#
print articles[(xmldoc.getElementsByTagName('title')[0].firstChild.data)]
#
# Just for reference:
soup = BeautifulSoup(urlopen(xmldoc.getElementsByTagName('link')[1].firstChild.data))
soup.find("div", {"class": "entry"})
#
# I like dictionaries.
full_articles = {}
#
# Loop through the article titles, and fetch the entry html.
for i in range(len(xmldoc.getElementsByTagName('title'))):
    full_articles.update({xmldoc.getElementsByTagName('title')[i].firstChild.data: (BeautifulSoup(urlopen(xmldoc.getElementsByTagName('link')[i].firstChild.data)).find("div", {"class": "entry"}))})
#
# Loop through the article titles, and fetch the content html.
for i in range(len(xmldoc.getElementsByTagName('title'))):
    full_articles.update({xmldoc.getElementsByTagName('title')[i].firstChild.data: (BeautifulSoup(urlopen(xmldoc.getElementsByTagName('link')[i].firstChild.data)).find("div", {"id": "content"}))})
#
def print_titles():
	for i in range(len(full_articles.keys())):
		print "[%d] %s" % (i,str(full_articles.keys()[i].encode('utf8')))
#
def selected_articles(my_choices):
	result = []
	if type(my_choices) is list:
		for choice in my_choices:
			result.append(choice)
	else:
		print 'Articles must be provided as a list: []'
	return result
#
def output_articles(selected_articles):
	for i in range(len(selected_articles)):
		with open('index.html','a+') as f:
			title_string = "<h1>%s</h1>" % str(full_articles.keys()[(selected_articles[i])].encode('utf8'))
			f.write(title_string)
			f.write(str(full_articles[(full_articles.keys()[(selected_articles[i])])]))
		f.closed
#
def print_articles(selected_articles):
	for i in range(len(selected_articles)):
		print(full_articles[(full_articles.keys()[(selected_articles[i])])])
#
html = full_articles[(full_articles.keys()[3])]
parsed_html = BeautifulSoup(html)
import requests
result = requests.get("http://beersmith.com/blog/2014/03/19/five-more-tips-for-all-grain-beer-brewing/")
c = result.content
soup = BeautifulSoup(c)
soup.body.find('div', attrs={'id':'content'}).text
#
#