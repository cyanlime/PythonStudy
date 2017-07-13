#14 3

def reverse_printing(num):
    array = []
    reverse_array = []

    if type(num)!=int:
        return IOError("please input a integer")
    strnum = str(num)
    print "length of number is %s" % len(strnum)

    for item in range(len(strnum)):
        array.append(strnum[item])
        # temp = strnum[item]
        # strnum[item] = strnum[len(strnum)-1-item] 
        # strnum[len(strnum)-1-item] = temp

    #restrnum = ''
    while len(array)>0:
        item = array.pop()
        #restrnum = restrnum.join(item)
        reverse_array.append(item)
    restrnum = ''.join(map(lambda x: str(x), reverse_array))
    return restrnum

if __name__ == "__main__":
    print reverse_printing(23456707)