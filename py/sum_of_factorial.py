def sum_of_factorial(max_num):
    odds = []
    evens = []
    for num in range(1, max_num+1):
        if num%2==0:
            evens.append(num)
        else:
            odds.append(num)

    evens_sum = 0
    evens_pro = 1
    for even in evens:
        for item in range(1, even+1):
            evens_pro*=item
        evens_sum+=evens_pro
        evens_pro = 1

    odds_sum = 0
    odds_pro = 1
    for odd in odds:
        for item in range(1, odd+1):
            odds_pro*=item
        odds_sum+=odds_pro
        odds_pro = 1
    
    return odds_sum, odds, evens_sum, evens, max_num

if __name__ == "__main__":
    odds_sum, odds, evens_sum, evens, max_num = sum_of_factorial(11)
    print "%s=%s, %s=%s" % ('+'.join(map(lambda x: str(x)+'!', odds)), odds_sum, '+'.join(map(lambda x: str(x)+'!', evens)), evens_sum)