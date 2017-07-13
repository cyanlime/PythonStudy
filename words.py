def words(string):
    num = 0
    word = []
    dic = {}
    for item in string:
        if item!=' ' and item!='.':
            word.append(item)
        else:
            aword = ''.join(map(lambda x: str(x), word))
            dic[aword] = len(aword)
            num+=1
            word = []
    return num, dic

if __name__ == "__main__":
    num, dic = words('hello how are you.')
    print "there are %s words" % num
    for key, value in dic.items():
        print "word %s length: %s" % (key, value)