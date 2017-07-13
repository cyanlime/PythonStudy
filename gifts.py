def gift(gifts):
    dic = {}
    for item in gifts:
        if item not in dic:
            dic[item]=1
        else:
            dic[item]+=1

    for key in dic.keys():
        if dic[key]>len(gifts)/2:
            return key
    return 0

def string_replace(string, arg):
    num = 0
    replace_string = []
    for item in range(len(string)):
        if string[item]=='s':
            if item==0 or (item!=0 and string[item-1]!='%'):
                replace_string.append(string[item])
        else:
            if string[item]=='%':
                replace_string.append(arg[num])
                num+=1
            else:
                replace_string.append(string[item])

    if len(arg)>num:
        for item2 in range(num, len(arg)):
            replace_string.append(arg[item2])
    restr = ''.join(map(lambda x: str(x), replace_string))
    return restr

def illegal(expression):
    braces = []
    brackets = []
    small_brackets = []
    for item in range(len(expression)):
        if expression[item] in ['{', '}', '[', ']', '(', ')']:
            if expression[item]=='{':
                braces.append(expression[item])
                continue
            if expression[item]=='}' and len(brackets)==0 and len(small_brackets)==0:
                if len(braces)>0:
                    braces.pop()
                    continue
                else:
                    return False

            if expression[item]=='[':
                brackets.append(expression[item])
                continue
            if expression[item]==']':
                if len(brackets)>0 and len(small_brackets)==0:
                    brackets.pop()
                    continue
                else:
                    return False

            if expression[item]=='(':
                small_brackets.append(expression[item])
                continue
            if expression[item]==')':
                if len(small_brackets)>0:
                    small_brackets.pop()
                    continue
                else:
                    return False
    
    if len(braces)==0 and len(brackets)==0 and len(small_brackets)==0:
        return True
    else:
        return False
    
import copy
def delete(max):
    array = []
    if max>1000:
        max=1000
    for num in range(max):
        array.append(num)

    pops = []
    newarray = []
    origin_array = copy.deepcopy(array)

    num = 0
    while len(array)>1:
        if num==0:
            for item in range(2, len(array), 3):
                pops.append(array[item])
        else:
            for item in range(0, len(array), 3):
                pops.append(array[item])
     
        for num in array:
            if num not in pops:
                newarray.append(num)        
        item=(item+2)%(len(array)-1)
        num+=1
        array = newarray
        pops = []
        newarray = []
    return array[0]

def shoot(p,n,nums):
    baskets = []
    for num in nums:
        basket = num%p
        if basket not in baskets:
            baskets.append(basket)
        else:
            return num
    if len(baskets)<=p:
        return -1

def interval(array):
    intervals = []
    for item in range(2,len(array),1):
        diff = array[item]-array[item-2]
        intervals.append(diff)
    max = intervals[0]
    for num in range(len(intervals)):
        if intervals[num]>max:
            max=intervals[num]
    return max, num


if __name__ == "__main__":
    print gift([1,2,3,3,3,2,2])
    print string_replace('sA%sC%ssE', ['B','D','F'])
    print illegal("[a+b*(5-4)]*{x+b+b*{(1+2)}}")
    print delete(8)
    print shoot(10,5,[0,21,53,41,55])
    print interval([1,2,3,7,8])