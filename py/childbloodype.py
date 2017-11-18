def bloodtypefactor(bloodtype):
    if bloodtype == "A":
        return ["a", "i"]
    elif bloodtype == "B":
        return ["b", "i"]
    elif bloodtype == "O":
        return ["i"]
    elif bloodtype == "AB":
        return ["a", "b"]
    else:
        raise ValueError("please input correct bloodtype")

def factorcombine(factors):
    bloodtypes = []
    for factor in factors:
        if factor in ["ai", "ia", "aa"]:
            if "A" not in bloodtypes:
                bloodtypes.append("A")
        elif factor in ["bi", "ib", "bb"]:
            if "B" not in bloodtypes:
                bloodtypes.append("B")
        elif factor == "ii":
            if "O" not in bloodtypes:
                bloodtypes.append("O")
        elif factor in ["ab", "ba"]:
            if "AB" not in bloodtypes:
                bloodtypes.append("AB")
        else:
            raise ValueError("factor incorrect")
    return bloodtypes

def inheritance_bloodtype(father,mother):
    #father=bloodtypefactor("A")
    bloodfactors=[]
    for item in father:
        for item2 in mother:
            bloodfactors.append(item+item2)
    blood_types=factorcombine(bloodfactors)
    return blood_types


class Person():
    def __init__(self, name='', gender='', bloodtype=''):
        self.name = name
        self.gender = gender
        self.bloodtype = bloodtype

class Father(Person):
    def __init__(self, name='', bloodtype=''):
        Person.__init__(self,name,'male',bloodtype)

class Mother(Person):
    def __init__(self, name='', bloodtype=''):
        Person.__init__(self,name,'female',bloodtype)

if __name__ == "__main__":
    micheal = Father('micheal', 'O')
    sara = Mother('sara', 'AB')

    print micheal.name, micheal.gender, micheal.bloodtype
    print sara.name, sara.gender, sara.bloodtype

    child = inheritance_bloodtype(bloodtypefactor(micheal.bloodtype), bloodtypefactor(sara.bloodtype))
    print 'child bloodtype maybe: %s' % child