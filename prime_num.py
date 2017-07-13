def prime_number(min, max):
    primenums = []
    leap=1

    for num in range(min, max+1):
        for item in range(2, num/2):
            if num%item==0:
                leap=0
                break
        if leap==1:
            primenums.append(num)
        leap=1
    return min, max, primenums

if __name__ == "__main__":
    min, max, primenums = prime_number(100, 200)
    print 'prime number between %s and %s are %s' % (min, max, primenums)