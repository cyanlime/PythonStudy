import requests
import re


def get_page(url):
    response = requests.get(url)
    html = response.content
    print html
    url = re.findall('<div class="leftimg">\s*<a target="_blank" href="(.*?)">', html, re.S)
    covers = re.findall('<div class="leftimg">.*<img src="(.*?)"', html, re.S)


def get_more_pages():
    pass



if __name__ == '__main__':
    url = 'http://you.ctrip.com/sight/xiamen21/s0-p1.html'
    #url = 'http://you.ctrip.com/sight/xiamen21/s0-p3.html#sightname'
    get_page(url)