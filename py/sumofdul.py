def sumofnum(num, times):
    sum = 0
    numlist = []
    numbers = []
    for time in range(1, times+1):
        numlist.append(str(num))

    while len(numlist)>0:
        strnum = ''.join(map(lambda x: x, numlist))
        num = int(strnum)
        numbers.append(num)
        numlist.pop()
    
    for number in numbers:
        sum+=number
    return numbers, sum

if __name__ == "__main__":
    numbers, sum = sumofnum(5, 5)
    print '%s=%s' % ('+'.join(map(lambda x: str(x), numbers)), sum)
