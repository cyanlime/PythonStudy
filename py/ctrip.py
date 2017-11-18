import urllib2
from bs4 import BeautifulSoup

"""
http://you.ctrip.com/sight/newyork248/s0-p2.html#sightname
http://you.ctrip.com/sight/newyork248/s0-p3.html#sightname
http://you.ctrip.com/sight/newyork248/s0-p1.html
http://you.ctrip.com/sight/newyork248/s0-p5.html#sightname
"""

# request = urllib2.Request('http://image.baidu.com/search/flip?tn=baiduimage&ie=utf-8&word=%E5%AE%9D%E8%8E%B2%E7%81%AF%E5%B0%8F%E7%8E%89&pn=20&gsm=3c&ct=&ic=0&lm=-1&width=0&height=0')
# response = urllib2.urlopen(request)
# html = response.read()

# soup = BeautifulSoup(html, "html.parser")
# names = soup.select('body > input > input > div.ttd2_background > div > div.des_wide.f_right > div:nth-of-type(2) > div.list_wide_mod2 > div > div.rdetailbox > dl > dt > a')
# ranks = soup.select('body > input > input > div.ttd2_background > div > div.des_wide.f_right > div:nth-of-type(2) > div.list_wide_mod2 > div > div.rdetailbox > dl > dt > s')
# scores = soup.select('body > input > input > div.ttd2_background > div > div.des_wide.f_right > div:nth-of-type(2) > div.list_wide_mod2 > div > div.rdetailbox > ul > li:nth-of-type(1) > a > strong')
# images = soup.select('div.leftimg')
# print names
# while len(ranks)<15:
#     ranks.append('')

# sites = []
# for image, name, rank, score in zip(images, names, ranks, scores):
#     data = {
#         #'image': image.get('src'),
#         'image': image.a.contents[1].get('src'),
#         'name': name.get_text(),
#         'score': score.get_text()
#     }
#     if rank == '':
#         data['rank'] = rank
#     else:
#         data['rank'] = rank.get_text()
#     sites.append(data)
# print page

def get_page(url, page):
    request = urllib2.Request(url)
    response = urllib2.urlopen(request)
    html = response.read()

    soup = BeautifulSoup(html, "html.parser")
    names = soup.select('body > input > input > div.ttd2_background > div > div.des_wide.f_right > div:nth-of-type(2) > div.list_wide_mod2 > div > div.rdetailbox > dl > dt > a')
    ranks = soup.select('body > input > input > div.ttd2_background > div > div.des_wide.f_right > div:nth-of-type(2) > div.list_wide_mod2 > div > div.rdetailbox > dl > dt > s')
    scores = soup.select('body > input > input > div.ttd2_background > div > div.des_wide.f_right > div:nth-of-type(2) > div.list_wide_mod2 > div > div.rdetailbox > ul > li:nth-of-type(1) > a > strong')
    images = soup.select('div.leftimg')
    while len(ranks)<15:
        ranks.append('')
    while len(scores)<15:
        scores.append('')
  
    sites = []
    for image, name, rank, score in zip(images, names, ranks, scores):
        data = {
            'image': image.a.contents[1].get('src'),
            'name': name.get_text(),
        }
        if rank == '':
            data['rank'] = rank
        else:
            data['rank'] = rank.get_text()
        if score == '':
            data['score'] = score
        else:
            data['score'] = score.get_text()
        sites.append(data)
    dic[page] = sites
    print page
    return sites

def save_images(sites):
    import requests
    import uuid
    #i = 0
    for site in sites:
        pic = requests.get(site['image'])
        #string = 'images/NewYork/'+str(i)+'.jpg'
        string = 'images/NewYork/'+str(uuid.uuid4())+'.jpg'
        with open(string, 'wb') as fp:
            fp.write(pic.content)
        # i+=1

def get_more_page(start, end):
    for page in range(start, end):
        url = 'http://you.ctrip.com/sight/newyork248/s0-p%s.html' % page
        if page==1:
            url = url
        else:
            url = url+'#sightname'
        sites = get_page(url, page)
        import time
        time.sleep(2)
        save_images(sites)

dic = {}
get_more_page(1, 39)
print dic
print "scrapy over"