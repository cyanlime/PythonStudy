""" continue """
def param_split(string):
    string.split(' ')

    a = '“C:\program files”'
    print len(a)
    for item in range(len(a)):
        print a[item]
    
    params = []
    param = []
    qutoes = 0
    for item in range(len(string)):
        if (string[item]!=' ' and string[item]!='"') or (string[item]==' ' and qutoes==1):
            param.append(string[item])
            continue
        if string[item]==' ' and qutoes==0:
            para = ''.join(map(lambda x: str(x), param))
            params.append(para)
            param = []
            continue
        if string[item]=='\"':
            quotes = 1
            continue
        if string[item]=='"' and quotes==1:
            qutoes = 0
            continue
    return params


if __name__ == "__main__":
    param_split('xcopy /s “C:\program files” “d:\”')