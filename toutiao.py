import requests
import urllib
import urllib2
import json

params = {
    'offset': 0,
    'format': 'json',
    'keyword': '街拍',
    'autoload': 'true',
    'count': 20,
    'cur_tab': 3
}
url = 'http://www.toutiao.com/search_content/?' + urllib.urlencode(params)

def get_page(url):
    try:
        request = urllib2.Request(url)
        response = urllib2.urlopen(request)
        html = response.read()
    except urllib2.HTTPError,e:
        if hasattr(e, "code"):
            print e.code
        if hasattr(e, "reason"):
            print e.reason

    data = json.loads(html)
    if data and 'data' in data.keys():
        for item in data.get('data'):
            print item.get('article_url')



def get_more_pages():
    pass

get_page(url)


