def password_legality(array):
    illegal_passwords = []
    origin_legal_passwords = []

    for passwd in array:
        if len(passwd)<=8:
            illegal_passwords.append(passwd)
            break
        item = 0
        while item<len(passwd):
            char = passwd[item]
            num = 0
            while passwd[item]==char and item<len(passwd)-1:
                num+=1
                item+=1
                if num==3:
                    illegal_passwords.append(passwd)
                    break
                if item==len(passwd)-1:
                    if passwd[item]==char and num==2:
                        illegal_passwords.append(passwd)
                        break
                    else:
                        origin_legal_passwords.append(passwd)

            if item==len(passwd)-1 or (passwd in illegal_passwords):
                break
    #return orign_legal_passwords, illegal_passwords
    is_upper = 0
    is_lower = 0
    is_digit = 0
    is_other_signal =0
    for item in origin_legal_passwords:
        for char in range(len(item)):
            if item[char].isupper():
                is_upper = 1
            elif item[char].islower():
                is_lower = 1
            elif item[char].isdigit():
                is_digit = 1
            else:
                is_other_signal=1
        if (is_upper==0 and is_lower==0) or (is_upper==0 and is_digit==0) or (is_upper==0 and is_other_signal==0) or (is_lower==0 and is_digit==0) or \
            (is_digit==0 and is_other_signal==0) or (is_lower==0 and is_other_signal==0):
            illegal_passwords.append(item)

    legal_passwords = []
    for item in origin_legal_passwords:
        if item not in illegal_passwords:
            legal_passwords.append(item)
    return legal_passwords, illegal_passwords

if __name__ == "__main__":
    legal_passwords, illegal_passwords = password_legality(['0211Abc900', '021abc9abc1', '021ABC9000', '021$bc9000'])
    print "legal passwords: %s, illegal_passwords: %s" % (legal_passwords, illegal_passwords)