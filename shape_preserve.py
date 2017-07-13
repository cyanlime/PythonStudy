def shape_preserve(max):
    shape_nums = []
    dic = {}
    for num in range(2, max+1):
        pro = 1
        for item in range(len(str(num))):
            pro*=10
        square_number = num*num
        number = square_number%pro
        if num==number:
            dic[num] = square_number
            shape_nums.append(dic)
            dic = {}
    return shape_nums
if __name__ == "__main__":
    shape_nums = shape_preserve(100000)
    for shape_num in shape_nums:
        for key, value in shape_num.items():
            print '%s:%s' % (key, value)