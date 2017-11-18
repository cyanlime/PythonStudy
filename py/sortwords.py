def sort_words(array):
    for item in range(len(array)-1):
        for item2 in range(item+1, len(array)):
            if (array[item][0]).lower()>(array[item2][0]).lower():
                temp = array[item]
                array[item] = array[item2]
                array[item2] = temp

    for item in range(len(array)-1):
        for item2 in range(item+1, len(array)):
            if (array[item][0]).lower()==(array[item2][0]).lower() and array[item][0]<array[item2][0]:
                temp = array[item]
                array[item] = array[item2]
                array[item2] = temp

    for item in range(len(array)-1):
        for item2 in range(item+1, len(array)):
            if array[item][0]==array[item2][0]:
                if len(array[item])>len(array[item2]):
                    leng = len(array[item2])
                else:
                    leng = len(array[item])
            
                if array[item][1]==array[item2][1] and len(array[item2])==2:
                        temp = array[item]
                        array[item] = array[item2]
                        array[item2] = temp
                        continue

                n = 1
                while n<leng:
                    if array[item][n]==array[item2][n]:
                        n+=1
                    elif array[item][n]>array[item2][n]:              
                        temp = array[item]
                        array[item] = array[item2]
                        array[item2] = temp
                        break
                    else:
                        break
    return array          

if __name__ == "__main__":
    print sort_words(['cap', 'to', 'cat', 'card', 'Two', 'To', 'ad', 'ac', 'Top', 'Too', 'Toe', 'toe', 'top', 'warn' ,'up', 'boat', 'boot'])