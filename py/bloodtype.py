import sys

def factorcombine(factors):
    bloodtypes = []
    for factor in factors:
        if factor.keys()[0] in ["ai", "ia", "aa"]:
            bloodtypes.append({"A": factor.values()[0]})
        elif factor.keys()[0] in ["bi", "ib", "bb"]:
            bloodtypes.append({"B": factor.values()[0]})
        elif factor.keys()[0] == "ii":
            bloodtypes.append({"O": factor.values()[0]})
        elif factor.keys()[0] in ["ab", "ba"]:
            bloodtypes.append({"AB": factor.values()[0]})
        else:
            raise ValueError("factor incorrect")
    return bloodtypes

def merge(bloodfactors):
    simfactors = []
    simbloodfactors = []
    for item in bloodfactors:
        if item.keys()[0] not in simfactors:
            simfactors.append(item.keys()[0])
            simbloodfactors.append(item)
        else:
            for item2 in simbloodfactors:
                if item2.keys()[0]==item.keys()[0]:
                    temp=item2.values()[0]+item.values()[0]
                    item2[item2.keys()[0]]=temp
    return simbloodfactors

def bloodtypefactor(bloodtype):
    if bloodtype == "A":
        return {"aa": 0.5, "ai": 0.5}
    elif bloodtype == "B":
        return {"bb": 0.5, "bi": 0.5}
    elif bloodtype == "O":
        return {"ii": 1}
    elif bloodtype == "AB":
        return {"ab": 1}
    else:
        raise ValueError("please input correct bloodtype")
    

def inheritance_bloodtype(father,mother):
    #father=bloodtypefactor("A")
    keys = []
    keys2 = []
    bloodfactors=[]
    for key in father.keys():
        for item in key:
            keys.append({item: 0.5*father[key]})
    for key2 in mother.keys():
        for item2 in key2:
            keys2.append({item2: 0.5*mother[key2]})
    for factor in keys:
        for factor2 in keys2:
            bloodfactor = {factor.keys()[0]+factor2.keys()[0]: factor.values()[0]*factor2.values()[0]}
            bloodfactors.append(bloodfactor)
    return bloodfactors

if __name__ == "__main__":
    child = inheritance_bloodtype(bloodtypefactor("AB"),bloodtypefactor("AB"))
    child = merge(factorcombine(child))
    print child
    for item in child:
        print "child‘s bloodtype: %s %% of %s" % (100*item.values()[0], item.keys()[0])
