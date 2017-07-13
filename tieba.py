import urllib
import urllib2
from bs4 import BeautifulSoup
import datetime

"""
http://tieba.baidu.com/p/2070600427?pn=3
"""
def get_page(url, page):
    headers = {
        'User-Agent': 'User-Agent:Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_0) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/59.0.3071.115 Safari/537.36'
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
    headportraits = soup.select('.p_author_face img')
    nicknames = soup.select('.d_name a')
    contents = soup.select('.d_post_content.j_d_post_content.clearfix')
    images = soup.select('.BDE_Image')

    for headportrait, nickname, content in zip(headportraits, nicknames, contents):
        data = {
            'headportrait': headportrait.get('src'), 
            'nickname': nickname.get_text(),
            'content': content.get_text()
        }
        print "{'headportrait': %s, 'nickname': %s, 'content': %s}" % (data['headportrait'], data['nickname'], data['content'])
    print "page: %s" % (page)

    import uuid
    import requests
    sites = []
    for image in images:
        img_url = image.get('src')
        pic = requests.get(img_url)
        string = 'images/Consort Donggo/'+str(uuid.uuid4())+'.jpg'
        with open(string, 'wb') as fp:
            fp.write(pic.content)

        sites.append(img_url)

def get_more_page(start, end):
    for page in range(start, end):
        url = 'http://tieba.baidu.com/p/2070600427?pn=%s' % (page)
        get_page(url, page)

get_more_page(1,5)