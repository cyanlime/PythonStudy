def inverse(array):
    for item in range(len(array)/2):
        temp = array[item]
        array[item] = array[len(array)-1-item]
        array[len(array)-1-item] = temp
    return array

def insert(array, num):
    if array[0]<array[len(array)-1]:
        if num > array[len(array)-1]:
            array.append(num)

        else:
            for item in range(len(array)):
                if num<=array[item]:
                    temp = array[item]
                    array[item] = num
                    for item2 in range(item+1, len(array)):
                        temp2 = array[item2]
                        array[item2] = temp
                        temp = temp2
                    array.append(temp)
                    return array
        
    if array[0] > array[len(array)-1]:
        if num < array[len(array)-1]:
            array.append(num)
        else:
            for item in range(len(array)):
                if num>=array[item]:
                    temp = array[item]
                    array[item] = num
                    for item2 in range(item+1, len(array)):
                        temp2 = array[item2]
                        array[item2] = temp
                        temp = temp2
                    array.append(temp)
                    return array

if __name__ == "__main__":
    print inverse([1,2,3,4,5,6,7])
    print insert([10,7,6,5,3,2,1], 9)
