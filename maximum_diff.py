def maximum_diff(array):
    for item in range(len(array)):
        for item2 in range(item+1, len(array)):
            if array[item2]<array[item]:
                temp = array[item2]
                array[item2] = array[item]
                array[item] = temp
    
    diffs = []
    item = 0
    item2 = 1
    while item2<len(array):
        diff = array[item2]-array[item]
        diffs.append(diff)
        item+=1
        item2+=1
    
    max = diffs[0]
    for num in diffs:
        if num>max:
            max=num
    return max

"""
 1, 2, 3, 4, 5, 6, 7, 8
 9,10,11,12,13,14,15,16
17,18,19,20,21,22,23,24
25,26,27,28,29,30,31,32
33,34,35,36,37,38,39,40
41,42,43,44,45,46,47,48
49,50,51,52,53,54,55,56
57,58,59,60,61,62,63,64
"""

def clockwise_print(arrays):
    clockwise_arrays = []
    num = 0
    while num<len(arrays)/2:
        for item in range(num, len(arrays[num])-num):
            clockwise_arrays.append(arrays[num][item])
        for item in range(num+1, len(arrays)-num):
            clockwise_arrays.append(arrays[item][len(arrays[item])-num-1])
        temp = arrays[len(arrays)-num-1][num]
        arrays[len(arrays)-num-1] = arrays[len(arrays)-num-1][::-1]
        for item in range(num+1, len(arrays[len(arrays)-num-1])-num-1):
            clockwise_arrays.append(arrays[len(arrays)-num-1][item])
        clockwise_arrays.append(temp)
        for item in range(len(arrays)-num-2, num, -1):
            clockwise_arrays.append(arrays[item][num])
        num+=1
    return clockwise_arrays

def zigzag_print(arrays):
    zigzag_arrays = []
    for item in range(len(arrays)):
        if item%2==0:
            for item2 in arrays[item]:
                zigzag_arrays.append(item2)
        else:
            arrays[item] = arrays[item][::-1]
            for item2 in arrays[item]:
                zigzag_arrays.append(item2)
    return zigzag_arrays

"""
1,2,3
4,5,6
7,8,9
"""
def clockwise_rotate(arrays):
    clockwise_rotate_arrays = []
    rotate_arrays = []
    for item2 in range(len(arrays[0])):
        for item in range(len(arrays)-1, -1, -1):
            rotate_arrays.append(arrays[item][item2])
        clockwise_rotate_arrays.append(rotate_arrays)
        rotate_arrays = []
    return clockwise_rotate_arrays

def rotate_string(string, pos):
    rotate_arrays = []
    for item in range(pos+1,len(string)):
        rotate_arrays.append(string[item])
    for item in range(pos+1):
        rotate_arrays.append(string[item])
    rotatestring = ''.join(map(lambda x: str(x), rotate_arrays))
    return rotatestring

def min_no_appear(arrays):
    for num in range(1, len(arrays)+1):
        if num not in arrays:
            return num

def monotony_sum(array, num):
    for item in range(len(array)):
        if array[item]==num:
            break
             
    sum = 0
    for item2 in range(item):
        if array[item2]<num:
            sum+=array[item2]
    return sum

if __name__ == "__main__":
    print maximum_diff([9,3,1,10])
    print clockwise_print([[1,2,3,4,5,6,7,8],[9,10,11,12,13,14,15,16],[17,18,19,20,21,22,23,24],[25,26,27,28,29,30,31,32],[33,34,35,36,37,38,39,40],[41,42,43,44,45,46,47,48],[49,50,51,52,53,54,55,56],[57,58,59,60,61,62,63,64]])
    print zigzag_print([[1,2,3,4,5,6,7,8],[9,10,11,12,13,14,15,16],[17,18,19,20,21,22,23,24],[25,26,27,28,29,30,31,32],[33,34,35,36,37,38,39,40],[41,42,43,44,45,46,47,48],[49,50,51,52,53,54,55,56],[57,58,59,60,61,62,63,64]])
    print clockwise_rotate([[1,2,3,4,5,6,7,8],[9,10,11,12,13,14,15,16],[17,18,19,20,21,22,23,24],[25,26,27,28,29,30,31,32],[33,34,35,36,37,38,39,40],[41,42,43,44,45,46,47,48],[49,50,51,52,53,54,55,56],[57,58,59,60,61,62,63,64]])
    print rotate_string('ABCDEFG', 4)
    print min_no_appear([-1,1,2,3,4,5,7])
    print monotony_sum([1,3,2,5,6,3,4,5,7,8,9],4)