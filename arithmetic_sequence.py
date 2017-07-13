def arithmetic_sequence(min, diff, num):
    sum = 0
    for item in range(num):
        sum+=min
        min+=diff
    return sum

def AutomorphicNumbers(max):
    automorphics = {}
    for item in range(5, max):
        product = 1
        for i in range(len(str(item))):
            product*=10
        num = item*item
        if item==num%(int(str(num)[:int((len(str(num))-len(str(item))))])*product):
            automorphics[item]=num
    return automorphics

def addsignal(string):
    array = []
    isdigit = 0
    for item in range(len(string)):
        if string[item].isdigit() and isdigit==0:
            array.append('*')
            array.append(string[item])
            isdigit = 1   
        elif (not string[item].isdigit()) and isdigit==1:
            array.append('*')
            array.append(string[item])
            isdigit = 0
        else:
            array.append(string[item])
    if string[len(string)-1].isdigit():
        array.append('*')

    newstring = ''.join(map(lambda x: str(x), array))
    return string, newstring

def count(candidates, votes):
    voters = {}
    for item in votes:
        if item in candidates:
            if item not in voters:
                voters[item]=1
            else:
                voters[item]+=1
        else:
            if 'Invalid' not in voters:
                voters['Invalid'] = 1
            else:
                voters['Invalid']+=1
    return voters      

def continuemax(string):
    digits = []
    digitstrs = []
    is_digit = 0
    for item in range(len(string)):
        if string[item].isdigit():
            digits.append(string[item])
            is_digit = 1
            continue
        if (not string[item].isdigit()) and is_digit==1:
            digitstrs.append(digits)
            digits = []
            is_digit = 0
            continue
        if (not string[item].isdigit()) and is_digit==0:
            continue
    if item==len(string)-1 and len(digits)>0:
        digitstrs.append(digits)

    origin_strs = digitstrs[0]
    max = len(origin_strs)
    for strs in digitstrs:
        if len(strs)>max:
            max = len(strs)
            origin_strs = strs

    maxstrs = []
    for strs in digitstrs:
        if len(strs)==len(origin_strs):
            maxstrs.append(strs)
    printstrs = []
    for item in maxstrs:
        maxstr = ''.join(map(lambda x: str(x), item))
        printstrs.append(maxstr)
    return printstrs, max

if __name__ == "__main__":
    print arithmetic_sequence(2,3,2)
    print AutomorphicNumbers(10000)
    string, newstring = addsignal('Jkdi234klowe90a3')
    print "%s to %s" % (string, newstring)
    voters = count(['A','B','C','D'], ['A','B','C','D','E','F','G','H','B','A','D'])
    for candidate, votes in voters.items():
        print "%s: %s" % (candidate, votes)
    print continuemax('abcd123456789ed125ss123058789')