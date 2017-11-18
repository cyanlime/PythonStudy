def least_common_mul(num1, num2):
    for item in range(1, num2+1):
        for item2 in range (1, num1+1):
            if num1*item==num2*item2:
                return num1*item

def getCubeRoot(num):
    for item in range(1, num+1):
        if item*item*item==num:
            return item, num

def count(array):
    positives = []
    negative = 0
    sum = 0
    for item in array:
        if item<0:
            negative+=1
        else:
            positives.append(item)
    for item in positives:
        sum+=item
    return negative, float(sum/len(positives))

def plumpile(string):
    dic = []
    piles = []
    for item in range(len(string)-1):
        piles.append(string[item])
        for item2 in range(item+1, len(string)):
            if string[item2]>string[item]:
                piles.append(string[item2])
        dic.append(piles)
        piles = []
    
    paths = []
    path = []
    for values in dic:
        value = values[0]
        for item in range(1, len(values)):
            if len(path)==0:
                path.append(value)
            for item2 in range(item, len(values)):
                if len(path)==1:
                    if values[item2]>value and value<values[len(values)-1]:
                        path.append(values[item2])
                else:
                    if values[item2]>path[len(path)-1] and value<values[len(values)-1]:
                        path.append(values[item2])
            paths.append(path)
            path = []
        if len(values)==1:
            paths.append(values)

    maxlen = len(paths[0])
    for path in paths:
        if len(path)>maxlen:
            maxlen=len(path)
            origin_path = path
    return maxlen, origin_path

if __name__ == "__main__":
    print least_common_mul(6,12)
    item, num = getCubeRoot(27)
    print "%s^3=%s" % (item, num)
    print count([-13, -4, -7, 1, 3, 5, 3])
    print plumpile('25154576534567')