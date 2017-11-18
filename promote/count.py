"""
统计一篇英文文章内每个单词的出现频率，并返回出现频率最高的前10个单词及其出现次数
"""
import re
with open('promote/test.txt', 'r') as fp:
    text = fp.read()

words = re.split('[0-9\W]+', text) 
"""0-9 nonword split"""

dic = {}
for word in words:
    if word!='':
        if word not in dic:
            dic[word] = 1
        else:
            dic[word]+=1

sorted_dic = sorted(dic.items(), key=lambda x: x[1], reverse=True)
tens = sorted_dic[:10]
print tens

""" """
array = []
for i in range(1, 500):
    array.append(i)

def evenitems(array):
    evens = []
    for item in range(1, len(array), 2):
        evens.append(array[item])
    while len(evens)!=1:
        return evenitems(evens)
    return evens
print evenitems(array)

"""”sports.sina.com.cn”翻转为”cn.com.sina.sports”"""
def revert(url):
    revert_url = list(url)[::-1]
    chars = []
    parts = []
    for item in range(len(revert_url)):
        if revert_url[item]!='.':
            parts.append(revert_url[item])
        if revert_url[item]=='.' or item==len(revert_url)-1:
            chars.extend(parts[::-1])
            if revert_url[item]=='.':
                chars.append(revert_url[item])
                parts = []
    revertstr = ''.join(map(lambda x: str(x), chars))
    return revertstr
print revert('sports.sina.com.cn')

"""3个整数13,312,343,连成的最大整数为:34331213 
又如:4个整数7,13,4,246连接成的最大整数为7424613 
现在给你一个正整数列表L，请你输出用这些正整数能够拼接成的最大整数。"""

def maxint(L, i=1):
    dic = {}
    for item in L:
        key = ''.join(map(lambda x: str(x), str(item)[:i]))
        if key not in dic:
            dic[key] = [] 
        dic[key].append(item)
    print dic
    for k, v in dic.items():
        if len(v)>1:
            return maxint(dic[k], i+1)
    return dic

print maxint([13,312,343,356,457,47,8777,8778])