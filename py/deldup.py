#!/usr/bin/env python 3.1


def plus():
    dic = {}
    sum = 0
    for item in a:
        if item not in dic.keys():
            dic[item]=1
        else:
            dic[item]+=1
    print dic

    for item2 in dic.keys():
        dic[item2]=dic[item2]%2
        sum+=item2*dic[item2]
    print dic
    return sum

if __name__ == "__main__":
    a = [1, 2, 3, 4, 5, 6, 2, 3, 2, 5, 4, 3, 1, 1, 1, 2, 1]
    sum = plus()
    print sum 