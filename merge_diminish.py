def merge_diminish(array1, array2):
    if array1[len(array1)-1]<=array2[0]:
        array1.extend(array2)
        array1 = array1[::-1]
        return array1

    if array2[len(array2)-1]<array1[0]:
        array2.extend(array1)
        for item in range(len(array2)/2):
            temp = array2[len(array2)-1-item]
            array2[len(array2)-1-item] = array2[item]
            array2[item] = temp
            return array2

    array = []
    item1 = 0
    item2 = 0
    while item1<len(array1) and item2<len(array2):
        if array1[item1]<array2[item2]:
            min = array1[item1]
            item1+=1
        else:
            min = array2[item2]
            item2+=1
        array.append(min)
    
    if item1<len(array1):
        array.extend(array1[item1:len(array1)])
    if item2<len(array2):
        array.extend(array2[item2:len(array2)])
    array = array[::-1]
    return array

def common(array1, array2):
    array = []
    for item in array1:
        if item in array2:
            array.append(item)
    return array, array1, array2

def common_2(array1, array2):
    item = 0
    k = 0
    for item in range(len(array1)):
        if array1[item] in array2:
            array1[k] = array1[item]
            k+=1
    array1 = array1[:k]
    return array1

if __name__ == "__main__":
    print merge_diminish([1,2,4,6,7,11], [6,7,8,9,10,12])
    array, array1, array2 = common([1,2,4,6,7,8,11], [6,7,8,9,10,11,12])
    print "common items between %s and %s is: %s" % (array1, array2, array)

    print common_2([1,2,4,6,7,9,5,8,11,13], [6,7,8,9,10,11,12])
