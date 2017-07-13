def IP_legal(array):
    illegal_ip = []
    legal_ip = []
    for item in array:
        nums = []
        for item2 in range(len(item)):
            if item[item2]!='.':
                nums.append(item[item2])
            else:
                num = ''.join(map(lambda x: str(x), nums))
                if int(num)>=0 and int(num)<=255:
                    nums = []
                    continue
                else:
                    illegal_ip.append(item)
                    break

    for item in array:
        if item not in illegal_ip:
            legal_ip.append(item)
    return legal_ip, illegal_ip

if __name__ == "__main__":
    legal_ip, illegal_ip = IP_legal(['255.255.255.255','512.12.2.3','0.0.0.1','192.123.333.1'])
    print 'legal ip: %s' % (', '.join(map(lambda x: str(x), legal_ip)))
    print 'illegal ip: %s' % (', '.join(map(lambda x: str(x), illegal_ip)))
