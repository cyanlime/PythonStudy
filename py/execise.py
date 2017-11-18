array = [1,2,3,4,5,6,7,8,4,2,3,4,2,1,2,4,5,6]

dic = {}
for num in array:
    if num not in dic:
        dic[num]=1
    else:
        dic[num]+=1

print dic

"""
一个dict中的元素按value的值排序输出
"""

sorted(dic.items(), cmp=lambda x, y: cmp(x[1], y[1]))

"""
袜子，10
鞋子，20
拖鞋，30
项链，40
要求随机返回一种商品，要求商品被返回的概率与其库存成正比
"""

dic = {
    '袜子': 10,
    '鞋子': 20,
    '拖鞋': 30,
    '项链': 40
}

# storage = []

# sum = 0
# for value in dic.values():
#     sum+=value

# for key, value in dic.items():
#     for item in range(value*10):
#         storage.append(key)

# import random

# array = []
# while len(array)<100:
#     array.append(random.choice(storage))

# for key in dic.keys():
#     print '%s: %s' % (key, array.count(key))

storage = []
for key, value in dic.items():
    part = [key]*value*10
    storage = storage + part

import random
array = random.sample(storage, 100)

for key in dic.keys():
    print '%s: %s' % (key, array.count(key))

"""
src = "security/afafsff/?ip=123.4.56.78&id=45"，请写一段代码用正则匹配出IP
"""
import re
src = "security/afafsff/?ip=123.4.56.78&id=45"
ip = re.findall('.*/?ip=(.*?)&.*?', src, re.S)[0]
print ip

"""
实现一个stack
"""
class Stack():
    def __init__(self):
        self._items = list()

    def isEmpty(self):
        return len(self)==0

    def __len__(self):
        return len(self._items)

    def peek(self):
        assert not self.isEmpty()
        return self._items[-1]

    def pop(self):
        assert not self.isEmpty()
        return self._items.pop()

    def push(self, item):
        self._items.append(item)

"""
有一个长度是101的数组，存在1~100的数字，有一个是重复的，拿重复的找出来
"""