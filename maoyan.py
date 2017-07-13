import requests
from bs4 import BeautifulSoup
from requests.exceptions import HTTPError
import re
import sqlite3
import os

def get_url(url):
    try:
        response = requests.get(url)
        if response.status_code==200:
            return response.text
        return None
    except HTTPError, e:
        print "request error"
        return None

def get_board(url):
    boards = []
    html = get_url(url)
    # soup = BeautifulSoup(html, 'html.parser')
    # covers = soup.select('.board-img')
    # names = soup.select('.name a')
    # links = soup.select('.name a')
    # actors = soup.select('.star')
    # dates = soup.select('.releasetime')
    # integers = soup.select('.integer')
    # fractions = soup.select('.fraction')

    pattern = re.compile('<dd>.*?<img data-src="(.*?)".*?<p class="name"><a href="(.*?)" title="(.*?)".*?<p class="star">\s*(.*?)\s*</p>'
            '.*?<p class="releasetime">(.*?)</p>.*?<i class="integer">(.*?)</i><i class="fraction">(.*?)</i>', re.S)
    items = re.findall(pattern, html)
    #print items

    for item in items:
        data = {
            'cover': item[0],
            'name': item[2],
            'link': 'http://maoyan.com'+item[1],
            'actor': item[3][3:],
            'date': item[4][5:],
            'score': item[5]+item[6]
        }
        data = get_detail_info(data['link'], data)
        boards.append(data)

    # for cover, name, link, actor, date, integer, ifraction in zip(covers, names, links, actors, dates, integers, fractions):
    #     data = {
    #         'cover': cover.get('data-src'),
    #         'name': name.get_text(),
    #         'link': 'http://maoyan.com'+link.get('href'),
    #         'actor': actor.get_text().strip(),
    #         'date': date.get_text(),
    #         'score': integer.get_text()+fraction.get_text()
    #     }
        print '''
{cover: %s,
name: %s,
link: %s,
actor: %s,
date: %s,
score: %s,
category: %s,
duration: %s,
introduce: %s,
comments: %s}''' % (data['cover'], data['name'], data['link'], data['actor'], data['date'], data['score'], data['category'], data['duration'], data['introduce'], data['comments'])
    return boards


def save_to_sqlite3(url, page):
    boards = get_board(url)
    conn = sqlite3.connect("maoyanDB.db")
    print "Opened database successfully"

    c = conn.cursor()
    c.execute("PRAGMA foreign_keys = ON")

    c.execute('''CREATE TABLE if not exists board
        (id integer primary key autoincrement,
        cover char,
        name text,
        link char,
        actor text,
        date text,
        score char)''')

    c.execute('''CREATE TABLE if not exists comment
        (id integer primary key autoincrement,
        headportrait char,
        name char,
        date char,
        comment text,
        praise char,
        board_id integer,
        FOREIGN KEY(board_id) REFERENCES board(id))''')        

    for board in boards:
        c.execute('INSERT INTO board (cover, name, link, actor, date, score) VALUES (?,?,?,?,?,?)', (board['cover'], board['name'], board['link'], board['actor'], board['date'], board['score']))
        print 'insert board: %s' % board['name']
        
        boardid = c.lastrowid
        for comm in board['comments']:
            c.execute('INSERT INTO comment (headportrait, name, date, comment, praise, board_id) VALUES (?,?,?,?,?,?)', (comm['headpor'], comm['name'], comm['date'], comm['comment'], comm['praise'], boardid))
            print 'insert comment: %s' % comm['name']

    conn.commit()
    conn.close()
    print "insert page %s successfully" % (page)

def get_detail_info(url, data):
    html = get_url(url)
    soup = BeautifulSoup(html, 'html.parser')

    category = soup.select('.ename.ellipsis')
    last = soup.select('.ellipsis')
    introduce = soup.select('.dra')
    headpos = soup.select('.portrait-container div.portrait img')
    names = soup.select('.user span.name')
    dates = soup.select('.time span')
    comments = soup.select('.comment-content')
    praises = soup.select('.num')

    short_comments = []
    for headpo, name, date, comment, praise in zip(headpos, names, dates, comments, praises):
        comment = {
            'headpor': headpo.get('src'),
            'name': name.get_text(),
            'date': date.get('title'),
            'comment': comment.get_text(),
            'praise': praise.get_text()
        }
        short_comments.append(comment)
    
    data['category'] = category[0].get_text()
    data['duration'] = last[1].get_text()
    data['introduce'] = introduce[0].get_text()
    data['comments'] = short_comments
    return data

def get_more_pages(start, end):
    for page in range(start, end):
        if page==1:
            url = 'http://maoyan.com/board/4?'
        else:
            url = 'http://maoyan.com/board/4?offset=%s' % ((page-1)*10)
        save_to_sqlite3(url, page)
    
url = 'http://maoyan.com/board'
get_more_pages(1,10)