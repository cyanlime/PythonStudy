def singleton(cls, *arg, **kw):
    instances = {}
    def _singleton():
        if cls not in instances:
            instances[cls] = cls(*arg, **kw)
            return instances[cls]
    return _singleton

class singleton():
    def __new__(cls, *args, **kw):
        if not hasattr(cls, '_instance'):
            cls._instance = super(singleton, cls).__new__(cls, *args, **kw)
            return cls._instance

def str2int(s):
    def fn(x, y):
        return x * 10 + y
    def char2num(s):
        return {'0': 0, '1': 1, '2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9}[s]
    return reduce(fn, map(char2num, s))
print str2int('13579')

"""
利用map()函数，把用户输入的不规范的英文名字，变为首字母大写，其他小写的规范名字。输入：['adam', 'LISA', 'barT']，输出：['Adam', 'Lisa', 'Bart']
"""
L = ['adam', 'LISA', 'barT']
print map(lambda x: x[0].upper()+x[1:len(x)].lower(), L)
print [x[0].upper()+x[1:len(x)].lower() for x in L]

"""请编写一个prod()函数，可以接受一个list并利用reduce()求积。"""

def prod(x, y):
    return x*y
print reduce(prod, [1,2,3,4,5])

"""尝试用filter()删除1~100的素数。"""
import math
def primenum(num):
    if num==1:
        return num==num
    for n in range(2, int(math.sqrt(num))+1):
        if num%n==0 and n!=num:
            return num%n==0
print filter(primenum, range(1, 101))

def count():
    fs = []
    for i in range(1, 4):
        def f(j):
            def g():
                return j*j
            return g
        fs.append(f(i))
    return fs

f1, f2, f3 = count()
print f1(), f2(), f3()


def log(text):
    def decorator(func):
        def wrapper(*args, **kw):
            print '%s %s():' % (text, func.__name__)
            return func(*args, **kw)
        return wrapper
    return decorator

@log('execute')
def now():
    print '2013-12-25'

now()

class Dict(dict):

    def __init__(self, **kw):
        super(Dict, self).__init__(**kw)

    def __getattr__(self, key):
        try:
            return self[key]
        except KeyError:
            raise AttributeError(r"'Dict' object has no attribute '%s'" % key)

    def __setattr__(self, key, value):
        self[key] = value

dic = Dict(a=1, b='hi', c='abc')
print dic['a'], dic.a, dic.b, dic.c
print dic['b']

"""编写一个search(s)的函数，能在当前目录以及当前目录的所有子目录下查找文件名包含指定字符串的文件，并打印出完整路径"""
import os
def search(s, path='.'):
    currentdir = os.path.abspath(path)
    files = os.listdir(path)
    for f in files:
        path = os.path.join(currentdir, f)
        if os.path.isfile(path) and s in f:
            print path
        if os.path.isdir(path):
            search(s, path)

search('py')