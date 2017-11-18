def coordinate(string):
    operates = []
    array = []
    isalp = 0
    isnum = 0
    issemi = 0
    nums = ['1','2','3','4','5','6','7','8','9','0']
    for item in range(len(string)):
        if (string[item]=='A' or string[item]=='D' or string[item]=='W' or string[item]=='S') and isalp==0 and (issemi==1 or item==0):
            array.append(string[item])
            isalp+=1
            continue
        elif (string[item] in nums) and isalp==1 and isnum<=2:
            array.append(string[item])
            isnum+=1
            continue
        elif string[item]==';':
            if isalp==1 and isnum<=2:
                array.append(string[item])
                operates.append(array)
            isalp=0
            isnum=0
            issemi=1
            array = []
            continue
        else:
            isalp=0
            isnum=0
            array = []
            issemi=0
            continue

    x=0
    y=0
    for item in operates:
        value = int(item[1]+item[2])
        if item[0]=='A':
            x-=value
        if item[0]=='D':
            x+=value
        if item[0]=='W':
            y+=value
        if item[0]=='S':
            y-=value
    return x,y

if __name__ == "__main__":
    x,y = coordinate('A10;S20;W10;D30;X;A1A;A10A11;;A10;')
    print "(%s,%s)" % (x,y)