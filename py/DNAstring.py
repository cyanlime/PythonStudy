"""undone"""

def GCstring(string, minlen):
    # GCstrings = {}
    # GCstr = []
    # GCappear = 0
    # GClen = 0
    # totallen = 0
    # for item in range(len(string)):
    #     if (string[item]=='G' or string[item]=='C') and GCappear==0:
    #         GCstr.append(string[item])
    #         GCappear = 1
    #         GClen+=1
    #         totallen+=1
    #         continue
    #     if string[item]!='G' and string[item]!='C' and GCappear==1 and totallen<minlen:
    #         GCstr.append(string[item])
    #         totallen+=1
    #         continue
    #     if (string[item]=='G' or string[item]=='C') and GCappear==1:
    #         GCstr.append(string[item])
    #         GClen+=1
    #         totallen+=1
    #         continue
    #     if string[item]!='G' and string[item]!='C' and GCappear==1 and totallen>=minlen:
    #         GCstrings[str(GClen)+'/'+str(totallen)]=[]
    #         GCstrings[str(GClen)+'/'+str(totallen)].append(GCstr)
    #         GCstr = []
    #         GCappear = 0
    #         GClen = 0
    #         totallen = 0
    # return GCstrings

    GCitems = []
    for item in range(len(string)):
        if string[item]=='G' or string[item]=='C':
            GCitems.append(item)

    GCs = []
    for item in GCitems:
        if item+4 in GCitems:
            GCs.append(item)

    dic = {}
    GCstrings = []
    for item in GCs:
        for item2 in range(item, item+5):
            if item2 in GCitems:
                GCstrings.append(item2)
        dic[item]=GCstrings
        GCstrings = []

    lenvalues = len(dic.values()[0])
    for key, values in dic.items():
        if len(values)>lenvalues:
            lenvalues = len(values)

    items = []
    for key, values in dic.items():
        if len(values)==lenvalues:
            items.append(key)

    minitem = items[0]
    for item in items:
        if item<minitem:
            minitem=item
    
    max_GCstrings=string[minitem:minitem+5]     
    return max_GCstrings

if __name__ == "__main__":
    print GCstring('AACTGTGCACGACCTGA', 5)