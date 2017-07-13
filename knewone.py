import urllib
import urllib2
from bs4 import BeautifulSoup

url = 'http://weibo.com/1686709997/Fazdk0VWT?ref=feedsdk&type=comment#_rnd1499076557504'
# url = 'http://photo.weibo.com/3669102477/talbum/index#!/mode/1/page/1'
# headers = {
#     'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_0) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/59.0.3071.115 Safari/537.36'
# }
# values = {
#     'cookie': '_s_tentry=www.liaoxuefeng.com; Apache=4432793094714.868.1493618220022; SINAGLOBAL=4432793094714.868.1493618220022; ULV=1493618221017:1:1:1:4432793094714.868.1493618220022:; login_sid_t=256499508647ab747929fb69c9e5a0bc; SCF=Agc6VAVCNWpO0F_Msebp7v-okDUvl7DAIK0Kpeqgeo4AFALP_gZpfwecp_l13s4XQM1Lr-8FafheWVgd6suSEI0.; SUB=_2A250XnqSDeRhGeRM4lUV9i3EzzuIHXVXKutarDV8PUJbmtAKLXHDkW97yXBBl9swHRITFXm6QnRkv8HCOQ..; SUBP=0033WrSXqPxfM725Ws9jqgMF55529P9D9W5xEndKQCTWfVUu4mzLuFBd5JpX5K2hUgL.FozE1KMXSoeRShM2dJLoIEnLxKML1K-L1h-LxKqL1--LB-zLxKnL12eL1-eLxK.L1-qLBo-7eK5c; SUHB=0qj1960ym4fPIs; SSOLoginState=1499073218; un=15216113863; WBStorage=e6c9073a1a48ae73|undefined; wvr=6; UOR=,,www.liaoxuefeng.com'
# }
# data = urllib.urlencode(values)
# request = urllib2.Request(url, headers=headers, data=data)

request = urllib2.Request(url)
response = urllib2.urlopen(request)
html = response.read()

soup = BeautifulSoup(html, 'html.parser')
#pics = soup.select('div.thumbnail-cover img')
pics = soup.select('div.WB_face W_fl')
print pics

data = {
    'pic': pics[0].get('src')
}