url = 'http://example.com/pdfs'
base_url = 'http://example.com/'

import urllib2
import os
from bs4 import BeautifulSoup

materials = urllib2.urlopen(url)

soup = BeautifulSoup(materials)

def find_urls(soup):
	all_urls = []
	for link in soup.find_all('a'):
		all_urls.append(link.get('href'))
	return all_urls

def find_pdfs_from_urls(url_list):
	pdf_list = []
	for i in range(len(url_list)):
		if '.pdf' in url_list[i]:
			pdf_list.append(url_list[i])
	return pdf_list

def download_urls(pdf_list):
	for link in pdf_list:
		url = base_url + link
		dlfile(url)

def dlfile(url):
	# Open the url
	try:
		f = urllib2.urlopen(url)
		print "downloading " + url
		# Open our local file for writing
		with open(os.path.basename(url), "wb") as local_file:
			local_file.write(f.read())
	#handle errors
	except urllib2.HTTPError, e:
		print "HTTP Error:", e.code, url
	except urllib2.URLError, e:
		print "URL Error:", e.reason, url

main():
	# not yet tested.
	download_urls(find_pdfs_from_urls(find_urls(soup)))


if __name__ == '__main__':
	main()