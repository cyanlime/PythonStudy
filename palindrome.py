def palindrome(num):
    flag = True

    strnum = str(num)
    for item in range(len(strnum)/2):
        if strnum[item] != strnum[len(strnum)-1-item]:
            flag = False
            print "%s is not a palindrome number." % num
            break
    
    if flag == True:
        print "%s is a palindrome number." % num


if __name__ == "__main__":
    palindrome(12348894321)