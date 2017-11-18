def next_bigger(array):
    next_bigger_factors = []
    for item in range(len(array)):
        for item2 in range(item+1, len(array)):
            if array[item2]>array[item]:
                next_bigger_factors.append(array[item2])
                break
        if item2==len(array)-1 and array[item2]<=array[item]:
            next_bigger_factors.append(-1)
    return next_bigger_factors

def next_min_bigger(array):
    next_min_bigger_factors = []
    for item in range(len(array)):
        min_bigger = -1
        for item2 in range(item+1, len(array)):
            if min_bigger==-1:
                if array[item2]>array[item]:
                    min_bigger = array[item2]
            else:
                if array[item]<array[item2]<min_bigger:
                    min_bigger = array[item2]
        next_min_bigger_factors.append(min_bigger)
    return next_min_bigger_factors


def words_distance(array, word1, word2):
    dic = {}
    for item in range(len(array)):
        if array[item]==word1 or array[item]==word2:
            if array[item] not in dic:
                dic[array[item]]=[]
                dic[array[item]].append(item)
            else:
                dic[array[item]].append(item)

    distance = {}
    for item in dic[word1]:
        for item2 in dic[word2]:
            if item-item2 not in distance:
                distance[item-item2] = []
                distance[item-item2].append((item, item2))
            else:
                distance[item-item2].append((item, item2))

    index = {}
    min = distance.keys()[0]
    for key in distance.keys():
        if (min>0 and 0<key<min) or (min<0 and 0>key>-min):
            min = key
    index[(word1, word2)] = []
    index[(word1, word2)].append(distance[min])
    
    for key in distance.keys():
        if key==-min:
            index[(word1, word2)].append(distance[key])
    return min, index

def realtime_median(array):
    medians = []
    for item in range(len(array)):
        medians.append(array[item/2])
    return medians


#  1, 2,-1
#  3, 4,-5
# -5,-6,-7

def two_appear(num):
    appears = []
    time = 0
    for number in range(num+1):
        for item in range(len(str(number))):
            if '2' in str(number)[item]:
                appears.append(number)
                break
    return appears, len(appears)

def integer_pair(array, num):
    pairs = []
    for item in range(len(array)):
        for item2 in range(item+1, len(array)):
            if array[item]+array[item2]==num:
                pairs.append((array[item], array[item2]))
    return pairs, len(pairs)

def series_sum(array):
    sums = []
    sum = 0
    item = 0
    while item<len(array):
        while array[item]>0 and item<len(array)-1:
            sum+=array[item]
            item+=1
        if item==len(array)-1:
            if array[item]>0:
                sum+=array[item]
                sums.append(sum)
            else:
                sums.append(sum)
            break
        else:
            if array[item]<0 and sum!=0:
                sums.append(sum)
                item+=1
                sum = 0
                series = []
                continue
            if array[item]<0 and sum==0:
                item+=1
                continue
    return sums

def min_adjust(array):
    item = 0
    item2 = len(array)-1
    adjust = []
    while array[item]<array[item+1] and item<len(array)-2:
        item+=1
    if item==len(array)-2 and array[item]<array[item+1]:
        return [0,0]
    if item<len(array)-1:
        while array[item2]>array[item2-1]:
            item2-=1
        return [item, item2]

def factorial(num):
    product = 1
    for item in range(1, num+1):
        product*=item

    zeronum = 0
    zero_appear = 0
    if str(product)[len(str(product))-1]=='0':
        for item2 in range(len(str(product))-1, -1, -1):
            if str(product)[item2]=='0':
                zeronum+=1
                continue
            else:
                return zeronum
    else:
        return zeronum

def mastermind(str1, str2):
    guess_right = 0
    fake_guess_right = 0
    strings1 = []
    strings2 = []
    for item in range(len(str1)):
        if str2[item]==str1[item]:
            guess_right+=1
        else:
            strings1.append(str1[item])
            strings2.append(str2[item])

    for char in strings1:
        if char in strings2:
            fake_guess_right+=1
    return [guess_right, fake_guess_right]


def first_appear_once_char(string):
    leaps = []
    for item in range(len(string)):
        for item2 in range(item+1, len(string)):
            if string[item] not in leaps:
                if string[item2]==string[item]:
                    leaps.append(string[item])
                    break
            else:
                break
        if item2==len(string)-1 and string[item2]!=string[item] and (string[item] in leaps):
            return string[item2]
        if item2==len(string)-1 and string[item2]!=string[item] and (string[item] not in leaps):
            return string[item]

if __name__ == "__main__":
    print next_bigger([11,13,10,5,12,21,3])
    print next_min_bigger([11,13,10,5,12,21,3])
    print words_distance(['hello', 'word', 'min', 'well', 'hello', 'know', 'hello', 'know', 'courage', 'max', 'hello', 'know'], 'know', 'hello')
    print realtime_median([1,2,3,4,5,6])
    print two_appear(1000)
    print integer_pair([1,2,3,4,5], 6)
    print series_sum([1,2,3,-6,1,7,4,-3,-4,2,4,5,6,-7,8,9,-5])
    print min_adjust([1,4,5,9,5,9])
    print factorial(10)
    print mastermind('RGBY','GGRR')
    print first_appear_once_char('tteefgggggkkjjef')