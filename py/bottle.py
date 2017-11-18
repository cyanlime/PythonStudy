def bottle(num):
    sum = 0
    get = num/3
    rest = num%3
    sum+=get
    while get+rest>=3:
        get = (get+rest)/3
        rest = (get+rest)%3
        sum+=get

    if rest==1 or rest==0:
        return sum, num
    if rest==2:
        return sum+1, num

def del_min_freq(string):
    dic = {}
    for item in range(len(string)):
        if string[item] not in dic:
            dic[string[item]] = 1
        else:
            dic[string[item]]+=1
    
    mins = []
    min = dic.items()[0][1]
    for key, value in dic.items():
        if value<min:
            min = value
    for key, value in dic.items():
        if value==min:
            mins.append(key)

    chars = []
    for item in range(len(string)):
        if string[item] not in mins:
            chars.append(string[item])
    char = ''.join(map(lambda x: str(x), chars))
    return char, string

if __name__ == "__main__":
    get, num = bottle(81)
    print "using %s bottles can get %s bottles" % (num, get)

    char, string = del_min_freq('adsszaabjjdjdjdd')
    print "delete the min times apperance of chars %s: %s" % (string, char)