def dec_to_hex(num):
    hex = []
    hex.append('0')
    hex.append('X')

    a = 0
    origin = num
    while num>=16:
        num/=16
        a+=1

    pro = 1
    for item in range(a):
        pro*=16
    hex.append(num)

    rest = origin-pro*num
    origin_rest = rest
    while rest>=16:
        b = 0
        n = 0
        while rest>=16:
            rest = rest/16
            b+=1
        while a+1-len(hex)+2-b>1:
            hex.append('0')
            b+=1
            n+=1
        hex.append(rest)
        while n>-1:
            pro = pro/16
            n-=1
        rest = origin_rest-pro*rest
        origin_rest = rest
    hex.append(rest)
    new_hex = []
    for item in hex:
        if item==10:
            new_hex.append('A')
        elif item==11:
            new_hex.append('B')
        elif item==12:
            new_hex.append('C')
        elif item==13:
            new_hex.append('D')
        elif item==14:
            new_hex.append('E')
        elif item==15:
            new_hex.append('F')
        else:
            new_hex.append(str(item))
        
    hex = ''.join(map(lambda x: str(x), new_hex))
    return origin, hex

if __name__ == "__main__":
    num, hex = dec_to_hex(4444444444)
    print 'dec %s transfer to hex %s' % (num, hex)