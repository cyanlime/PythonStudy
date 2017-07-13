def adjust_matrix(array):
    for num in range(len(array)):
        max = array[num][num]
        max_item = num
        for item in range(num+1, len(array)):
            if array[item][num]>max:
                max = array[item][num]
                max_item = item
        temp = array[num]
        array[num] = array[max_item]
        array[max_item] = temp
    return array

def find_min(array):
    minx = array[0][0]
    miny = array[0][1]
    for item in array:
        if item[0]<minx:
            minx = item[0]
            miny = item[1]
    for item in array:
        if item[0]==minx:
            if item[1]<miny:
                miny=item[1]
    return minx, miny

def pop_complex_num(array):
    imaginary_num = []
    complex_num = {}
    start_image = 0

    for item in array:
        for char in range(len(item)):
            if item[char]=='+':
                start_image = 1
            if item[char]!='+' and item[char]!='i' and start_image==1:
                imaginary_num.append(item[char])
        imaginary_part = ''.join(map(lambda x: str(x), imaginary_num))
        complex_num[item] = int(imaginary_part)
        imaginary_num = []
        start_image = 0

    # for key, value in complex_num.items():
    #     pass

    key = max(complex_num, key=complex_num.get)

    for item in range(len(array)):
        if array[item]==key:
            array.pop(item)
            break
    return array, len(array)

if __name__ == "__main__":
    array = adjust_matrix([[3,6,8,7],[6,7,5,3],[8,6,5,3],[9,8,7,2]])
    for item in array:
        print ' '.join(map(lambda x: str(x), item))

    minx,miny = find_min([(3,3),(2,2),(5,5),(2,1),(3,6)])
    print "%s %s" % (minx, miny)

    array, size = pop_complex_num(['1+2i','3+42i','1+3i','2+5i'])
    print array,size