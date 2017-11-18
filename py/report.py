import random

def numberoff(nums, max):
    first = nums[0]
    sec = nums[1]
    third = nums[2]
    print first, sec, third
    for num in range(1, max+1):
        loop = 0
        for item in list(str(num)):
            if int(item)==first:
                loop = 1
                print '%s, %s' % (num, 'Fizz')
                break
        if loop==0:
            if num%first==0:
                if num%sec==0:
                    if num%third==0:
                        print '%s, %s' % (num, 'FizzBuzzWhizz')
                        continue
                    print '%s, %s' % (num, 'FizzBuzz')
                    continue
                print '%s, %s' % (num, 'Fizz')
                continue
            elif num%sec==0:
                print '%s, %s' % (num, 'Buzz')
                continue
            elif num%third==0:
                print '%s, %s' % (num, 'Whizz')
                continue
            else:
                print num


if __name__ == '__main__':
    nums = []
    while len(nums)!=3:
        num = random.randint(1, 9)
        if num not in nums:
            nums.append(num)
        continue
    numberoff(sorted(nums), 100)