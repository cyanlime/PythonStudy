def octal_format(num):
    quto = num/8
    remainder = num%8
    if quto>0:
        return int(str(quto)+str(remainder)), num
    else:
        return remainder, num

def symmatrix(arrays):
    num = 0
    for item in range(len(arrays)):
        for item2 in range(len(arrays[item])):
            if arrays[item][item2]==arrays[item2][item]:
                num+=1
    if num == len(arrays)*len(arrays):
        return "yes!"
    else:
        return "no!"

def youngest():
    print "please input the number of data:"
    number = int(raw_input())
    
    arrays = []
    while len(arrays)<number:
        print "please input the %s information of employee:" % (str(len(arrays)+1)+'th')
        info = raw_input()

        info_tuple = (None,None,None)
        word = []
        words = []
        for item in range(len(info)):
            if info[item]!=' ':
                word.append(str(info[item]))
            if info[item]==' ' or item==len(info)-1:
                infoword = ''.join(map(lambda x: str(x), word))
                words.append(infoword)
                word = []
        info_tuple = (words[0],words[1],int(words[2]))
        arrays.append(info_tuple)
    #print arrays

    for item in range(len(arrays)):
        for item2 in range(item+1, len(arrays)):
            #id2, name2, age2 = arrays[item2]
            if arrays[item][2]>arrays[item2][2]:
                temp = arrays[item]
                arrays[item] = arrays[item2]
                arrays[item2] = temp                
    return arrays[:3]

if __name__ == "__main__":
    # value, num = octal_format(25)
    # print "octal format of %s: %s" % (num, value)

    # print symmatrix([[16,19,16,6],[19,16,14,5],[16,14,16,3],[6,5,3,16]])
    # print symmatrix([[1,2],[3,4]])

    # print youngest([(1,'codemeow',24),(2,'cyanlime',21),(3,'sara',25),(4,'brenda',23),(5,'mick',21)])
    # youngest = youngest([(501,'Jack',6),(102,'Nathon',100),(599,'Lily',79),(923,'Lucy',15),(814,'Mickle',65)])
    # for item in youngest:
    #     print '%s %s %s' % (item[0], item[1], item[2])
    youngest = youngest()
    for item in youngest:
        print '%s %s %s' % (item[0], item[1], item[2])