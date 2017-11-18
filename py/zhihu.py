import urllib
import urllib2
from bs4 import BeautifulSoup
import datetime

for page in range(1, 70):
    url = 'https://www.zhihu.com/topic/19845181/questions?page=%s' % page

    request = urllib2.Request(url)
    response = urllib2.urlopen(request)
    html = response.read()

    soup = BeautifulSoup(html, 'html.parser')
    titles = soup.select('a.question_link')
    links = soup.select('a.question_link')
    dates = soup.select('.time')

    for title, link, date in zip(titles, links, dates):
        unix_date = int(str(date.get('data-timestamp'))[:10])
        data = {
            'title': title.get_text(),
            'link': 'https://www.zhihu.com/'+link.get('href'),
            'date': datetime.datetime.fromtimestamp(unix_date)
        }
        print "{'title': %s, 'link': %s, 'date': %s}" % (title.get_text(), 'https://www.zhihu.com/'+link.get('href'), datetime.datetime.fromtimestamp(unix_date))
    print "page %s" % (page)
