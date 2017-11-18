"""unfinish"""

import math
def prime_partner(array):
    array.sort()
    max_primes_sum = array[-1]+array[-2]

    primenums = []
    for num in range(5, max_primes_sum+1):
        leap = 0
        for item in range(2, int(math.sqrt(num))+1):
            if num%item==0:
                leap = 1
                break
        if leap==0:
            primenums.append(num)

    prime_partners = []
    for item in range(len(array)):
        for item2 in range(item+1, len(array)):
            sum = array[item]+array[item2]
            if sum in primenums:
                prime_partners.append((array[item], array[item2]))
                 
    #return prime_partner
    primes = {}
    for prime_partner in prime_partners:
        prime1, prime2 = prime_partner
        if prime1 not in primes:
            primes[prime1]=1
        else:
            primes[prime1]+=1
        if prime2 not in primes:
            primes[prime2]=1
        else:
            primes[prime2]+=1
    #return primes

    nums = []
    for key, value in primes.items():
        if value==1:
            nums.append(key)

    primeparts = []
    for prime_partner in prime_partners:
        if (prime_partner[0] in nums) or (prime_partner[1] in nums):
            primeparts.append(prime_partner)
    
    #return primeparts
    prime_parts_nums = []
    for primepart in primeparts:
        prime_parts_nums.append(primepart[0])
        prime_parts_nums.append(primepart[1])
    new_prime_partners = []
    for prime_partner in prime_partners:
        if (prime_partner[0] not in prime_parts_nums) and (prime_partner[1] not in prime_parts_nums):
            new_prime_partners.append(prime_partner)
    return new_prime_partners


if __name__ == "__main__":
    print prime_partner([2,5,6,13,12,3,45,8,9,7])