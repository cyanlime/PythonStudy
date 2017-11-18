def sort_std_info(array):
    for item in range(len(array)):
        for item2 in range(item+1, len(array)):
            if array[item][2]<array[item2][2]:
                temp = array[item2]
                array[item2] = array[item]
                array[item] = temp

    for item in range(len(array)-1):
        if array[item][2]==array[item+1][2]:
            if array[item][0]>array[item+1][0]:
                temp = array[item+1]
                array[item+1] = array[item]
                array[item] = temp

    for item in range(len(array)-1):
        if (array[item][2]==array[item+1][2]) and  (array[item][0]==array[item+1][0]):
            if array[item][1]>array[item+1][1]:
                temp = array[item+1]
                array[item+1] = array[item]
                array[item] = temp
    return array

def find_list_max(array):
    item_column = 0
    columns_array = []
    while len(columns_array)<len(array[0]):
        column = []    
        for item in array:
            column.append(item[item_column])
        columns_array.append(column)
        item_column+=1
    
    for item in columns_array:
        max = item[0]
        max_item = 0
        for item2 in range(1,len(item)):
            if item[item2]>max:
                max = item[item2]
                max_item = item2
        temp = item[0]
        item[0] = item[max_item]
        item[max_item] = temp
    
    for item in columns_array:
        sec_max = item[1]
        sec_max_item = 1
        for item3 in range(2,len(item)):
            if item[item3]>sec_max:
                sec_max = item[item3]
                sec_max_item = item3
        temp = item[1]
        item[1] = item[sec_max_item]
        item[sec_max_item] = temp

    max_colums_array = []
    for item in columns_array:
        max_colums_array.append(item[:2])

    max_array = []
    max_item = 0
    while len(max_array)<len(max_colums_array[0]):
        max_line_array = []
        for item in max_colums_array:
            max_line_array.append(item[max_item])
        max_array.append(max_line_array)
        max_item+=1
    return max_array   

def find_list_max2(array):
    item_column = 0
    columns_array = []
    while len(columns_array)<len(array[0]):
        column = []    
        for item in array:
            column.append(item[item_column])
        columns_array.append(column)
        item_column+=1
    
    max_array1 = []
    for item in columns_array:
        max = item[0]
        max_item = 0
        for item2 in range(1,len(item)):
            if item[item2]>max:
                max = item[item2]
                max_item = item2
        max_array1.append(max)
        temp = item[0]
        item[0] = item[max_item]
        item[max_item] = temp

    max_array2 = []
    for item in columns_array:
        sec_max = item[1]
        sec_max_item = 1
        for item3 in range(2,len(item)):
            if item[item3]>sec_max:
                sec_max = item[item3]
                sec_max_item = item3
        max_array2.append(sec_max)
    
    max_array = []
    return max_array1, max_array2

if __name__ == "__main__":
    array = sort_std_info([('abc',20,99),('ccd',19,98),('bed',20,97),('ced',20,98),('bed',19,97)])
    for item in array:
        print '%s %s %s' % (item[0],item[1],item[2])

    max_array = find_list_max([[1,2,4,9,8],[-1,4,9,8,8],[12,9,8,7,0],[7,8,9,7,0]])
    for item in max_array:
        print ' '.join(map(lambda x: str(x), item))

    max_array1, max_array2 = find_list_max2([[1,2,4,9,8],[-1,4,9,8,8],[12,9,8,7,0],[7,8,9,7,0]])
    print ' '.join(map(lambda x: str(x), max_array1))
    print ' '.join(map(lambda x: str(x), max_array2))