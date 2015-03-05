from bs4 import BeautifulSoup, NavigableString
import urllib2
import re

TAG_RE = re.compile(r'<[^>]+>')

def remove_tags(text):
    return TAG_RE.sub('', text)


page = urllib2.urlopen('http://www.bing.com/news/search?q=momofuku+ando&FORM=HDRSC6').read()
soup = BeautifulSoup(page)

mydivs = soup.findAll('div', {'class':'newstitle'})
links = [div.findAll('a') for div in mydivs]


titles = [link[0].contents for link in links]

new_titles = []

for title in titles:
    if title[0].find('img') == -1 and title[0].find('RSS') == -1:
    	new_title = ''.join(str(v) for v in title)
        new_title = remove_tags(new_title)
        print new_title
