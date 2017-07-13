import urllib
import urllib2
from bs4 import BeautifulSoup
import datetime

"""
url = 'https://www.qiushibaike.com/'
https://www.qiushibaike.com/8hr/page/2/?s=4997457
https://www.qiushibaike.com/8hr/page/3/?s=4997457
"""
url = 'http://www.xiami.com/song/1768196?spm=a1z1s.7154410.0.0.ytiO88'
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
headportraits = soup.select('.usr_cover img')
nicknames = soup.select('.author a')
contents = soup.select('.brief div')
dates = soup.select('.time')

for headportrait, nickname, content, date in zip(headportraits, nicknames, contents, dates):
    data = {
        'headportrait': headportrait.get('src'), 
        'nickname': nickname.get_text(),
        'content': content.get_text().stripped_strings,
        'datetime': date.get_text()
    }
    print "{'headportrait': %s, 'nickname': %s, 'content': %s, 'datetime': %s}" % (data['headportrait'], data['nickname'], data['content'], data['datetime'])
#print "page: %s" % (page)

