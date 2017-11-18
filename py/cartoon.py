# -*- coding: utf-8 -*-

import requests
from bs4 import BeautifulSoup
from requests.exceptions import HTTPError
import re
import sqlite3
import os
import json

def get_url(url):
    try:
        response = requests.get(url)
        if response.status_code==200:
            return response.text
        return None
    except HTTPError, e:
        print "request error"
        return None

def get_page(url, page):
    day_cartoons = []
    html = get_url(url)

    covers = re.findall('<img data-kksrc="(.*?)"', html, re.S)
    links = re.findall('<div class="topic-tit"><a href="(.*?)"', html, re.S)
    titles = re.findall('<div class="topic-tit">.*? title="(.*?)"', html, re.S)
    authors = re.findall('<div class="topic-title fl-left">(.*?)</div>', html, re.S)
    praises = re.findall('<div class="praise ico-praise fl-right">(.*?)</div>', html, re.S)

    for cover, link, title, author, praise in zip(covers, links, titles, authors, praises):
        data = {
            'cover': cover,
            'link': 'http://www.kuaikanmanhua.com'+link,
            'title': title,
            'author': author,
            'praise': praise
        }
        data = get_cartoon(data['link'], data)
        day_cartoons.append(data)
        with open('kuaikan.txt', 'a') as fp:
            fp.write(json.dumps(data) + '\n')
        print '''
{cover: %s,
link: %s,
title: %s,
introduce: %s,
author: %s,
praise: %s,
cartoons: %s}
''' % (data['cover'], data['link'], data['title'], data['introduce'], data['author'], data['praise'], data['cartoons'])
    return day_cartoons


def save_to_sqlite3(url, page):
    day_cartoons = get_page(url, page)
    conn = sqlite3.connect("kuaikanDB.db")
    print "Opened database successfully"

    c = conn.cursor()
    c.execute("PRAGMA foreign_keys = ON")

    c.execute('''CREATE TABLE if not exists cartoon
        (id integer primary key autoincrement,
        cover char,
        title char,
        link char,
        author char,
        introduce text,
        praise char)''')

    c.execute('''CREATE TABLE if not exists period
        (id integer primary key autoincrement,
        subcover char,
        subtitle char,
        sublink char,
        subdate char,
        subpraise char,
        cartoon_id integer,
        FOREIGN KEY(cartoon_id) REFERENCES cartoon(id))''')        

    for daycartoon in day_cartoons:
        c.execute('INSERT INTO cartoon (cover, title, link, author, introduce, praise) VALUES (?,?,?,?,?,?)', (daycartoon['cover'], daycartoon['title'], daycartoon['link'], daycartoon['author'], daycartoon['introduce'], daycartoon['praise']))
        print 'insert cartoon: %s' % daycartoon['title']
        
        cartoonid = c.lastrowid
        for percart in daycartoon['cartoons']:
            c.execute('INSERT INTO period (subcover, subtitle, sublink, subdate, subpraise, cartoon_id) VALUES (?,?,?,?,?,?)', (percart['subcover'], percart['subtitle'], percart['sublink'], percart['subdate'], percart['subpraise'], cartoonid))
            print 'insert period cartoon: %s' % percart['subtitle']

    conn.commit()
    conn.close()
    print "insert page %s successfully" % (page)

def get_cartoon(url, data):
    html = get_url(url)
    introduce = re.findall('<div class="switch-content">\s*<p>(.*?)</p>', html, re.S)
    sub_covers = re.findall('<img src="(.*?)".*? class="kk-sub-img">', html, re.S)
    sub_titles = re.findall('<tr>.*?class="tit">\s*<a class="".*? title="(.*?)"', html, re.S)
    sub_links = re.findall('<tr>.*?class="tit">\s*<a class="" href="(.*?)"', html, re.S)
    sub_praises = re.findall('alt="praise">\s*</i>\s*(.*?)\s*</td>', html, re.S)
    sub_dates = re.findall('<td>(.*?)</td>', html, re.S)

    cartoons = []
    for subcover, subtitle, sublink, subpraise, subdate in zip(sub_covers, sub_titles, sub_links, sub_praises, sub_dates):
        cartoon = {
            'subcover': subcover,
            'subtitle': subtitle,
            'sublink': 'http://www.kuaikanmanhua.com'+sublink,
            'subpraise': subpraise,
            'subdate': subdate
        }
        #cartoon = get_peroid_comments(cartoon['sublink'], cartoon)
        cartoons.append(cartoon)

    data['cartoons'] = cartoons
    data['introduce'] = introduce[0]
    return data

def get_more_pages(start, end):
    for page in range(start, end):
        url = 'http://www.kuaikanmanhua.com/?pos=%s' % page
        save_to_sqlite3(url, page)

get_more_pages(0,1)