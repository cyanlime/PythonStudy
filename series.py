def seriesnum(num):
    init = 1
    minnum = init
    sum = 0
    nums = []

    while minnum<num:
        if sum!=num:
            sum+=minnum
            minnum+=1
            if minnum>num:
                print 'the number does not exist'
            else:
                if sum==num:
                    for item in range(init, minnum):
                        nums.append(item)
                        nums.append('+')
                    nums.pop()                
                    print '%s=%s' % (''.join(map(lambda x: str(x), nums)), num)
                    nums = []
                    sum=0
                    init+=1
                    minnum=init
                if sum>num:
                    sum=0
                    init+=1
                    minnum=init
    return init, minnum

if __name__ == '__main__':
    print seriesnum(6)
    print seriesnum(9)
    print seriesnum(2000)
        
