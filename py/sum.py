import sys

def divide(num):
    if type(num)==int and num>1:
        sum = 0
        prints = []
        for item in range(1, num+1):
            sum+=item
            prints.append(item)
            if sum%item==0:
                print '%s = %s' % (' '.join(map(lambda x: str(x), prints)), sum)
            prints.append('+')
        return sum
    else:
        print 'paramater should be a positive integer number'


def sum(num):
    if type(num)==int and num>1:
        sum = 0
        prints = []
        for item in range(1, num+1):
            sum+=item
            prints.append(item)
            print '%s = %s' % (' '.join(map(lambda x: str(x), prints)), sum)
            prints.append('+')
        return sum
    else:
        print 'paramater should be a positive integer number'

if __name__ == "__main__":
    #print "please input a integer number:"
    #num = int(sys.stdin.readline)

    #total = sum(18)
    div = divide(18)
    #print "The sum of one to %s is %s" % (18, total)