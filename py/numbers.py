def bigger():
    sum = 0
    item = 1
    while sum<1000:
        sum+=item
        item+=1
    return item, sum

if __name__ == "__main__":
    num, sum = bigger()
    print '1+2+...+%s=%s' % (num, sum)

