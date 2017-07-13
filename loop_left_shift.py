# [1,2,3,4,5,6,7,8,9,10]
# [5,6,7,8,9,10,1,2,3,4]

def loop_left_shift(array, p):
    loop_array = []
    for item in range(p, len(array)):
        loop_array.append(array[item])
    for item2 in range(0, p):
        loop_array.append(array[item2])
    return loop_array, array, p

def median(arrayA, arrayB):
    if arrayA[len(arrayA)-1]<=arrayB[0]:
        median = arrayA[len(arrayA)-1]
    if arrayB[len(arrayB)-1]<arrayA[0]:
        median = arrayB[len(arrayB)-1]

    array = []
    itemA = 0
    itemB = 0
    while len(array)<len(arrayA):
        if arrayA[itemA]<arrayB[itemB]:
            min = arrayA[itemA]
            itemA+=1
        else:
            min = arrayB[itemB]
            itemB+=1
        array.append(min)
    median = array.pop()
    return median, arrayA, arrayB

def breakup(array):
    odd_array = []
    for item in range(len(array)):
        if item%2==1:
            odd_array.append(array[item])

    k = 0
    for item in range(len(array)):
        if item%2==0:
            array[k] = array[item]
            k+=1
    array = array[:k]
    return array, odd_array
    
if __name__ == "__main__":
    loop_array, array, p = loop_left_shift([1,2,3,4,5,6,7,8,9,10], 5)
    print "%s loop %s left shift: %s" % (array, p, loop_array)

    median, arrayA, arrayB = median([11,13,15,16,17,18],[1,2,12,18,19,20])
    print "the median between %s and %s: %s" % (arrayA, arrayB, median)

    even_array, odd_array = breakup([1,2,3,4,5,6,7,8,9])
    print "evenitem_array:%s, odditem_array:%s" % (even_array, odd_array)