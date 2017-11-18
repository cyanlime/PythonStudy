def eat_peach(num, day):
    num = num/2-1
    eat_peach(num)

    x2=1
    for day in range(9,0,-1):
        x1 = (x2+1)*2
        x2 = x1
    print x1


def upspring(sn, times):
    hn = sn/2
    for i in range(2, times+1):
        sn+=2*hn
        hn/=2
    return sn

def perfect_number(num):
    numbers = []
    for item in range(2, num):
        sum = 0
        factors = []
        for item2 in range(1, item):
            if item%item2==0:
                factors.append(item2)
        for factor in factors:
            sum+=factor
        if sum==item:
            print '%s factors are %s' % (item, factors)
            numbers.append(item)
    return numbers

if __name__ == "__main__":
    print upspring(100.0, 10)
    print 'the perfect number in 1000 is %s' % (perfect_number(1000))