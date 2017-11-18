def prime_factor(num):
    number = num
    factors = []

    for item in range(2, num/2):
        while num%item==0 and num!=1:
            num/=item
            factors.append(item)
    return number, factors

if __name__ == "__main__":
    number, factors = prime_factor(100)
    print '%s=%s' % (number, '*'.join(map(lambda x: str(x), factors)))