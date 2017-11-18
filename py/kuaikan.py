# -*- coding: utf-8 -*-

import urllib
import urllib2
from bs4 import BeautifulSoup
import requests
import uuid

"""
http://www.kuaikanmanhua.com/?pos=6
"""

def get_page(periods, url, page):
    #url = 'http://www.kuaikanmanhua.com/'
    headers = {
        'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_0) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/59.0.3071.115 Safari/537.36'
    }
    try:
        request = urllib2.Request(url, headers=headers)
        response = urllib2.urlopen(request)
        html = response.read()
    except urllib2.HTTPError,e:
        if hasattr(e, "code"):
            print e.code
        if hasattr(e, "reason"):
            print e.reason

    soup = BeautifulSoup(html, 'html.parser')
    covers = soup.select('.blank-img')
    titles = soup.select('.topic-tit a')
    links = soup.select('.topic-tit a')
    authors = soup.select('.topic-title.fl-left')
    praises = soup.select('.praise.ico-praise.fl-right')

    for cover, title, link, author, praise in zip(covers, titles, links, authors, praises):
        data = {
            'cover': cover.get('src'), 
            'title': title.get('title'),
            'link': 'http://www.kuaikanmanhua.com'+link.get('href'),
            'author': author.get_text(),
            'praise': praise.get_text()
        }
        periods.append(data)
        print "{'cover': %s, 'title': %s, 'link': %s, 'author': %s, 'praise': %s}" % (data['cover'], data['title'], data['link'], data['author'], data['praise'])
    
    print "page: %s" % (page)

def get_more_page(start, end):
    periods = []
    for page in range(start, end):
        url = 'http://www.kuaikanmanhua.com/?pos=%s' % (page)
        get_page(periods, url, page)
    return periods

def get_page_detail(periods):
    cartoons = []
    for period in periods:
        percar = {}
        url = period['link']
        try:
            request = urllib2.Request(url)
            response = urllib2.urlopen(request)
            html = response.read()
        except urllib2.HTTPError,e:
            if hasattr(e, "code"):
                print e.code
            if hasattr(e, "reason"):
                print e.reason

        soup = BeautifulSoup(html, 'html.parser')
        cover = soup.select('.kk-img')[0].get('src')
        title = soup.select('.comic-name')[0].get_text()
        author = soup.select('.author-nickname')[0].get_text()
        comment = soup.select('.switch-content p')[0].get_text()

        verse_covers = soup.select('.kk-sub-img')
        verse_titles = soup.select('.tit a')
        verse_links = soup.select('.tit a')
        verse_praises = soup.select('.like')
        verse_dates = soup.select('tr > td:nth-of-type(4)')

        percar['info'] = []
        for vercover, vertitle, verlink, verpraise, verdate in zip(verse_covers, verse_titles, verse_links, verse_praises, verse_dates):
            info = {
                'vercover': vercover.get('src'),
                'vertitle': vertitle.get('title'),
                'verlink': 'http://www.kuaikanmanhua.com'+verlink.get('href'),
                'verpraise': verpraise.get_text().strip(),
                'verdate': verdate.get_text()
            }
            a = get_detail_images(info['verlink'], info['vertitle'])

            percar['info'].append(info)
        percar['cover']=cover
        percar['title']=title
        percar['author']=author
        percar['comment']=comment
        print '''cover: %s, 
            title: %s,
            author: %s,
            comment: %s,
            info: %s    
            ''' % (percar['cover'], percar['title'], percar['author'], percar['comment'], percar['info'])
        cartoons.append(percar)
        print 'period %s' % len(cartoons)
    return cartoons

def get_detail_images(url, title):
    a = {}
    images = []
    try:
        request = urllib2.Request(url)
        response = urllib2.urlopen(request)
        html = response.read()
    except urllib2.HTTPError,e:
        if hasattr(e, "code"):
            print e.code
        if hasattr(e, "reason"):
            print e.reason

    soup = BeautifulSoup(html, 'html.parser')
    imgs = soup.select('.kklazy')
    for img in imgs:
        imglink = img.get('data-kksrc')
        if imglink is not None:
            pic = requests.get(imglink)
            path = 'images/Kuaikan/%s' % title
            string = path+str(uuid.uuid4())+'.jpg'
            with open(string, 'wb') as fp:
                fp.write(pic.content)

            images.append(imglink)

    a['title'] = title
    a['image'] = images
    return a
    

print "starting..."
periods = get_more_page(0,7)
get_page_detail(periods)
print "end"