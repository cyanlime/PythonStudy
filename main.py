#!/usr/bin/env python 3.1

print "global: it's beginning"
j = 1
print "global: j = %s" % j

def func1():
    i = 1
    print "func1: i = %s" % i
    def func2():
        i = 2
        print "func2: i = %s" % i
    return func2

if __name__ == '__main__':
    var1 = func1()
    var1()
    print "main: it's over"