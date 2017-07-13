def order_words(str1,str2):
    origin_words = []
    origin_word = []
    for item in range(len(str1)):
        if str1[item]!=' ' and item!=len(str1)-1:
            origin_word.append(str1[item])
            continue
        if str1[item]==' ':
            originword = ''.join(map(lambda x: str(x), origin_word))
            origin_words.append(originword)
            origin_word = []
            continue
        if item==len(str1)-1:
            origin_word.append(str1[item])
            originword = ''.join(map(lambda x: str(x), origin_word))
            origin_words.append(originword)
            origin_word = []

    order_word = []
    order_words = []
    for item2 in range(len(str2)):
        if str2[item2]!=' ':
            order_word.append(str2[item2])
        if str2[item2]==' ':
            orderword = ''.join(map(lambda x: str(x), order_word))
            order_words.append(orderword)
            order_word = []
            continue
        if item2==len(str2)-1:
            orderword = ''.join(map(lambda x: str(x), order_word))
            order_words.append(orderword)
            order_word = []
           
    for word in origin_words:
        if word not in order_words:
            return False
    return True

def space_replace(string):
    strings = []
    for item in range(len(string)):
        if string[item]!=' ':
            strings.append(string[item])
        else:
            strings.append('%20')
    replace_string = ''.join(map(lambda x: str(x), strings))
    return replace_string

def string_compress(string):
    comstrings = []
    item = 0
    num = 1
    while item<len(string):
        num = 1
        origin_item = item
        item+=1
        if origin_item==len(string)-1:
            comstrings.append(string[origin_item])
            comstrings.append('1')
            break
        while string[item]==string[origin_item] and item<len(string)-1:
            num+=1
            item+=1
        comstrings.append(string[item-1])
        if string[item]==string[origin_item] and item==len(string)-1:
            comstrings.append(str(num+1))
            break
        else:
            comstrings.append(str(num))

    if len(comstrings)>=len(string):
        return string
    else:
        comstring = ''.join(map(lambda x: str(x), comstrings))
        return comstring

# 1 2 3
# 0 1 2
# 0 0 1
def clean_matrix(array):
    rows = []
    ranks = []
    for item in range(len(array)):
        for item2 in range(len(array[item])):
            if array[item][item2]==0:
                rows.append(item)
                ranks.append(item2)
    
    for item in range(len(array)):
        for item2 in range(len(array[item])):
            if (item in rows) or (item2 in ranks):
                array[item][item2]=0
    return array

def sum_of_array(array1, array2):
    sum = []
    carry = 0
    item = 0
    if len(array1)>len(array2):
        for num1 in range(len(array1)-len(array2)):
            array2.append(0)
    else:
        for num2 in range(len(array2)-len(array1)):
            array1.append(0)

    while item<len(array1):
        if array1[item]+array2[item]>9 or (array1[item]+array2[item]==9 and carry==1):
            if carry==1:
                sum.append(array1[item]+array2[item]-10+1)
            else:
                sum.append(array1[item]+array2[item]-10)
            carry=1
        else:
            if carry==1:
                sum.append(array1[item]+array2[item]+1)
            else:
                sum.append(array1[item]+array2[item])
            carry=0
        item+=1

    if carry==1:
        sum.append(1)
    return sum

if __name__ == "__main__":
    print order_words("This is nowcoder","is This nowcoder")
    print space_replace("Mr John Smith")
    print space_replace("Hello  World")
    print string_compress('aabcccccaaa')
    #print string_compress('welcometonowcoderrrrrrrrrrrrrrrrrrrrr')
    print clean_matrix([[1,2,3],[0,1,2],[0,0,1]])
    print sum_of_array([3,4,6,9,9],[7,4,4])