def printf(pattern, num):
    patterns = []
    for item in range(1, num+1):
        patterns.append(pattern)
    print '%s' % (''.join((map(lambda x: str(x), patterns))))
    while len(patterns)>0:
        patterns.pop()
        print '%s' % (''.join((map(lambda x: str(x), patterns))))

if __name__ == "__main__":
    printf("*", 9)
