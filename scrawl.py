import urllib2
from bs4 import BeautifulSoup

request = urllib2.Request('https://search.jd.com/Search?keyword=%E5%A3%81%E7%94%BB&enc=utf-8&wq=%E5%A3%81%E7%94%BB&pvid=e3ecf5298e5649389ab135f186810927')
#request = urllib2.Request('https://image.baidu.com/search/flip?tn=baiduimage&ie=utf-8&word=%E5%AE%9D%E8%8E%B2%E7%81%AF%E5%B0%8F%E7%8E%89&ct=201326592&ic=0&lm=-1&width=&height=&v=flip')
response = urllib2.urlopen(request)
html = response.read()

soup = BeautifulSoup(html, "html.parser")
#print soup
"""
//*[@id="imgid"]/ul/li[17]/a/img
#imgid > ul > li:nth-child(17) > a > img

body.flip > div#wrapper > div#imgContainer > div#imgid > ul.imglist > li.imgitem > a.imglink > img
#imgid > ul > li:nth-child(19) > a > img
"""

#imgid > ul > li:nth-child(1) > img
#imgid > ul > li:nth-child(8) > a > img

#J_goodsList > ul > li:nth-child(1) > div > div.p-img > a > img
#J_goodsList > ul > li:nth-child(2) > div > div.p-img > a > img

"""
#J_goodsList > ul > li:nth-child(3) > div > div.p-img > a > img
#J_goodsList > ul > li:nth-child(1) > div > div.p-price > strong > i
#J_goodsList > ul > li:nth-child(5) > div > div.p-price > strong > i
#J_goodsList > ul > li:nth-child(1) > div > div.p-name.p-name-type-2
#J_goodsList > ul > li:nth-child(3) > div > div.p-name.p-name-type-2
#J_goodsList > ul > li:nth-child(4) > div > div.p-name.p-name-type-2
"""
#image = soup.select('#J_goodsList > ul > li:nth-of-type(1) > div > div.p-img > a > img')
images = soup.select('#J_goodsList > ul > li > div > div.p-img > a > img')
prices = soup.select('#J_goodsList > ul > li > div > div.p-price > strong > i')
descs = soup.select('#J_goodsList > ul > li > div > div.p-name.p-name-type-2')

#image = soup.select('html > body.flip > div#wrapper > div#imgContainer > div#imgid > ul.imglist > li.imgitem > a.imglink > img')
#image = soup.select('#imgid > ul > li:nth-of-type(8) > a > img')

#print image, price, desc

for image, price, desc in zip(images, prices, descs):
    if image.get('src'):
        data = {
            'image': 'https:'+image.get('src'),
            'price': price.get_text(),
            #'desc': 'desc.get_text()
        }
        print data