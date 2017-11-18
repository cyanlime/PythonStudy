def narnum(max):
    narnums = []
    for num in range(100,max):
        strnum = str(num)
        strnumlen = len(strnum)      
        nums = []
        sums = []
        for item in strnum:
            nums.append(item)

        for item2 in range(len(nums)):
            intnum = int(nums[item2])
            product = intnum
            while strnumlen-1>0:
                product*=intnum
                strnumlen-=1
            sums.append(product)
            strnumlen = len(nums)

        sum = 0
        for item in sums:
            sum+=item
   
        if num==sum:
            narnums.append(num)
    return narnums

if __name__ == "__main__":
    narnums=narnum(100000)
    strnums = []
    for num in narnums:
        lengnum = len(str(num))
        for item in range(lengnum):
            strnum = str(num)[item]
            strnums.append(strnum)
        print '%s=%s' % ('+'.join(map(lambda x: str(x)+'^'+str(lengnum), strnums)), num)  
        strnums = []          
