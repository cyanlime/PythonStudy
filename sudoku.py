def about_seven(max):
    item = 7
    sevens = []
    for num in range(7, max+1):
        if num%7==0:
            sevens.append(num)
        else:
            for item in range(len(str(num))):
                if str(num)[item]=='7' or num%7==0:
                    sevens.append(num)
                    break
    return sevens

def perfect_num(max):
    perfects = {}
    for num in range(2,max+1):
        factors = []
        sum = 0
        for item in range(1, num):
            if num%item==0:
                factors.append(item)
        for fact in factors:
            sum+=fact
        if sum==num:
            perfects[num]=factors
    return perfects

def find_appear_once(string):
    dic = {}
    for item in range(len(string)):
        if string[item] not in dic:
            dic[string[item]]=1
        else:
            dic[string[item]]+=1
    
    once_keys = []
    for key, value in dic.items():
        if value==1:
            once_keys.append(key)

    if len(once_keys)==0:
        return -1
    else:
        for item in range(len(string)):
            if string[item] in once_keys:
                return string[item]

import math
def primesum(num):
    primes = []
    for item in range(2, num):
        leap = 0
        for item2 in range(2, int(math.sqrt(item))+1):
            if item%item2==0:
                leap = 1
                break
        if leap==0:
            primes.append(item)

    dic = {}
    for item in range(len(primes)):
        for item2 in range(item+1, len(primes)):
            if primes[item]+primes[item2]==num:
                dic[primes[item2]-primes[item]]=[]
                dic[primes[item2]-primes[item]].append(primes[item])
                dic[primes[item2]-primes[item]].append(primes[item2])
                break

    min = dic.keys()[0]
    for key in dic.keys():
        if key<min:
            min = key
    return dic[min]

if __name__ == '__main__':
    print about_seven(100)
    # perfects = perfect_num(1000)
    # for key, values in perfects.items():
    #     print "%s=%s" % (key, '+'.join(map(lambda x: str(x), values)))
    print find_appear_once('aabybccdeef')
    print primesum(20)