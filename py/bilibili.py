# -*- coding: utf-8 -*-
import urllib
import urllib2
from bs4 import BeautifulSoup

"""
https://movie.douban.com/review/best/?start=40
"""

url = 'https://bangumi.bilibili.com/anime/timeline'
request = urllib2.Request(url)
response = urllib2.urlopen(request)
html = response.read()

soup =  BeautifulSoup(html, 'html.parser')
#pics = soup.select('div.thumbnail-cover img')
covers = soup.select('.c-item img')
names = soup.select('.t span')
links = soup.select('.r-i a:nth-of-type(2)')
updatetimes = soup.select('.update-time')
infos = soup.select('.update-info')

for cover, name, link, updatetime, info in zip(covers, names, links, updatetimes, infos):
    data = {
        'cover': 'https:'+cover.get('src'),
        'name': name.get_text(),
        'link': 'https:'+link.get('href'),
        'updatetime': updatetime.get_text().strip(),
        'info': info.get_text()
    }
#     print '''cover: %s,
# name: %s,
# link: %s,
# updatetime: %s,
# info: %s''' % (data['cover'], data['name'], data['link'], data['updatetime'], data['info'])
    print data