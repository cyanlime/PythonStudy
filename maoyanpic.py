import requests
from bs4 import BeautifulSoup
from requests.exceptions import HTTPError
import re
import sqlite3
import os
import json
import urllib2, time

def get_url(url):
    try:
        request = urllib2.Request(url)
        print url
        response = urllib2.urlopen(request)
        # response = requests.get(url)
        print 'response OK'
        if response.code==200:
            html = response.read()
            #return response.text
            return html
        return None
    except HTTPError, e:
        print "request error"
        return None

def get_page(url, page):
    newsimgs = []
    html = get_url(url)

    titles = re.findall('<h4 class="images-header one-line">.*?}">(.*?)</a>', html, re.S)
    links = re.findall('<h4 class="images-header one-line">\s*<a href="(.*?)"', html, re.S)
    coverimages =  re.findall('<div class="images-thumbnails clearfix">.*?<img src="(.*?)".*?<img src="(.*?)".*?<img src="(.*?)"', html, re.S)

    for title, link, coverimgs in zip(titles, links, coverimages):
        data = {
            'title': title,
            'link': 'http://maoyan.com'+link,
            'coverimgs': coverimgs
        }
        data = get_detail_imgs(data['link'], data)
        newsimgs.append(data)
        with open('maoyanpic.txt', 'a') as f:
            f.write(json.dumps(data) + '\n')
#         print """
# title: %s,
# link: %s,
# coverimages: %s,
# shareImg: %s,
# images: %s
# comments: %s       
# """ % (data['title'], data['link'], data['coverimgs'], data['shareImg'], data['images'], data['comments'])
    return newsimgs

def create_datasheet():
    conn = sqlite3.connect("maoyanpic.db")
    print "Opened database successfully"

    c = conn.cursor()
    c.execute("PRAGMA foreign_keys = ON")

    c.execute('''CREATE TABLE if not exists newsimg
        (id integer primary key autoincrement,
        title char,
        link char,
        shareImg char)''')

    c.execute('''CREATE TABLE if not exists coverimage
        (id integer primary key autoincrement,
        imageurl char,
        newsimg_id integer,
        FOREIGN KEY(newsimg_id) REFERENCES newsimg(id))''')        

    c.execute('''CREATE TABLE if not exists image
        (id integer primary key autoincrement,
        url char,
        content text,
        newsimg_id integer,
        FOREIGN KEY(newsimg_id) REFERENCES newsimg(id))''')

    c.execute('''CREATE TABLE if not exists comment
        (id integer primary key autoincrement,
        headportrait char,
        nickname char,
        comment char,
        date char,
        newsimg_id integer,
        FOREIGN KEY(newsimg_id) REFERENCES newsimg(id))''')

    conn.commit()
    conn.close()
    print 'you can use datasheets'


def save_to_sqlite3(url, page):
    newsimgs = get_page(url, page)
    conn = sqlite3.connect("maoyanpic.db")
    print "Opened database successfully"

    c = conn.cursor()
    c.execute("PRAGMA foreign_keys = ON")

    c.execute('SELECT * FROM newsimg WHERE link=?', (newsimgs[0]['link'],))
    datas = c.fetchall()
    if len(datas)==0:
        for newimg in newsimgs:
            c.execute('INSERT INTO newsimg (title, link, shareImg) VALUES (?,?,?)', (newimg['title'], newimg['link'], newimg['shareImg']))
            print 'insert data into newimg: %s' % newimg['title']
            
            newsimg_id = c.lastrowid
            covers = []
            imgurls = []
            usercomms = []

            for cover in newimg['coverimgs']:
                cover = re.findall('(.*?)@', cover, re.S)[0]
                covers.append((cover, newsimg_id),)
            c.executemany('INSERT INTO coverimage (imageurl, newsimg_id) VALUES (?,?)', covers)

            for image in newimg['images']:
                imgurl = re.findall('(.*?)@', image[1], re.S)[0]
                imgurls.append((imgurl, image[0], newsimg_id),)
            c.executemany('INSERT INTO image (url, content, newsimg_id) VALUES (?,?,?)', imgurls)           
            
            for usercomm in newimg['comments']:
                usercomms.append((usercomm['headportrait'], usercomm['nickname'], usercomm['comment'], usercomm['date'], newsimg_id),)
            c.executemany('INSERT INTO comment (headportrait, nickname, comment, date, newsimg_id) VALUES (?,?,?,?,?)', usercomms)           
            print 'insert data into comment: %s' % usercomm['nickname']

    conn.commit()
    conn.close()
    print "page %s insert done" % (page)


def get_detail_imgs(url, data):
    html = get_url(url)

    shareImg = re.findall('.*?"shareImg":"(.*?)"', html, re.S)
    images = re.findall('.*?"content":"(.*?)","imageUrl":"(.*?)"', html, re.S)

    headportraits = re.findall('<div class="portrait">\s*<img src="(.*?)"', html, re.S)
    nicknames = re.findall('<span class="name">(.*?)</span>', html, re.S)
    comments = re.findall('<div class="comment-content">(.*?)</div>', html, re.S)
    dates = re.findall('<div class="time" title="(.*?)">', html, re.S)

    usercomments = []
    for headportrait, nickname, usercomment, date in zip(headportraits, nicknames, comments, dates):
        comment = {
            'headportrait': re.findall('(.*?)@', headportrait, re.S)[0],
            'nickname': nickname,
            'comment': usercomment,
            'date': date
        }
        usercomments.append(comment)

    data['shareImg'] = re.findall('(.*?)@', shareImg[0], re.S)[0]
    data['images'] = images
    dir = make_dirs(data['title'])
    save_images(images, dir)
    data['comments'] = usercomments
    return data

def make_dirs(path):
    dir = os.path.join('images/Maoyanpic/', path)
    is_exists = os.path.exists(dir)
    if not is_exists:
        print 'create a directory: %s' % (path)
        os.mkdir(os.path.join('images/Maoyanpic/', path))
    return dir

def save_images(images, dir):
    for image in images:
        url = re.findall('(.*?)@', image[1], re.S)[0]
        boolean = is_img_download(dir, url)
        if boolean==True:
            print 'Downloading image: %s' % url
            pic = requests.get(url)    
            try:
                name = re.findall('.*?/movie/(.*?)$', url, re.S)[0]
            except:
                name = re.findall('.*/(.*?)$', url, re.S)[0] + '.jpg'
            string = os.path.join(dir, name) 
            with open(string, 'wb') as fp:
                fp.write(pic.content)   
            print 'Image %s saved' % url
        else:
            print 'Image %s has been downloaded' % url

def is_img_download(dir, url):
    try:
        name = re.findall('.*?/movie/(.*?)$', url, re.S)[0]
    except:
        name = re.findall('.*/(.*?)$', url, re.S)[0] + '.jpg'
    path = os.path.join(dir, name)

    if os.path.exists(path):
        return False
    else:
        return True

# def get_more_pages(start, end):
#     #create_datasheet()
#     for page in range(start, end):
#         if page==1:
#             url = 'http://maoyan.com/news?showTab=4'
#         else:
#             url = 'http://maoyan.com/news?showTab=4&offset=%s' % ((page-1)*10)
#         save_to_sqlite3(url, page)

#get_more_pages(20,22)

# url = 'http://maoyan.com/news?showTab=4'
# save_to_sqlite3(url, 1)


from multiprocessing import Pool
import os, time

def get_more_pages(page):
    print 'Run task %s(%s)' % (page, os.getpid())
    if page==1:
        url = 'http://maoyan.com/news?showTab=4'
    else:
        url = 'http://maoyan.com/news?showTab=4&offset=%s' % ((page-1)*10)
    save_to_sqlite3(url, page)
    print url

if __name__ == '__main__':
    print 'Parent process: %s' % os.getpid()
    create_datasheet()
    p = Pool()
    start = time.time()
    for i in range(40, 80):
        p.apply_async(get_more_pages, args=(i,))
        print 'download page %s' % i
    print 'Waiting for all subprocesses done...'
    p.close()
    p.join()
    end = time.time()
    print 'All subprocesses done, takes %s seconds' % (end-start)


# url = 'http://maoyan.com/news/21084'
# response = requests.get(url)
# html = response.text
# comments = re.findall('<div class="comment-content">(.*?)</div>', html, re.S)
# for comment in comments:
#     print comment