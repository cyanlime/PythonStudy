# 00B
# 0A1
# 000

# 100000B
# 0101010
# 0001000
# 0A10011
# 0000000

def fishing(array,x,y,t):
    sum = 0
    for item in range(len(array)):
        for item2 in range(len(array[item])):
            if item==x-1 and item2==y-1:
                pro = array[item][item2]
            sum+=array[item][item2]
    random_pro = sum/((item+1)*(item2+1))

    if pro>random_pro:
        return "cc", pro
    elif random_pro>pro:
        return "ss", random_pro
    else:
        return "equal", pro

def cut_grid(array):
    X_axis = []
    Y_axis = []
    for item in array:
        X_axis.append(item[0])
        Y_axis.append(item[1])

    min_X = X_axis[0]
    for x in X_axis:
        if x<min_X:
            min_X = x
    max_X = X_axis[0]
    for x in X_axis:
        if x>min_X:
            max_X = x  
    min_Y = Y_axis[0]
    for y in Y_axis:
        if y<min_Y:
            min_Y = y
    max_Y = Y_axis[0]
    for y in Y_axis:
        if y>min_Y:
            max_Y = y

    if max_X-min_X>max_Y-min_Y:
        area = (max_X-min_X)*(max_X-min_X)
    else:
        area = (max_Y-min_Y)*(max_Y-min_Y)
    return area

def transfer_crimer(values,t,c):
    methods = {}
    item=0

    while item<len(values)-c+1:
        sum=0
        originitem = item
        for item in range(originitem, originitem+c):
            sum+=values[item]
        if sum<t:
            methods[(values[item-c+1],values[item])]=sum
        item=originitem+1
    return methods

def average_age(Y,x,N):
    for item in range(1, N+1):
        average = Y+item+x*(21-(Y+item))
        Y=average
    return average

0011
1010
0110
0010

if __name__ == "__main__":
    print fishing([[0.2,0.1],[0.1,0.4]],1,1,1)
    print cut_grid([[0,0],[0,3]])
    print transfer_crimer([1,2,3,4,5,6,36,5,4,321,2,3,2,5,2],100,5)
    print average_age(5,0.2,3)