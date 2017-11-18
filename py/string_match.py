def string_match(str1, str2):
    item1 = 0
    item2 = 0
    origin_item1 = -1
    while item1<len(str1) and item2!=len(str2):
        if str1[item1]==str2[item2]:
            item1+=1
            item2+=1
        else:
            item1+=1
            item2 = 0
    
    if item2==len(str2):
        return item1-len(str2)
    else:
        return -1

import copy
def min_k_nums(arrays,k):
    origin_arrays = copy.deepcopy(arrays)
    min_nums = []
    while len(min_nums)<k:
        min = arrays[0]
        min_item = 0
        for item in range(len(arrays)):
            if arrays[item]<min:
                min_item = item
                min = arrays[item]
        min_nums.append(arrays.pop(min_item))
        min_item = 0

    nums = []
    for num in origin_arrays:
        if num in min_nums:
            nums.append(num)
    return nums

def add_string(string):
    adds = []
    for item in range(len(string)-2, -1, -1):
        adds.append(string[item])
    strings = ''.join(map(lambda x: str(x), adds))
    return strings

""" continue """
def longest_palindrome(string):
    palindrome_strings = []
    origin_item1 = 0
    origin_item2 = len(string)-1
    item1 = 0
    item2 = len(string)-1
    n = 0
    while (item1!=item2 and item1<len(string)-1):
        while string[item1]==string[item2] and item1!=len(string)-1:
            n+=1
            item1+=1
            item2-=1
            if item1==item2:
                palindrome_strings.append(string[item1-n:item1+n+1])
                break

        if item1==item2:
            origin_item2 = item1-n-1
            item2 = origin_item2
            origin_item1+=1
            item1 =  origin_item1
            continue

        if string[item1]!=string[item2]:
            item1+=1
            item2=origin_item2
            n = 0
            continue
        
        if item1==origin_item2:
            origin_item1+=1
            origin_item2-=1
            item1 = origin_item1
            item2 = origin_item2
            n = 0
            continue
    return palindrome_strings

if __name__ == "__main__":
    print string_match('abdfggfdfghtbvgttrertgbnbvgtthfgfgvhbjnkmbvgttthfg', 'bvgttthfg')
    print min_k_nums([1,2,3,7,8,9,5,0,56,4,32,45,6,545,653], 7)
    print add_string('abhgefghghfe')
    print longest_palindrome('ad1234543211234321adff')