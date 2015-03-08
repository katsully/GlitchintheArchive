import pytumblr
import sys
import os
import time
import urllib
from urllib import FancyURLopener
import urllib2
import simplejson
import newspaper
import requests
import re
from bs4 import BeautifulSoup

TAG_RE = re.compile(r'<[^>]+>')

def remove_tags(text):
		return TAG_RE.sub('', text)

# def get_caption(titles):
# 	caption = ""
# 	for title in titles:
# 		caption += title + '\n'
# 	return caption

# ouath_data = open("oauth.txt")

# # get all keys
# keys = ouath_data.read()
# keys_decoded = keys.decode("utf-8-sig")
# keys = keys_decoded.encode("utf-8")
# keys = keys.rstrip().split('\n')
def search_party ():
# Get top Google Trend
  searchTerm = newspaper.hot()[0]

  # Replace spaces ' ' in search term for '%20' in order to comply with request
  searchTermSyntax = searchTerm.replace(' ','%20')

  # Replace spaces ' ' in search term with '+' for bing requests
  bingSearchTermSyntax = searchTerm.replace(' ','+')


  # Start FancyURLopener with defined version 
  class MyOpener(FancyURLopener): 
      version = 'Chrome'



  # Notice that the start changes for each iteration in order to request a new set of images for each loop
  url = ('https://ajax.googleapis.com/ajax/services/search/images?' + 'v=1.0&q='+searchTermSyntax+'&start='+str(0)+'&userip=MyIP')
  #urllib.urlretrieve(url, "image"  str(i)  ".jpg")
  request = urllib2.Request(url, None, {'Referer': 'testing'})
  response = urllib2.urlopen(request)

  # Get results using JSON
  results = simplejson.load(response)
  data = results['responseData']
  dataInfo = data['results']

  # Get unescaped url for first result
  myopener.retrieve(dataInfo[0]['unescapedUrl'],searchTerm+'.jpg')




# get top news articles from Bing
  page = urllib2.urlopen('http://www.bing.com/news/search?q='+bingSearchTermSyntax+'&FORM=HDRSC6').read()
  soup = BeautifulSoup(page)

  mydivs = soup.findAll('div', {'class':'newstitle'})
  links = [div.findAll('a') for div in mydivs]



  titles = [link[0].contents for link in links]



  new_titles = []


# each title comes in as a list (ie - [<strong>Daylight</strong>, u' ', <strong>Saving</strong>, u' ', <strong>Time</strong>, u' Starts Sunday at 2 a.m.'])
# this loop concatenates the list as a string and removes html tags
  for title in titles:
      if title[0].find('img') == -1 and title[0].find('RSS') == -1:
      	new_title = ''.join(str(v).encode('ascii','ignore') for v in title)
        new_title = remove_tags(new_title)
        new_titles.append(new_title)
        print new_title



# # post photo to tumblr
# client.create_photo("anarchyarchive", caption=get_caption(new_titles), state="published" , data=searchTerm.encode('utf-8') + ".jpg")