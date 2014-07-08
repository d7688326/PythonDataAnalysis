"""
this is used to find all the links that (https://foursquare.com/explore?mode=url&near=New%20York%2C%20NY&q=museum) 
provides, which are most popular museums in New york city 
"""


import re

import urllib2

FileName = 'links'
# new browser for opening the website
browser=urllib2.build_opener()
browser.addheaders=[('User-agent', 'Mozilla/5.0')]
# function for saving links to a txt file
def getUrlFromPage(link):
	response=browser.open(link) 
	myHTML=response.read()
	nameOfFile = ''+FileName+'.txt'
	fileWriter=open(nameOfFile,'w')
	# find all related links by regex
	urls = re.findall(r'<h2>\s*<a\s*href=[\'"]?([^\'" >]+)', myHTML)
	print ', \n'.join(urls)
	# write them into a txt file
	fileWriter.write('https://foursquare.com')
	fileWriter.write('\nhttps://foursquare.com'.join(urls))
	fileWriter.close()

getUrlFromPage("https://foursquare.com/explore?mode=url&near=New%20York%2C%20NY&q=museum")


	


