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

# Get top Google Trend
searchTerm = newspaper.hot()[0]

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
  'ooimSQMY3oWBCpM25m9ShanYPkeZIjsxKTAncUUshzRf3cv7yu',
  '19b0a9BiJzQIEBnRBtfKAqmqgOf7jyoDyvVKqWf6adgWk8Plx9',
  'CpNsePybAAFC1GhVUGOOqhW7TFc0V00ntb89IdhkTDkNyeXwGm',
  'NSGiU1oz1i7Goe662NgdYgclc74ab87KyDvnQJhovfd0XT5Bb5'
)

# post photo to tumblr
client.create_photo("anarchyarchive", state="published" , data=searchTerm.encode('utf-8') + ".jpg")