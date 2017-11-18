def common_char(str1, str2):
    array1 = []
    array2 = []
    for item in range(len(str1)):
        array1.append(str1[item])
    for item in range(len(str2)):
        array2.append(str2[item])

    re_array1 = array1[::-1]
    re_array2 = array2[::-1]

    reitem1=0
    reitem2=0
    same_chars = []
    while re_array1[reitem1]==re_array2[reitem2]:
        same_chars.append(re_array1[reitem1])
        reitem1+=1
        reitem2+=1
    
    item1=len(array1)-reitem1+1
    item2=len(array2)-reitem2+1

    return str1, str2, item1, item2, same_chars

if __name__ == "__main__":
    array1, array2, item1, item2, same_chars = common_char('loading', 'being')
    print "from the %s char of %s and %s char of %s, chars are %s" % (item1, array1, item2, array2, same_chars[::-1])