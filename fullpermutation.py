def swap(x, y):
    temp = x
    x = y
    y = temp
    return x, y


def fullpermutation(string):
    tempstringlist = list(string)
    stringlist = tempstringlist
    for item in range(0, len(stringlist)):
        for item2 in range(item+1, len(stringlist)):
            #new_stringlist = stringlist
            #swap(stringlist[item], stringlist[item2])
            temp = stringlist[item]
            stringlist[item] = stringlist[item2]
            stringlist[item2] = temp
            print stringlist
            stringlist = tempstringlist
            #print (''.join(map(lambda x: str(x), stringlist)))

if __name__ == '__main__':
    fullpermutation('abc')