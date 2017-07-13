def reverse(array):
    for item in range(0, len(array)/2):
        temp = array[len(array)-1-item]
        array[len(array)-1-item] = array[item]
        array[item] = temp
    return array

def del_x(array, x):
    k = 0
    for item in range(len(array)):
        if array[item]==x:
            k+=1
        else:
            array[item-k] = array[item]
    del_xarray=array[:len(array)-k]
    return del_xarray

def del_x_2(array, x):
    k = 0
    for item in range(len(array)):
        if array[item]!=x:
            array[k] = array[item]
            k+=1
    del_xarray = array[:k]
    return del_xarray

def del_s_t(array, s, t):
    if s>=t or len(array)==0:
        return "Array is null or s not larger than t." 
    k = 0
    for item in range(len(array)):
        if array[item]>t or array[item]<s:
            array[k] = array[item]
            k+=1
    del_s_t_array = array[:k]
    return del_s_t_array

def del_sort_dup(array):
    dic = {}
    for item in array:
        if item not in dic.keys():
            dic[item]=1
        else:
            dic[item]+=1
    return dic.keys()

def merge_sort(array1, array2):
    if array1[len(array1)-1]<array2[0]:
        array1.extend(array2)
        return array1
    if array2[len(array2)-1]<array1[0]:
        array2.extend(array1)
        return array2

    item1=0
    item2=0
    array = []
    while item1<len(array1) and item2<len(array2):
        if array1[item1]>array2[item2]:
            min = array2[item2]
            item2+=1
        else:
            min = array1[item1]
            item1+=1
        array.append(min)

    if item1<len(array1):
        array.extend(array1[item1:len(array1)])
    if item2<len(array2):
        array.extend(array2[item2:len(array2)])
    return array, array1, array2
    

if __name__ == "__main__":
    #print reverse([1,2,3,4,5,6,7,8,9,10])
    #print reverse([0,1,2,3,4,5,6,7,8,9,10])
    # print del_x([1,2,3,4,5,2,3,2,3,3,3,2,5,3,2,4,5], 3)
    # del_xarray= del_x_2([1,2,3,4,5,2,3,2,3,3,3,2,5,3,2,4,5], 3)
    # print del_xarray

    print del_s_t([1,2,3,11,7,4,5,6,7,8,9,10], 4, 8)
    print del_sort_dup([1,2,3,3,3,4,5,5,6,5,7,8,9,10])
    array, array1, array2 = merge_sort([1,2,3,4,5,5,7,9], [2,4,6,8,10])
    print "%s merge to %s: %s" % (array1, array2, array)

