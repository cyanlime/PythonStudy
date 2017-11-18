def sum_polynomial(array1, array2):
    dic = {}
    for item in range(len(array1)-1, 1, -2):
        dic[array1[item]] = array1[item-1]

    for item in range(len(array2)-1, 1, -2):
        if array2[item] not in dic:
            dic[array2[item]] = array2[item-1]
        else:
            dic[array2[item]]+=array2[item-1]
     
    sorted_dic = sorted(dic.items(), key=lambda item: item[0], reverse=True)
    array = []
    for key, value in sorted_dic:
        if value!=0:
            array.append(value)
            array.append(key)
    return array

if __name__ == "__main__":
    array = sum_polynomial([3,3,5,-2,1,4,0],[4,2,3,-1,2,1,1,-4,0])
    print ' '.join(map(lambda x: str(x), array))        