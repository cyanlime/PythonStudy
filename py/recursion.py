def age(n):
    if n == 1:
        c = 10
    else:
        c = age(n-1) + 2
    return c

def factorial(n):
    if n == 0:
        result = 1
    else:
        result = n*factorial(n-1)
    return result

def sum_of_factorial(n):
    sum = 0
    product = 1
    for item in range(1,n+1):
        product*=item
        sum+=product
    return sum

def sum_of_fraction(max):
    numerator = 2.0
    denominator = 1.0
    sum = numerator/denominator

    for item in range(1, max):
        numerator, denominator = numerator+denominator, numerator
        sum+=numerator/denominator
    return sum

# print factorial(4)
# print sum_of_factorial(20)
# print sum_of_fraction(20)


def print_diamond(style, n):
#         0         3 
#         1       2,3,4
#         2     1,2,3,4,5
#         3,  0,1,2,3,4,5,6
#         4     1,2,3,4,5
#         5       2,3,4
#         6         3 
#         [[],[],[],[],[]]    """

    diamond = []
    for line in range(0, n/2+1):
        array = []
        for row in range(0, n/2-line):
            array.append(' ')
        for row in range(n/2-line, n/2+line+1):
            array.append(style)
        for row in range(n/2+line, n):
            array.append(' ')
        diamond.append(array)

    for line in range(n/2+1, n):
        array = []
        for row in range(0, line-n/2):
            array.append(' ')
        for row in range(line-n/2, n/2+n-line):
            array.append(style)
        for row in range(n/2+n-line, n):
            array.append(' ')
        diamond.append(array)
    #return diamond
    for item in diamond:
        dia = ''.join(map(lambda x: str(x), item))
        print dia

print_diamond('*', 25)