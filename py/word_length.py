def last_word_length(string):
    words = []
    for item in range(len(string)-1, -1, -1):
        words.append(string[item])
        if string[item]==' ':
            word_length = len(words)-1
            return word_length, string

def char_num(string, char):
    num = 0
    for item in string:
        if item==char or item.lower()==char or item.upper()==char:
            num+=1
    return char, num, string

import random
def de_dup_sort(n):
    numbers = []
    while len(numbers)<n:
        number = random.randint(1,1000)
        numbers.append(number)

    fre_num = {}
    for num in numbers:
        if num not in fre_num:
            fre_num[num]=1
        else:
            fre_num[num]+=1

    values = fre_num.keys()
    return sorted(values)
        
def depart_string(string1, string2):
    strings = []
    strings.append(string1)
    strings.append(string2)

    for string in strings:
        array = []
        for item in string:
            if item!= ' ':
                array.append(item)
        num = len(array)/8
        rest = len(array)%8

        item = 0
        array1 = []
        while item<num:
            for arrayitem in range(item*8, item*8+8):
                array1.append(array[arrayitem])
            print ''.join(map(lambda x: str(x), array1))
            item+=1
            array1=[]

        if rest!=0:
            rest_array = []
            for item in range(num*8, len(array)):
                rest_array.append(array[item])
            for item in range(len(array), (num+1)*8):
                rest_array.append('0')
            print ''.join(map(lambda x: str(x), rest_array))


if __name__ == "__main__":
    last_word_len, string = last_word_length('hello world, python')
    print "the length of last word of string %s: %s" % (string, last_word_len)

    char, num, string = char_num('aaABCSe 1Eef', 'e')
    print "char %s appears %s times in %s" % (char, num, string)

    print de_dup_sort(200)

    depart_string('abc   e   fghikilmnopdhh', 'ABc d e d d dh')