#!/usr/bin/python
a = 'abcdef'
print list(a)

def string_reverse(string):
    liststr = list(string)
    strs = []
    while len(strs)<len(string):
        s = liststr.pop(len(liststr)-1)
        strs.append(s)
    return ''.join(map(lambda x: str(x), strs))

print string_reverse('abcdef')

"""
升序合并如下两个list, 并去除重复的元素:
list1 = [2, 3, 8, 4, 9, 5, 6]
list2 = [5, 6, 10, 17, 11, 2]
"""

def merger_sort(list1, list2):
    for item in list2:
        if item not in list1:
            list1.append(item) 
    return qsort(list1)

import random
def qsort(l):
    if len(l)<2:
        return l
    e = random.choice(l)
    small = [i for i in l if i<e]
    large = [i for i in l if i>e]
    #print 'small:%s, large:%s, e:%s' % (small, large, e)
    return qsort(small)+[e]+qsort(large)

list1 = [2, 3, 8, 4, 9, 5, 6]
list2 = [5, 6, 10, 17, 11, 2]
print merger_sort(list1, list2)

x = [0, 1]
i = 0
i, x[i] = 1, 2
print x




a = [2, 3, 8, 4, 9, 5, 6]
print a[:-2]
b = [5, 6, 10, 17, 11, 2, 1]

Source = a+b
Source.sort()
print 'source:%s' % Source

def mean(Source):
    if not Source:
        return ([], [])
    Big = Source[len(Source)-1]
    Small = Source[len(Source)-2]
    Max, Min = mean(Source[:-2])
    Max.append(Small)
    Min.append(Big)
    return Max, Min

print mean(Source)

print a[::2]
print a[:-2]

a = [2, 3, 8, 4, 9, 5, 6]
#print sum(i+3 for i in a[::2])
print sum(a)
print sum([a[i]+3 for i in range(0,len(a),1)])

"""
找出数组中出现次数超过数组长度一半的值并打印，例如: [0, 2, 4, 5, 2, 2, 2], 2 出现的次数为 4 并超过数组长度一半，则输出 2
"""
dic = {}
array = [0, 2, 4, 5, 2, 2, 2]
for num in array:
    if num in dic:
        dic[num]+=1
        if dic[num]>len(array)/2:
            print num
    else:
        dic[num]=1

"""
已知字符串的字符是各不相同的，求任意拼接的所有组合。例：’ab’, 则输出’aa’, ‘ab’, ‘ba’, ‘bb’
"""
string = 'ab'
for item in list(string):
    for item2 in list(string):
        print item+item2

"""
20 个降序排列数组, 每个包含 500 个数字, 找出其中 500 个最大的数字
"""
import random
twenty_list = []
for item in range(20):
    array = []
    for i in range(500):
        num = random.randint(0, 2000)
        array.append(num)
    array.sort(reverse=True)
    twenty_list.append(array)
print twenty_list

import os
def print_directory_contents(sPath):
    dirs = os.listdir(sPath)
    for sChild in dirs:
        sChildPath = os.path.join(sPath, sChild)
        if os.path.isdir(sChildPath):
            print_directory_contents(sChildPath)
        else:
            print content


A0 = dict(zip(('a','b','c','d','e'),(1,2,3,4,5)))
for i in range(10):
    if i in A0:
        print i


a = [1,2,3,4,5,6]
print a[::2], a[-2:]

"""一行代码实现对列表a中的偶数位置的元素进行加3后求和"""

print sum([a[i]+3 for i in a[i] if i%2==0])