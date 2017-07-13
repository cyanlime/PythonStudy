import math
def primefactor(num):
    array = []
    for number in range(2, num/2+1):
        leap =0
        for item in range(2, int(math.sqrt(number))+1):
            if number%item==0 and number!=item:
                leap=1
        if leap==0:
            array.append(number)

    primefactors = []
    for item in array:
        if num%item==0:
            primefactors.append(item)
    return primefactors

def primefactor2(num):
    factors = []
    for item in range(2, int(math.sqrt(num))+1):
        while num%item==0:
            num/=item
            factors.append(item)
        if num==1:
            break
    return factors

def float_to_int(num):
    strnum = str(num)
    intnum = []
    dot_item = 0
    for item in range(len(strnum)):
        if strnum[item]!='.' and dot_item==0:
            intnum.append(strnum[item])
        if strnum[item]=='.':
            dot_item = item
        if strnum[item]!='.' and item==dot_item+1:
            if int(strnum[item])<5:
                break
            else:
                intnum.pop()
                intnum.append(int(strnum[dot_item-1])+1)
    
    inum = ''.join(map(lambda x: str(x), intnum))
    return inum

def merge_value(array):
    dic = {}
    for item in array:
        for item2 in range(len(item)):
            if item2==0:
                if item[item2] not in dic:
                    dic[item[item2]] = item[item2+1]
                else:
                    dic[item[item2]]+=item[item2+1]
                break
    for key, value in dic.items():
        print "%s %s" % (key, value)

def reverse_dep(num):
    reverse_nums = []
    strnum = str(num)
    for item in range(len(strnum)-1, -1, -1):
        if strnum[item] not in reverse_nums:
            reverse_nums.append(strnum[item])
    newint = ''.join(map(lambda x: str(x), reverse_nums))
    return newint

def numchar(string):
    array = []
    for item in range(len(string)):
        if 0<=ord(string[item])<=127:
            if string[item] not in array:
                array.append(string[item])
    return len(array)

def reverse(num):
    nums = []
    strnum = str(num)
    for item in range(len(strnum)-1, -1, -1):
        nums.append(strnum[item])
    renum = ''.join(map(lambda x: str(x), nums))
    return num, renum

def reverse_sentence(sentence):
    words = []
    chars = []
    for item in range(len(sentence)-1, -1, -1):
        if sentence[item]!=' ':
            chars.append(sentence[item])
        if sentence[item]==' ' or item==0:
            chars = chars[::-1]
            word = ''.join(map(lambda x: str(x), chars))
            words.append(word)
            chars = []
    resentence = ' '.join(map(lambda x: str(x), words))
    return resentence, sentence

if __name__ == "__main__":
    print primefactor2(100)
    print float_to_int(56.9)

    merge_value([[0,1],[0,2],[1,2],[3,4]])
    print reverse_dep(9876673)

    print numchar('abdbdcdd')
    num, renum = reverse(1516000)
    print "integer %s revese to %s" % (num, renum)

    resentence, sentence = reverse_sentence('I am a boy')
    print "sentence '%s' reverse to '%s'" % (sentence, resentence)