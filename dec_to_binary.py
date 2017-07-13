def dec_to_binary(num):
    n = 0
    chars = []
    if num%2!=0:
        integer = num-1
    else:
        integer = num

    origin = integer
    if integer>1:
        while integer>1:
            integer/=2
            n+=1
        chars.append('1')
        originn = n

        pro = 1
        for item in range(n):
            pro*=2

        n2=0
        rest = origin-pro
        origin_rest = rest
        if rest>1:
            while len(chars)<originn:
                while rest>1:
                    rest/=2
                    n2+=1
                pro2 = 1
                for item in range(n2):
                    pro2*=2   
                while n-n2>1:
                    chars.append('0')
                    n-=1
                if len(chars)<originn:
                    chars.append('1')
                    rest = origin_rest-pro2
                    origin_rest = rest
                    n=n2
                    n2=0

        if rest==0:
            if num%2!=0:
                for item in range(n-1):
                    chars.append('0')
                chars.append('1')
            else:
                for item in range(n):
                    chars.append('0')
    if integer==0:
        chars.append('1')
    return chars
        
if __name__ == "__main__":
    print dec_to_binary(8888)