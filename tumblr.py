import pytumblr
import sys
import os
import time
import urllib
from urllib import FancyURLopener
import urllib2
import simplejson
import requests
from bs4 import BeautifulSoup

ouath_data = open("oauth.txt")

# get all keys
keys = ouath_data.read()
keys_decoded = keys.decode("utf-8-sig")
keys = keys_decoded.encode("utf-8")
keys = keys.rstrip().split('\n')

# Get top Google Trend
page = urllib2.urlopen('http://www.google.com/trends/').read()
soup = BeautifulSoup(page)
mydivs = soup.findAll("div", { "class" : "landing-page-hottrends-image-and-info-row-container" })
myspans = [div.span for div in mydivs]
search_term_list = [span.getText() for span in myspans]
searches_spans = soup.findAll("span", { "class" : "hottrends-single-trend-info-line-number" })
search_num_list = [span.getText().replace(",","")[:-1] for span in searches_spans]
search_num_list = map(int, search_num_list)
## THIS IS THE NUMBER YOU WANT
top_hit_num = max(search_num_list)
search_index = search_num_list.index(top_hit_num)
searchTerm = search_term_list[search_index]
print searchTerm


# Replace spaces ' ' in search term for '%20' in order to comply with request
searchTermSyntax = searchTerm.replace(' ','%20')


# Start FancyURLopener with defined version 
class MyOpener(FancyURLopener): 
    version = 'Chrome'
myopener = MyOpener()


# Notice that the start changes for each iteration in order to request a new set of images for each loop
url = ('https://ajax.googleapis.com/ajax/services/search/images?' + 'v=1.0&q='+searchTermSyntax+'&start='+str(0)+'&userip=MyIP')
#urllib.urlretrieve(url, "image" + str(i) + ".jpg")
request = urllib2.Request(url, None, {'Referer': 'testing'})
response = urllib2.urlopen(request)

# Get results using JSON
results = simplejson.load(response)
data = results['responseData']
dataInfo = data['results']

# Get unescaped url for first result
print dataInfo[0]['unescapedUrl']

myopener.retrieve(dataInfo[0]['unescapedUrl'],searchTerm+'.jpg')

# Authenticate via OAuth
client = pytumblr.TumblrRestClient(
  keys[0],
  keys[1],
  keys[2],
  keys[3]
)

# TO DO - include search term (make an image macro)
# Find article on something like Fox News, find number of comments, glitch based on 
# number of comments

## Why are some images glitched more than others?

## Single image is better
# post photo to tumblr
client.create_photo("anarchyarchive", state="published" , data=searchTerm.encode('utf-8') + ".jpg")