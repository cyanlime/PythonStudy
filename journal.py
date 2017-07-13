import urllib2
from bs4 import BeautifulSoup

url = 'http://you.ctrip.com/'
def get_page(url):
    request = urllib2.Request(url)
    response = urllib2.urlopen(request)
    html = response.read()

    soup = BeautifulSoup(html, "html.parser")
    journal_pics = soup.select('div.journal_pic img')
    titles = soup.select('div.r_text a')
    links = soup.select('div.r_text a')

    for journal_pic, title, link in zip(journal_pics, titles, links):
        data = {
            'pic': journal_pic.get('src'),
            'title': title.get_text(),
            'link': link.get('href')
        }
        print data

get_page(url)  
