# 1,1,2,3,4,5,13,21
import time

def breed():
    pass

x = [1, 2, 3]
y = x[:]
print y


dic = {1: 'a', 2: 'b'}
for key, value in dic.items():
    print key, value
    time.sleep(1)

def fibseq(max):
    fibs = []

    a1=1
    b2=1
    fibs.append(a1)
    fibs.append(b2)
    n=len(fibs)
    while n<max:
        a1+=b2
        fibs.append(a1)
        b2+=a1
        fibs.append(b2)
        n+=2
    return fibs
    

def product(num):
    products = []
    pros = []
    for number in range(1, num+1):
        for item in range(1, number+1):
            pro = number*item
            products.append((pro,number,item))
        for product in products:
            str0 = str(product[0])
            str1 = str(product[1])
            str2 = str(product[2])
            pros.append(str1+'*'+str2+'='+str0)
        print '%s' % ' '.join(map(lambda x: str(x), pros))
            
        products = []
        pros = []

def printf(style, num):
    styles = []
    for number in range(1, num+1):
        styles.append(style)
        print ''.join(map(lambda x: str(x), styles))

def fib(n):
    if n==1:
        return [1]
    if n==2:
        return [1, 1]
    fibs = [1, 1]
    for i in range(2,n):
        fibs.append(fibs[-1]+fibs[-2])
    return fibs

if __name__ == "__main__":
    product(9)
    printf('*', 9)
    print fibseq(10)
    print fib(10)


