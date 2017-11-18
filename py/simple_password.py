def simpasswd(string):
    originpasswd = []
    newpasswd = []
    for item in range(len(string)):
        if string[item].isupper():
            char = string[item].lower()
            # if char=='z':
            #     newchar = 'a'
            # else:
            #     newchar = chr(ord(char)+1)
            newchar = chr((ord(char)+1-ord('a'))%26+ord('a'))
            newpasswd.append(newchar)
            continue
        elif string[item].islower():
            num = 1
            if ord('a')<=ord(string[item])<=ord('o'):
                for charnum in range(ord('a'), ord('o')+1, 3):
                    num+=1
                    if ord(string[item])<charnum:
                        newchar = num-1
                        break
            elif string[item] in ['p', 'q', 'r', 's']:
                newchar = 7
            elif string[item] in ['t', 'u', 'v']:
                newchar = 8
            else:
                newchar = 9
            newpasswd.append(str(newchar))
            continue
        else:
            newchar = string[item]
            if string[item].isdigit():
                newpasswd.append(str(newchar))
            else:
                newpasswd.append(newchar)
            continue
    passwd = ''.join(map(lambda x: str(x), newpasswd))
    return passwd, string

if __name__ == "__main__":
    password, string = simpasswd('$YUANzhi1987')
    print "password %s to newpassword %s" % (string, password)