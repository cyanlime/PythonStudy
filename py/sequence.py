def compare(x,y,z):
    if x>y:
        if x>z:
            if y>z:
                print z,y,x
            else:
                print y,z,x
    else:
        if y>z:
            if z>x:
                print x,z,y
        else:
            print x,y,z

def multiplication(row):
    for line in range(1,row+1):
        print
        for rank in range(1,line+1):
            print '%s*%s=%s' % (line,rank,line*rank)


import sys
def weight(weight, increment, deadline):
    for year in range(1,deadline+1):
        moon_weight = (weight+year*increment)*0.165
        print '%s years later, weight is %s' % (year,moon_weight)
        
if __name__ == "__main__":
    #compare(88,7,6)
    #multiplication(4)
    #weight(46, 1)
    print 'Please input your weight on earth:'
    para1 = int(sys.stdin.readline())
    print 'Please input the increment one year:'
    para2 = float(sys.stdin.readline())
    print 'Please input the number of years you count:'
    para3 = int(sys.stdin.readline())

    weight(para1, para2, para3)