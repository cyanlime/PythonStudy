def max_value_matrix():
    print "please input the dimension of row and column:"
    dimension = raw_input()

    value = []
    values = []
    for item in range(len(dimension)):
        if dimension[item]!=' ':
            value.append(dimension[item])
        if dimension[item]==' ' or item==len(dimension)-1:
            v = ''.join(map(lambda x: str(x), value))
            values.append(v)

    m = int(values[0])
    n = int(values[0])

    arrays = []
    array = []
    row_value = []
    while len(arrays)<m:
        print "please input the value of row:"
        row_values = raw_input()
        for item in range(len(row_values)):
            if row_values[item]!=' ':
                row_value.append(row_values[item])
            if row_values[item]==' ' or item==len(row_values)-1:
                v = ''.join(map(lambda x: str(x), row_value))
                array.append(int(v))
                row_value = []
        arrays.append(array)
        array = []
    
    for array in arrays:
        max = array[0]
        maxitem = 0
        sum = 0
        for item in range(len(array)):
            sum+=array[item]
            if array[item]>max:
                max = array[item]
                maxitem = item
        array[maxitem] = sum
    
    for array in arrays:
        print ' '.join(map(lambda x: str(x), array))
        
if __name__ == "__main__":
    print max_value_matrix()