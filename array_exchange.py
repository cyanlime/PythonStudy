def array_exchange(array, m):
    array1 = []
    for item in range(m, len(array)):
        array1.append(array[item])
    for item2 in range(0, m):
        array1.append(array[item2])
    return array1

def find_x(array, x):
    if x==array[len(array)-1]:
        return "max number in array is %s" % x
    if x>array[len(array)-1]:
        array.append(x)
        return "insert %s: %s" % (x, array)

    for item in range(0, len(array)):
        if array[item]==x:
            temp = array[item+1]
            array[item+1] = array[item]
            array[item] = temp
            return "find %s: %s" % (x, array)
        else:
            if array[item]>x:
                array.insert(item, x)
                return "insert %s: %s" % (x, array)


if __name__ == "__main__":
    print array_exchange([1,2,3,4,5,9,7,6,5,4,3,6,7,8,9], 5)
    print find_x([1,2,3,4,5,6,7,8,9], 5)
