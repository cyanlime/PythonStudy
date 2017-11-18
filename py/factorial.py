def factorial(num):
    sum = 0
    product = 1
    nums = []
    products = []
    
    max = num+1
    while max>1:
        for item in range(1, max):
            product*=item
        products.append(product)
        nums.append('%s!' % (max-1))
        nums.append('+')
        max-=1
    
    for item in products:
        sum+=item
    nums.pop()
    print '%s=%s' % (''.join(map(lambda x: str(x), nums)),sum)
    
if __name__ == '__main__':
    factorial(8)