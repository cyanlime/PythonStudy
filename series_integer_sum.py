def series_odds_sum(num):
    max = num*num*num
    for item in range(1, max, 2):
        sums = []
        sum = 0
        for item2 in range(item, item+num*2-1, 2):
            sum+=item2
        if sum==max:
            for item3 in range(item2, item2+1-num*2, -2):
                sums.append(item3)
            return sums, num
    if num==1:
        return [1], 1

if __name__ == "__main__":
    sums, num = series_odds_sum(100)
    print '%s^3=%s' % (num, '+'.join(map(lambda x: str(x), sums)))