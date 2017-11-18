def continue_subseq(arrayA, arrayB):
    itemb = 0
    for item in range(len(arrayA)):
        if arrayA[item]==arrayB[itemb]:
            while itemb<len(arrayB)-1:
                if arrayA[item]==arrayB[itemb]:
                    item+=1
                    itemb+=1
            if itemb==len(arrayB)-1 and item<=len(arrayA) and arrayA[item]==arrayB[itemb]:
                return True, arrayA, arrayB
            else:
                return False, arrayA, arrayB
    return false, arrayA, arrayB

def del_min(array):
    dic = {}
    for item in array:
        if item not in dic.keys():
            dic[item]=1
        else:
            dic[item]+=1
    print dic

    min = array[0]
    min_item = 0
    while len(array)>1:
        for item in range(len(array)):
            if array[item]<min:
                min = array[item]
                min_item = item
        print min
        array.pop(min_item)
        min = array[0]
        min_item = 0
    print array.pop()

if __name__ == "__main__":
    boolean, arrayA, arrayB = continue_subseq([1,2,3,4,5,6,7,8], [2,3,4,5,6])
    print "%s is a continuous subsequence of %s: %s" % (arrayB, arrayA, boolean)

    del_min([1,2,3,4,6,7,8,4,5,3,2,4,2,1,9,0,75,3,54,4])