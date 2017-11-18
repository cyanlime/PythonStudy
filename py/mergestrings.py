def strings_process(str1, str2):
    strings = str1+str2
    string = []
    for s in strings:
        string.append(s)

    if len(string)%2==0:
        odd_max = len(string)
        even_max = len(string)-1
    else:
        odd_max = len(string)-1
        even_max = len(string)   

    for item in range(0, even_max, 2):
        for item2 in range(item+2, even_max, 2):
            if string[item]>string[item2]:
                temp = string[item]
                string[item] = string[item2]
                string[item2] = temp
    for item in range(1, odd_max, 2):
        for item2 in range(item+2, odd_max, 2):
            if string[item]>string[item2]:
                temp = string[item]
                string[item] = string[item2]
                string[item2] = temp

    values = []
    for item in string:
        if item=='a' or item=='A':
            char = '1010'
        elif item=='b' or item=='B':
            char = '1011'
        elif item=='c' or item=='C':
            char = '1100'
        elif item=='d' or item=='D':
            char = '1101'
        elif item=='e' or item=='E':
            char = '1110'
        elif item=='f' or item=='F':
            char = '1111'
        elif item==0:
            char = '0000'
        elif item==1:
            char = '0001'
        elif item==2:
            char = '0010'
        elif item==3:
            char = '0011'
        elif item==4:
            char = '0100'
        elif item==5:
            char = '0101'
        elif item==6:
            char = '0110'
        elif item==7:
            char = '0111'
        elif item==8:
            char = '1000'
        elif item==9:
            char = '1001'
        else:
            values.append(char)
        # chars = []
        # item = 0
        # for item in range(len(char)):
        #     chars.append(char[item])
        # chars = chars[::-1]       
        # value = 8*int(chars[0])+4*int(chars[1])+2*int(chars[2])+int(chars[3])
        value = 8*int(char[3])+4*int(char[2])+2*int(char[1])+int(char[0])
        if 10<=value<=15:
            if value==10:
                value = 'A'
            if value==11:
                value = 'B'
            if value==12:
                value = 'C'
            if value==13:
                value = 'D'
            if value==14:
                value = 'E'
            if value==15:
                value = 'F'
        values.append(value)
    pro_string = ''.join(map(lambda x: str(x), values))
    return pro_string

if __name__ == "__main__":
    print strings_process('dec','fab')