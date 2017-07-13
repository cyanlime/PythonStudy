import hello
import datetime

def even_numbers(max):
    evennums = []
    for num in range(1, max+1):
        if num%2==0:
            evennums.append(num)
    return evennums

def call():
    beginning_time = datetime.datetime.now()
    berry = hello.hello('berry')
    ending_time = datetime.datetime.now()
    costtime = ending_time-beginning_time
    print '%s [timecosts: %s]' % (berry, costtime)

def hump_to_underline(name):
    humps = []
    for item in range(len(name)):
        humps.append(name[item])

    for item2 in range(0, len(humps)-1):
        if humps[item2].isupper():
            if humps[item2+1].islower():
                humps[item2] = humps[item2].lower()
                if item2!=0:
                    humps.insert(item2, '_')
            if humps[item2+1].isupper():
                continue
        
    for item2 in range(1, len(humps)):
        if humps[item2-1].islower() and humps[item2].isupper():
            humps.insert(item2, '_')
    
    if humps[0].isupper():
        humps[0] = humps[0].lower()
            
    newname = ''.join(map(lambda x: str(x), humps))
    return name, newname

def transfer(inputStr):
    reversedInputStr = inputStr[::-1]
    words = []
    buffer = ''
    preCharIsUpper = True
    preWordIsUpper = None
    for char in reversedInputStr:
        isUpper = True if char.isupper() else False
        if isUpper:
            if preCharIsUpper:
                buffer += char
                preWordIsUpper = True
            else:
                preCharIsUpper = True
                buffer += char
                words.append(buffer.lower()[::-1])
                buffer = ''
                preWordIsUpper = False
        else:
            if preCharIsUpper:
                preCharIsUpper = False
                if len(buffer) > 0:
                    buffer = buffer[::-1] if len(buffer) > 1 else buffer[::-1].lower()
                    words.append(buffer)
                    buffer = ''
                buffer += char
                preWordIsUpper = False
            else:
                buffer += char
                preWordIsUpper = False
    if len(buffer) > 0:
        if preWordIsUpper:
            buffer = buffer[::-1] if len(buffer) > 1 else buffer[::-1].lower()
            words.append(buffer)
        else:
            words.append(buffer.lower()[::-1])
    return '_'.join(words[::-1])

        



if __name__ == "__main__":
    #print even_numbers(10000)

    #print transfer("GetITATMyself")
    #print transfer("getMyself")
    #print transfer("GGGetItemMyself")
    print transfer("ITGirl")
    print transfer("someThing")
    print transfer("numCPUCore")
    print transfer("rayXYZ")
    #print transfer("getAMyselfITGirl")
    #print transfer("GetMyselfIT")
    #print transfer("AGetMyselfITGame")
    #print transfer("geteAAAgain")

    call()
    name, newname = hump_to_underline('GetITATMyself')
    name, newname = hump_to_underline('getMyself')
    name1, newname1 = hump_to_underline('GetItemMyself')
    name2, newname2 = hump_to_underline('getAMyselfITGirl')
    name3, newname3 = hump_to_underline('GetMyselfIT')
    name4, newname4 = hump_to_underline('AGetMyselfITGame')
    name5, newname5 = hump_to_underline('geteAAAgain')


    print '%s transfer to %s' % (name, newname)
    print '%s transfer to %s' % (name1, newname1)
    print '%s transfer to %s' % (name2, newname2)
    print '%s transfer to %s' % (name3, newname3)
    print '%s transfer to %s' % (name4, newname4)
    print '%s transfer to %s' % (name5, newname5)