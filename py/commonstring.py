def common_strings(str1,str2):
    commonstrs = []
    strs = []
    common = 0
    item1=0
    item2=0
    origin_item1=0
    while item2<len(str2)-1:
        while item1<len(str1)-1:
            if str1[item1]==str2[item2]:
                strs.append(str1[item1])
                common = 1
                item1+=1
                item2+=1
                continue
            if str1[item1]!=str2[item2] and common==0:
                item1+=1
                continue
            if str1[item1]!=str2[item2] and common==1:
                commonstrs.append(strs)
                common = 0
                strs = []
                origin_item1=item1
                item1+=1
        item2+=1
        item1=origin_item1

    if item2==len(str2) and common==1:
        strs.append(str2[item2-1])
        commonstrs.append(strs)  
    return commonstrs

if __name__ == "__main__":
    print common_strings('abcdefghijklmnwefopefghig','abcsafjklmnopqrstuvwopefghig')