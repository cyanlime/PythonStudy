import urllib
import urllib2
from bs4 import BeautifulSoup

"""
https://movie.douban.com/review/best/?start=40
"""

"""
https://list.jd.com/list.html?cat=1316,1383,1404&page=1&sort=sort_totalsales15_desc&trans=1&JL=6_0_0#J_main
https://list.jd.com/list.html?cat=1316,1383,1404&page=2&sort=sort_totalsales15_desc&trans=1&JL=6_0_0&ms=3#J_main
https://list.jd.com/list.html?cat=1316,1383,1404&page=3&sort=sort_totalsales15_desc&trans=1&JL=6_0_0#J_main
https://list.jd.com/list.html?cat=1316,1383,1404&page=2&sort=sort_totalsales15_desc&trans=1&JL=6_0_0#J_main
"""



#url = 'https://movie.douban.com/explore#!type=movie&tag=%E7%88%B1%E6%83%85&sort=recommend&page_limit=20&page_start=0'

def get_page(url, page):
    request = urllib2.Request(url)
    response = urllib2.urlopen(request)
    html = response.read()

    soup = BeautifulSoup(html, 'html.parser')
    pics = soup.select('.p-img a')
    links = soup.select('.p-img img')
    #prices = soup.select('.J_price')

    #plist > ul > li:nth-child(10) > div > div.p-name.p-name-type3 > a > em

    names = soup.select('div.p-name em')

    print pics

    # pic.get('href')
    # link.get('src')

    



def get_more_pages(start, end):
    for page in range(start, end):
        url = 'https://list.jd.com/list.html?cat=1316,1383,1404&page=%s&sort=sort_totalsales15_desc&trans=1&JL=6_0_0#J_main' % (page)
        get_page(url,page)

get_more_pages(1,10)


# def get_page(url, page):
#     request = urllib2.Request(url)
#     response = urllib2.urlopen(request)
#     html = response.read()

#     soup = BeautifulSoup(html, 'html.parser')
#     #pics = soup.select('div.thumbnail-cover img')
#     pics = soup.select('img.movie-img')
#     print pics


# def get_more_pages(start, end):
#     for one in range(start, end):
#         url = 'https://movie.douban.com/j/chart/top_list?type=13&interval_id=100%3A90&action=&start='
#         url = url+'%s&limit=20' % (20*(one-1))

#         #url = 'https://movie.douban.com/j/chart/top_list?type=13&interval_id=100%3A90&action=&start=%s&limit=20' % (20*(one-1))
#         get_page(url, one)

# get_more_pages(1, 10)
