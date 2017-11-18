def mix_chars(str1,str2,str3):
    if len(str3)!=len(str1)+len(str2):
        return False
    else:
        str3s = []
        for item in range(len(str3)):
            str3s.append(str3[item])

        origin_item3 = 0
        for item1 in range(len(str1)):
            if str1[item1] in str3:
                for item3 in range(origin_item3, len(str3s)):
                    if str3s[item3]==str1[item1]:
                        origin_item3 = item3
                        str3s.pop(item3)
                        break
        string2 = ''.join(map(lambda x: str(x), str3s))
        if string2==str2:
            return True
        else:
            return False

def min_k_num(array1,array2,k):
    item1 = 0
    item2 = 0
    array = []
    item1_in = 0
    item2_in = 0
    item1_in2 = 0
    while len(array)<k:
        if item1<len(array1)-1 and item2<len(array2)-1:
            if array1[item1]<array2[item2]:
                array.append(array1[item1])
                item1+=1
            else:
                array.append(array2[item2])
                item2+=1
        else:
            if item1==len(array1)-1 and item2!=len(array2)-1:
                if array1[item1]<array2[item2] and item1_in==0:
                    array.append(array1[item1])
                    item1_in = 1
                else:
                    array.append(array2[item2])
                    if item2!=len(array2)-1:
                        item2+=1
                continue
            if item2==len(array2)-1 and item1!=len(array1)-1:
                if array2[item2]<array1[item1] and item2_in==0:
                    array.append(array2[item2])
                    item2_in = 1
                else:
                    array.append(array1[item1])
                    if item1!=len(array1)-1:
                        item1+=1
                continue
            if item2==len(array2)-1 and item1==len(array1)-1 and len(array)==len(array1)+len(array2)-2:
                if array2[item2]<array1[item1]:
                    array.append(array2[item2])
                else:
                    item1_in2 = 1
                    array.append(array1[item1])
                continue
            if item2==len(array2)-1 and item1==len(array1)-1 and len(array)==len(array1)+len(array2)-1:
                if item1_in2==1 or item1_in==1:
                    array.append(array2[item2])
                    continue
                if item2_in==1 or item1_in2==0:
                    array.append(array1[item1])
    return array[k-1]

# e =[66, 2 ,6,2,8, 4, 3]
# a =[ 7,12,65,7,4,40,15]

def odd(max):
    nums = []
    filter_nums = []
    for num in range(1, max, 2):
        nums.append(num)
    
    while len(nums)>1:
        for item in range(len(nums)):
            if item%2==1:
                filter_nums.append(nums[item])
        nums = filter_nums
        filter_nums = []
    return nums

# 5 1 8 5 2
# 1 3 10 3 3
# 7 8 5 5 16
def max_matrix_product(array):
    item1 = 0
    item2 = 0
    products = []

    while item1<len(array):
        while item2<len(array[item1]):
            origin_item1 = item1
            origin_item2 = item2
            product = 1
            for item1 in range(len(array)):
                if item1!=origin_item1:
                    product*=array[item1][item2]
            item1=origin_item1
            for item2 in range(len(array[item1])):
                if item2!=origin_item2:
                    product*=array[item1][item2]
            item2=origin_item2
            products.append(product)
            item2+=1    
        item1+=1
        item2=0
    
    max = products[0]
    for num in products:
        if num>max:
            max=num
    return max

# 1 1 [2]
# 2 1 [1]
# 3 2 [1,2]
def who_cheat():
    print 'please input the total question numbers:'
    numbers = raw_input()
    dic = {}
    while len(dic.keys())<int(numbers):
        print 'please input the questioner ID and the answerers ID like "1 [2]":'
        question, answers = raw_input().split(' ')
        dic[int(question)]=answers

    cheats = []
    for key in dic.keys():
        for value in dic[key]:
            if value.isdigit() and (int(value) in dic.keys()):
                for v in dic[int(value)]:
                    if v.isdigit() and int(v)==key:
                        if (key not in cheats) and (int(value) not in cheats):
                            cheats.append(key)
                            cheats.append(int(value))

    for value in dic.values():
        values = []
        for item in value:
            if item.isdigit():
                values.append(int(item))
        for key in dic.keys():
            n = 0
            for v in dic[key]:
                if v.isdigit() and int(v) in cheats:
                    n+=1
            if n>=2 and key not in cheats:
                cheats.append(key) 
    return cheats

if __name__ == "__main__":
    print mix_chars('ABDDDC','12CDDD','AB12CDDDDDDC')
    print min_k_num([1,2,7,8,9,11],[3,4,5,6,6,6,7,8,9],12)
    print odd(500)
    print max_matrix_product([[5,1,8,5,2],[1,3,10,3,3],[7,8,5,5,16]])
    print who_cheat()