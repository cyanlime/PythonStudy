# -*- coding: utf-8 -*-

import urllib
import urllib2
from bs4 import BeautifulSoup


"""
https://movie.douban.com/review/best/?start=40
"""

def get_page(url, one):
    request = urllib2.Request(url)
    response = urllib2.urlopen(request)
    html = response.read()

    soup = BeautifulSoup(html, 'html.parser')
    #pics = soup.select('div.thumbnail-cover img')
    pics = soup.select('.subject-img img')
    names = soup.select('.title-link')
    links = soup.select('.title-link')
    comments = soup.select('.short-content')

    for pic, name, link, comment in zip(pics, names, links, comments):
        data = {
            'pic': pic.get('src'),
            'name': name.get_text(),
            'link': link.get('href'),
            'comments': comment.get_text()
        }
        for key in data:
            print key, data[key]
    print one

def get_more_page(start, end):
    for one in range(start, end):
        url = 'https://movie.douban.com/review/best/?start=%s' % (20*(one-1))
        get_page(url, one)
    
get_more_page(1,6)