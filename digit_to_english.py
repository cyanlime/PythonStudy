def parse(num):
    strnum = str(num)
    words = []
    for item in range(len(strnum)-1, -1, -1):
        words.append(strnum[item])

    hundred = words[:3]
    thousand = words[3:6]
    million = words[6:len(words)]

    hundred = hundred[::-1]
    thousand = thousand[::-1]
    million = million[::-1]

    units = ['zero','one','two','three','four','five','six','seven','eight','nine']
    tens = ['ten','eleven','twelve','thirteen','fourteen','fifteen','sixteen','seventeen','eighteen','nineteen']
    tens_more = ['zero','ten','twenty','thirty','forty','fifty','sixty','seventy','eighty','ninety']

    reads = []
    if len(million)>0:
        if len(million)==3:
            num = int(million[0])
            reads.append(units[num])
            reads.append('hundred')
            reads.append('and')

            num = int(million[1])
            if num>1:
                reads.append(tens_more[num])
                if num!=0:
                    num = int(million[2])
                    reads.append(units[num])
            else:
                num = int(million[1])
                reads.append(tens[num])

        if len(million)==2:
            num = int(million[0])
            if num>1:
                reads.append(tens_more[num])
                num = int(million[1])
                if num!=0:
                    reads.append(units[num])
            else:
                num = int(million[1])
                reads.append(tens[num])
        
        if len(million)==1:
            num = int(million[0])
            reads.append(units[num])

        reads.append('million')
        reads.append('and')

if __name__ == "__main__":
    parse(23456789)