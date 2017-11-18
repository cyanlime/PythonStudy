def IP_category(array):
    IP_addresses = []
    subnet_maskes = []
    for item in array:
        is_subnet_mask = 0
        IP_address = []
        subnet_mask = []
        for char in range(len(item)):
            if item[char]!='~' and is_subnet_mask==0:
                IP_address.append(item[char])
            if item[char]=='~' and is_subnet_mask==0:
                IPaddress = ''.join(map(lambda x: str(x), IP_address))
                IP_addresses.append(IPaddress)
                is_subnet_mask=1
            if item[char]!='~' and is_subnet_mask==1:
                subnet_mask.append(item[char])
            if char==len(item)-1:
                subnetmask = ''.join(map(lambda x: str(x), subnet_mask))
                subnet_maskes.append(subnetmask)
    #return IP_addresses, subnet_maskes

    A_IPs = []
    B_IPs = []
    C_IPs = []
    D_IPs = []
    E_IPs = []
    private_IPs = []
    illegal_IPs = []
    illegal_subnet_masks = []

    for item in IP_addresses:
        nums = []
        is_dot = 0
        is_A = 0
        is_B = 0
        is_C = 0
        is_D = 0
        is_E = 0
        is_A_private = 0
        is_B_private = 0
        is_C_private = 0
        for char in range(len(item)):
            if item[char]!='.':
                nums.append(item[char])

            if item[char]=='.' and is_dot==0:
                num = ''.join(map(lambda x: str(x), nums))
                if num=='':
                    illegal_IPs.append(item)
                    break
                else:
                    if int(num)>255:
                        illegal_IPs.append(item)
                        break
                    elif 1<=int(num)<=126:
                        if int(num)!=10:
                            is_A = 1
                        else:
                            is_A_private = 1
                    elif 128<=int(num)<=191:
                        if int(num)!=172:
                            is_B = 1
                        else:
                            is_B_private = 1
                    elif 192<=int(num)<=223:
                        if int(num)!=192:
                            is_C = 1
                        else:
                            is_C_private = 1
                    elif 224<=int(num)<=239:
                        is_D = 1
                    elif 240<=int(num)<=255:
                        is_E = 1
                    is_dot = 1
                    nums = []
                    continue

            if item[char]=='.' and is_dot==1:
                num = ''.join(map(lambda x: str(x), nums))
                if num=='':
                    illegal_IPs.append(item)
                    break
                else:
                    if int(num)>255 or int(num)<0:
                        illegal_IPs.append(item)
                        break
                    else:
                        if is_B_private==1 and 16<=int(num)<=31:
                            is_B_private = 2
                        if is_C_private==1 and int(num)==168:
                            is_C_private = 2
                        is_dot = 2
                        nums = []
                        continue

            if (item[char]=='.' and is_dot==2) or (is_dot==3 and char==len(item)-1):
                num = ''.join(map(lambda x: str(x), nums))
                if num=='':
                    illegal_IPs.append(item)
                    break
                else:
                    if int(num)>255 or int(num)<0:
                        illegal_IPs.append(item)
                        break
                    is_dot+=1
                    nums = []

            if is_dot==4:
                if is_A == 1:
                    A_IPs.append(item)
                if is_B == 1 or is_B_private==1:
                    B_IPs.append(item)
                if is_C == 1 or is_C_private==1:
                    C_IPs.append(item)
                if is_D == 1:
                    D_IPs.append(item)
                if is_E == 1:
                    E_IPs.append(item)
                if is_A_private==1 or is_B_private==2 or is_C_private==2:
                    private_IPs.append(item)
                break

    #return private_IPs, A_IPs, B_IPs, C_IPs, D_IPs, E_IPs, illegal_IPs

    masks = []
    nums = []
    num = 1
    for item in range(0,9):
        while len(nums)<item:
            nums.append(num)
        while len(nums)<8:
            nums.append('0')
        mask = ''.join(map(lambda x: str(x), nums))
        masks.append(mask)
        nums = []

###""" handle subnet mask """
    value = 1
    num = 0
    values = []
    for item in masks:
        for length in range(0, len(item)):
            if length== 0:
                value = 1
            else:
                value*=2
            num+=int(item[len(item)-1-length])*value
        values.append(str(num))
        num = 0

    second_values = []
    for num in values:
        if num!='0' and num!='128':
            second_values.append(num)

    third_values = []
    for num in values:
        if num!='0':
            third_values.append(num)

    
    illeagel_subnet_masks = []
    for item in subnet_maskes:
        chars = []
        is_dot = 0
        next = 0
        last_255 = 0
        for char in range(len(item)):
            if item[char]!='.':
                chars.append(item[char])
            if item[char]=='.' and is_dot==0:
                num = ''.join(map(lambda x: str(x), chars))
                if num=='' or num!='255':
                    illeagel_subnet_masks.append(item)
                    break
                chars=[]
                is_dot=1
                continue
            if item[char]=='.' and is_dot==1:
                num = ''.join(map(lambda x: str(x), chars))
                if num not in second_values:
                    illeagel_subnet_masks.append(item)
                    break
                if num=='255':
                    last_255=1
                chars=[]
                is_dot=2
                continue
            if item[char]=='.' and is_dot==2:
                num = ''.join(map(lambda x: str(x), chars))
                if last_255==0 and num!='0':
                    illeagel_subnet_masks.append(item)
                    break
                if last_255==1 and num=='255':
                    last_255=1
                if last_255==1 and (num in third_values) and num!='255':
                    last_255=0
                chars = []
                is_dot=3
                continue
            if is_dot==3 and char==len(item)-1:
                num = ''.join(map(lambda x: str(x), chars))
                if (last_255==0 and num!='0') or (last_255==1 and (num not in values)):
                    illeagel_subnet_masks.append(item)
                    break

    return private_IPs, A_IPs, B_IPs, C_IPs, D_IPs, E_IPs, illegal_IPs, illeagel_subnet_masks

if __name__ == "__main__":
    private_IPs, A_IPs, B_IPs, C_IPs, D_IPs, E_IPs, illegal_IPs, illeagel_subnet_masks = IP_category(['10.70.44.68~255.254.255.0', '1.0.0.1~255.0.0.0', '192.168.0.2~255.255.240.0','19..0.~255.192.0.0'])
    print "private IPs: %s, A IPs: %s, B IPs: %s, C IPs: %s, D IPs: %s, E IPs: %s, illeageal IPs: %s, illeagel subnet masks %s" % (private_IPs, A_IPs, B_IPs, C_IPs, D_IPs, E_IPs, illegal_IPs, illeagel_subnet_masks)
