import urllib2
import os

#request = urllib2.Request("https://image.baidu.com/search/index?tn=baiduimage&ipn=r&ct=201326592&cl=2&lm=-1&st=-1&fm=result&fr=&sf=1&fmq=&pv=&ic=0&nc=1&z=&se=&showtab=0&fb=0&width=&height=&face=0&istype=2&ie=utf-8&ctd=&word=%E5%AE%9D%E8%8E%B2%E7%81%AF%E5%B0%8F%E7%8E%89")
request = urllib2.Request("https://list.jd.com/list.html?cat=9987,653,655")
response = urllib2.urlopen(request)
html = response.read()


from HTMLParser import HTMLParser
from htmlentitydefs import name2codepoint

urls = []
class MyHTMLParser(HTMLParser):
    def handle_starttag(self, tag, attrs):
        #print "Start tag:", tag
        if tag=="img":
            #if attrs[0][0]=="class" and attrs[1][0]=="data-imgurl" and attrs[2][0]=="src" and attrs[3][0]=="style":
            for attr in attrs:
                if attr[0] == "src":
                    k, v = attr
                    print "url:'https:%s'" % v
                    urls.append('https:'+v)
        print urls
    # def handle_endtag(self, tag):
    #     print "End tag:", tag

    # def handle_data(self, data):
    #     print "Data:", data

    # def handle_comment(self, data):
    #     print "Comment:", data

    # def handle_entityref(self, name):
    #     c = unichr(name2codepoint[name])
    #     print "Named ent:", c

    # def handle_charref(self, name):
    #     if name.startswith('x'):
    #         c = unichr(int(name[1:], 16))
    #     else:
    #         c = unichr(int(name))
    #     print "Num ent:", c

    # def handle_decl(self, data):
    #     print "Decl:", data

parser = MyHTMLParser()
#parser.feed('<img class="main_img img-hover" data-imgurl="https://ss1.bdstatic.com/70cFuXSh_Q1YnxGkpoWK1HF6hhy/it/u=2964039308,454155981&amp;fm=23&amp;gp=0.jpg" src="https://ss1.bdstatic.com/70cFuXSh_Q1YnxGkpoWK1HF6hhy/it/u=2964039308,454155981&amp;fm=23&amp;gp=0.jpg" style="background-color: rgb(219, 191, 178); width: 268px; height: 201px;">')
#parser.feed('<img class="main_img img-hover" data-imgurl="https://ss0.bdstatic.com/70cFvHSh_Q1YnxGkpoWK1HF6hhy/it/u=1525079380,2700088424&amp;fm=23&amp;gp=0.jpg" src="https://ss0.bdstatic.com/70cFvHSh_Q1YnxGkpoWK1HF6hhy/it/u=1525079380,2700088424&amp;fm=23&amp;gp=0.jpg" style="background-color: rgb(219, 191, 178); width: 268px; height: 201px;">')
#parser.feed('<img width="220" height="220" data-img="1" src="//img13.360buyimg.com/n7/jfs/t3502/149/1442706783/302122/91048536/5825a5a6Nde8ecb75.jpg" title="双镜头，大内存，长续航！【点我给你看颜值，戳我到会场！】">')
parser.feed(html)


import requests
i = 0
for url in urls:
    urlrequest = urllib2.Request(url)
    urlresponse = urllib2.urlopen(urlrequest)
    data = urlresponse.read()
    
    pic = requests.get(url)
    string = 'images\\'+str(i)+'.jpg'
    fp = open(string, 'wb')
    fp.write(pic.content)
    fp.close()
    i+=1

