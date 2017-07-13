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
    headportraits = soup.select('.author.clearfix img')
    nicknames = soup.select('.author.clearfix h2')
    contents = soup.select('.content span')

    for headportrait, nickname, content in zip(headportraits, nicknames, contents):
        data = {
            'headportrait': 'https:'+headportrait.get('src'), 
            'nickname': nickname.get_text(),
            'content': content.get_text()
        }
        print "{'headportrait': %s, 'nickname': %s, 'content': %s}" % (data['headportrait'], data['nickname'], data['content'])
    print "page: %s" % (page)

def get_more_page(start, end):
    for page in range(start, end):
        url = 'https://www.qiushibaike.com/8hr/page/%s/?s=4997457' % (page)
        get_page(url, page)

get_more_page(1,35)