def position(string):
    array = []
    for item in range(len(string)):
        array.append((string[item],item))
    
    dic = {}
    array2 = []
    for item in array:
        key, value = item
        if key not in dic:
            array2 = []
            array2.append(value)
            dic[key] = array2
        else:
            dic[key].append(value)
    return dic

def position2(string):
    d = {}
    for index, char in enumerate(string):
        ofs = d.get(char)
        if ofs is None:
            ofs = []
            d[char] = ofs
        ofs.append(index)
    l = d.items()
    #l.sort()
    for tup in l:
        print ','.join(map(lambda i: '%s:%s' % (tup[0], i), tup[1]))


if __name__ == "__main__":
    position2('kygexrrwunuwxalgcbxistydvrxmfyhbzgfpjwtrsaszqkxqjrgchhybxuzlmccafsljlfdse')
    dic = position('kygexrrwunuwxalgcbxistydvrxmfyhbzgfpjwtrsaszqkxqjrgchhybxuzlmccafsljlfdse')
    for key, values in dic.items():
        print ''.join(map(lambda x: key+':'+str(x)+',', values))
