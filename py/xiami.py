import urllib
import urllib2
from bs4 import BeautifulSoup
import requests
import uuid

"""
url = 'https://www.qiushibaike.com/'
https://www.qiushibaike.com/8hr/page/2/?s=4997457
https://www.qiushibaike.com/8hr/page/3/?s=4997457
"""
def get_page(song_sheet, url, page):
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
    covers = soup.select('.block_cover img')
    titles = soup.select('.block_items.clearfix a')
    links = soup.select('.block_items.clearfix a')
    authors = soup.select('.collect_info a')
    dates = soup.select('.collect_info span')

    for cover, title, link, author, date in zip(covers, titles, links, authors, dates):
        data = {
            'cover': cover.get('src'), 
            'title': title.get('title'),
            'link': 'http://www.xiami.com'+link.get('href'),
            'author': author.get('title'),
            'date': date.get_text()
        }
        if data['link']!='http://www.xiami.comjavascript:;' and (data['link'] not in song_sheet) and ('/u/' not in data['link']) and ('http://www.xiami.comhttp://' not in data['link']):
            song_sheet.append(data['link'])
        print "{'cover': %s, 'title': %s, 'link': %s, 'author': %s, 'date': %s}" % (data['cover'], data['title'], data['link'], data['author'], data['date'])
    print "page: %s" % (page)

def get_more_pages(start, end):
    song_sheet = []
    for page in range(start, end):  
        url = 'http://www.xiami.com/collect/recommend/page/%s?spm=a1z1s.3061697.6856253.143.9F0SxD' % (page)
        get_page(song_sheet, url, page)
    return song_sheet

def get_infos():
    infos = []
    sheets = get_more_pages(1, 5)

    sheet = 0
    for url in sheets:
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
        covers = soup.select('.bigImgCover img')
        titles = soup.select('.info_collect_main h2')
        labels = soup.select('.cdinfo a[target="_blank"]')
        #authors = soup.select('.cdinfo a[title]')
        #dates = soup.select('.cdinfo li')

        info_imgs = soup.select('.bigImg img')
        song_names = soup.select('.song_name a')
        introduces = soup.select('#des_')

        if len(covers)!=0 and len(titles)!=0 and len(labels)!=0:
            cover = covers[0].get('src')
            pic = requests.get(cover)
            string = 'images/Xiami/cover/'+str(uuid.uuid4())+'.jpg'
            with open(string, 'wb') as fp:
                fp.write(pic.content)
           
            info = {
                'cover': cover, 
                'title': titles[0].get_text().strip(),
                #'author': author.get('title'),
            }
            
            info['label'] = []
            info['img'] = []
            info['song_name'] = []
            for label in labels:
                info['label'].append(label.get_text())
            for img in info_imgs:
                img_url = img.get('src')
                pic = requests.get(img_url)
                string = 'images/Xiami/image/'+str(uuid.uuid4())+'.jpg'
                with open(string, 'wb') as fp:
                    fp.write(pic.content)

                info['img'].append(img_url)
            for name in song_names:
                info['song_name'].append(name.get('title'))
            
            infos.append(info)
            print '''{'cover': %s, 
            'title': %s, 
            'label': %s, 
            'img': %s, 
            'song_name': %s}''' % (info['cover'], info['title'], info['label'], info['img'], info['song_name'])

            print 'sheet %s' % (sheet)
            sheet+=1

    return infos

print "start downloading..."
get_infos()
print "ending."