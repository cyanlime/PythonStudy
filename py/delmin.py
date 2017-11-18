def delmin(array):
    if len(array)==0:
        return "array is null"
    min = array[0]
    
    for item in range(len(array)):
        if array[item]<min:
            min = array[item]
            min_item = item
    
    if min_item==len(array)-1:
        array[min_item]=array[len(array)-2]
    else:
        array[min_item]=array[len(array)-1]
    return min, array

if __name__ == "__main__":
    min, array = delmin([2,3,43,4,2,4,5,6,7,17,3,5,67,9,1])
    print "delete %s new array is %s" % (min, array)