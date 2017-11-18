def power(num):
    originnum = num
    if num%2==0:
        i = 0
        while num>1:
            num/=2
            i+=1
        factor = 2
        product = 1
        for item in range(1, i):
            product*=factor
            rest = originnum-product
            print "%s+2^%s=%s" % (rest, item, originnum)

            # originrest = rest
            # while rest>1:
            #     rest/=2
            #     rest2 = originrest-rest
                #print "%s+2^%s=%s" % (rest2, item, originnum)

    else:
        i = 0
        while num>1:
            num/=2
            i+=1
        return "2^%s+1=%s" % (i, originnum)


if __name__ == "__main__":
    print power(256)
