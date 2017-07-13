import urllib
import urllib2
from bs4 import BeautifulSoup
import datetime

"""
url = 'https://www.qiushibaike.com/'
https://www.qiushibaike.com/8hr/page/2/?s=4997457
https://www.qiushibaike.com/8hr/page/3/?s=4997457
"""
def get_page(url, page):
    headers = {
        'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_0) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/59.0.3071.115 Safari/537.36'
    }
    request = urllib2.Request(url, headers=headers)
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
    covers = soup.select('.cover img')
    titles = soup.select('.title a')
    links = soup.select('.title a')
    introduces = soup.select('.brief')
    dates = soup.select('.date')

    for cover, title, link, introduce, date in zip(covers, titles, links, introduces, dates):
        data = {
            'cover': cover.get('src'), 
            'title': title.get_text().strip(),
            'link': 'http://www.xiami.com/'+title.get('href'),
            'introduce': introduce.get_text(),
            'date': date.get_text().strip()
        }
        print "{'cover': %s, 'title': %s, 'link': %s, 'introduce': %s, 'date': %s}" % (data['cover'], data['title'], data['link'], data['introduce'], data['date'])
    print "page: %s" % (page)

def get_more_page(start, end):
    for page in range(start, end):
        url = 'http://www.xiami.com/collect/subpast/page/%s?spm=0.0.0.0.T8ACHZ' % page
        get_page(url, page)

get_more_page(1,12)