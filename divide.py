def divide(num):
    B = num/100
    S = (num-B*100)/10
    G = num-B*100-S*10
    print '%s+%s+%s=%s' % (B, S, G, B+S+G)

def sum_product(nums):
    if type(nums)==list:
        product = 1
        sum = 0
        products = []
        sums = []
        for item in nums:
            if type(item)==int:
                if item%2==0:
                    product*=item
                    products.append(item)
                    products.append("*")
                else:
                    sum+=item
                    sums.append(item)
                    sums.append("+")
            else:
                print 'factors in list should be integer'
        products.pop()
        sums.pop()
        print '%s=%s' % (''.join(map(lambda x: str(x), products)), product)
        print '%s=%s' % (''.join(map(lambda x: str(x), sums)), sum)
        return sum, product
    else:
        print 'parameter should be a list'

if __name__ == "__main__":
    divide(785)
    sum_product([1,2,3,4,5,6,7,8,8,9,9,7])