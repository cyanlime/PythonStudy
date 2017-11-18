def encrypt(passwd, result):
    enc_passwd = []
    for item in range(len(passwd)):
        if passwd[item].islower():
            if passwd[item]=='z':
                char = chr(ord(passwd[item].upper())+1-26)
            else:        
                char = chr(ord(passwd[item].upper())+1)
        elif passwd[item].isupper():
            if passwd[item]=='Z':
                char = chr(ord(passwd[item].lower())+1-26)
            else:
                char = chr(ord(passwd[item].lower())+1)
        elif passwd[item].isdigit():
            char = (int(passwd[item])+1)%10
        else:
            char = passwd[item]
        enc_passwd.append(char)
    encpasswd = ''.join(map(lambda x: str(x), enc_passwd))

    item = 0
    unenc_passwd = []
    for item in range(len(result)):
        if result[item].islower():
            if result[item]=='a':
                char = chr(ord(result[item].upper())-1+26)
            else:        
                char = chr(ord(result[item].upper())-1)
        elif result[item].isupper():
            if result[item]=='A':
                char = chr(ord(result[item].lower())-1+26)
            else:
                char = chr(ord(result[item].lower())-1)
        elif result[item].isdigit():
            char = (int(result[item])-1)%10
        else:
            char = result[item]
        unenc_passwd.append(char)
    unencpasswd = ''.join(map(lambda x: str(x), unenc_passwd))
    return encpasswd, unencpasswd

if __name__ == "__main__":
    print encrypt('abcDefg9zZ0$', 'BCDeFGH0Aa1$')