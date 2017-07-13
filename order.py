def namelist():
    # A = [a, b, c]
    # B = [x, y, z]

    # a!:x
    # c!:x,z

    A = ['a','b','c']
    B = ['x','y','z']
    complist = []
    complist2 = []
    for item in A:
        for item2 in B:
            comp = item+item2
            if comp!='ax' and comp!='cx' and comp!='cz':
                complist.append(comp)


def select(complist):
    dicA = {}
    listA = []
    comp = []
    for item in complist:
        comA = item[0]
        if comA not in listA:
            listA.append(comA)
            numA=1
            dicA[comA]=numA
        else:
            numA+=1
            dicA[comA]=numA          
    print dicA

    for value in dicA.values():
        if len(dicA.values())==1 and value==1:
            return comp

    for key in dicA:
        if dicA[key]==1:
            first_key = key

    for item in complist:
        if item[0]==first_key:
            print item
            first_comp = item
    comp.append(first_comp)
    print first_comp

    first_complist = []
    for item2 in complist:
        if item2[1]!=first_comp[1] and item2!=first_comp:
            first_complist.append(item2)
    
    print first_complist
    select(first_complist)

    

    
        





if __name__ == "__main__":
    print namelist()
    print select(['ay', 'az', 'bx', 'by', 'bz', 'cy'])